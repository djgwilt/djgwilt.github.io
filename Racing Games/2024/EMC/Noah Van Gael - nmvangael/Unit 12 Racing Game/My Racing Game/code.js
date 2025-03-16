const output = document.getElementById("output");


OUTPUT_PATCH = `
import sys
import io
sys.stdout = io.StringIO()
from js import addToOutput
orig_print = print
# redirect print via output textarea and console
def new_print(*args, **kwargs):
  stdout_len = len(sys.stdout.getvalue())
  orig_print(*args, **kwargs)
  stdout = sys.stdout.getvalue()
  addToOutput(stdout[stdout_len:])
  sys.stdout.flush()
print = new_print
`

INPUT_PATCH = `
from js import input_patch
input = input_patch
__builtins__.input = input_patch
`

function addToOutput(s) {
  output.value += s;
  console.log(s);
}

window.onerror = function(msg, url, lineNo, columnNo, error) {
  try {
    addToOutput("Error occurred: to view, run page in new tab & use ctrl-shift-j to view console");  
    pyodide.runPython("window.clearInterval(intervalHandle)");  
  } catch(err) {}
};

var pyodide = undefined;

async function main(){
  pyodide = await loadPyodide();
  pyodide.setDebug(true)
}

function input_patch(text) {
  return prompt(text);
};

pyodideReadyPromise = main();

async function evaluatePython(code) {
  await pyodideReadyPromise;
  pyodide.runPython(OUTPUT_PATCH);
  pyodide.runPython(INPUT_PATCH);
     
  try {
    pyodide.runPython(code);
  } catch(err) {
    addToOutput(err);
  }
}

function checkCellIds() {
  let $table = $("#racing_track");
  if ($table.length !== 1) {
    addToOutput("Make sure you have a table with id 'RacingTrack'.\n")
    return false;
  }
  let $rows = $table.find("tr");
  if ($rows.length < 1) {
    addToOutput("Warning: couldn't find any rows in the table.")
  }
  for (let iRow = 0; iRow < $rows.length; iRow++) {
    let $row = $($rows[iRow]);
    let $cells = $row.find("td");
    let res = $cells.map((iCol, cell) => {
      if (cell.id !== `R${iRow}C${iCol}`) {
        addToOutput(`Incorrect cell ID. Expected: 'R${iRow}C${iCol}', found: '${cell.id}'.\n`)
        return false;
      }
      return true;
    });
    if (!res.get().every(x => x)) {
      return false;
    }
  }
  return true;
}

$(document).ready(() => {
  if (checkCellIds()) {
    addToOutput("Ready!\n");
    $.get("game.py", function(data) {
      evaluatePython(data);
    });
  } else {
    addToOutput("There were issues with your HTML table. Please fix them and try again.")
  }
});

function remove_shield() {
  addToOutput("shield down");

  let element;
  if (document.getElementById("shield3") && document.getElementById("shield3").classList.contains("shield")) {
    element = document.getElementById("shield3");
    element.classList.remove("shield");
    addToOutput("shield 1 down");
  } else if (document.getElementById("shield2") && document.getElementById("shield2").classList.contains("shield")) {
    element = document.getElementById("shield2");
    element.classList.remove("shield");
    addToOutput("shield 2 down");
  } else if (document.getElementById("shield1") && document.getElementById("shield1").classList.contains("shield")) {
    element = document.getElementById("shield1");
    element.classList.remove("shield");
    addToOutput("shield 3 down");
  }
}