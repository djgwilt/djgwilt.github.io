// listen for keypress (to detect arrow keys)
document.onkeydown = checkKey
// to store movement direction
var xDir = 0
var yDir = 0
// to store current column position
var row = 1
var column = 1
// to store the handle code for the timer interval to cancel it when we crash
var intervalHandle
// to count score
var score = 0
var speed = 300
//to store squares
var emptys = []
var walls = []
var kills = []
//to store apple
var acoords = "RBCB"
// the function called when a key is pressed - sets direction variable
function checkKey(e) {
  // this next line is a workaround for older versions of IE which didn't pass the event as a parameter
  e = e || window.event
  if(e.keyCode == '39') {
    // right arrow
    xDir = 1
    yDir = 0
  } else if(e.keyCode == '37') {
    // left arrow
    xDir = -1
    yDir = 0
  } else if(e.keyCode == '38') {
    // up arrow
    xDir = 0
    yDir = -1
  } else if(e.keyCode == '40') {
    // down arrow
    xDir = 0
    yDir = 1
  }
}
// called when the page is loaded to start the timer checks
function runGame() {
  generate(6, 6)
  document.getElementById("R1C1").className = "PlayerClosed"
  document.getElementById(acoords).className = "Apple"
  intervalHandle = setInterval(updatePosition, speed)
  document.getElementById("Message").innerText = "Score: " + score
}
// the timer check function - runs every 300 milliseconds to update the car position
function updatePosition() {
  if(xDir != 0 || yDir != 0) {
    // Set the cell where the car was to empty
    // Update the column position for the car
    column += xDir
    row += yDir
    // Re-draw the car (or report a crash)
    if((!document.getElementById("R" + row.toString(16).toUpperCase() + "C" + column.toString(16).toUpperCase())) || (document.getElementById("R" + row.toString(16).toUpperCase() + "C" + column.toString(16).toUpperCase()).className == "Wall")) {
      column -= xDir
      row -= yDir
    } else {
      document.getElementById("R" + (row - yDir).toString(16).toUpperCase() + "C" + (column - xDir).toString(16).toUpperCase()).className = "Empty"
      if(document.getElementById("R" + row.toString(16).toUpperCase() + "C" + column.toString(16).toUpperCase()).className == "Apple") {
        win()
      } else if(document.getElementById("R" + row.toString(16).toUpperCase() + "C" + column.toString(16).toUpperCase()).className == "Kill") {
        handleCrash()
      } else {
        document.getElementById("R" + row.toString(16).toUpperCase() + "C" + column.toString(16).toUpperCase()).className = "PlayerClosed"
      }
    }
  }
}

function win() {
  document.getElementById("R" + row.toString(16).toUpperCase() + "C" + column.toString(16).toUpperCase()).className = "PlayerOpen"
  score += 1
  var newcoords = acoords
  while(newcoords == acoords || newcoords == "R" + row.toString(16).toUpperCase() + "C" + column.toString(16).toUpperCase()) {
    newcoords = choice(emptys)
  }
  acoords = newcoords
  document.getElementById(acoords).className = "Apple"
  document.getElementById("Message").innerText = "Score: " + score
  try {
    for(i = 0; i < 2; i++) {
      var newkillcoords = choice(walls)
      document.getElementById(newkillcoords).className = "Kill"
      walls.splice(walls.indexOf(newkillcoords), 1)
      kills.push(newkillcoords)
    }
  } catch {}
  speed -= 5
  if(speed > 150) {
    window.clearInterval(intervalHandle)
    intervalHandle = setInterval(updatePosition, speed)
  }
}
// if the car has gone off the table, this tidies up including crash message
function handleCrash() {
  window.clearInterval(intervalHandle)
  document.getElementById("Message").innerText = "You died, score: " + score
}

function randint(max) {
  return Math.floor(Math.random() * max);
}

function choice(l) {
  return l[Math.floor(Math.random() * l.length)]
}

function checkdone(array, x, y) {
  try {
    if(x < 0 || y < 0 || x > array.length - 1 || y > array[0].length - 1) return true
    var char = array[y][x]
    if(char == "f") return true
    else return false
  } catch {
    return true
  }
}

function generate(width, height) {
  var o = []
  var n = []
  for(i = 0; i < height; i++) {
    var n = []
    for(j = 0; j < 2 * width + 1; j++) {
      n.push("#")
    }
    o.push(n)
    var n = []
    for(j = 0; j < width; j++) {
      n.push("#")
      n.push(" ")
    }
    n.push("#")
    o.push(n)
  }
  var n = []
  for(i = 0; i < 2 * width + 1; i++) {
    n.push("#")
  }
  o.push(n)
  var cells = []
  for(i = 0; i < height; i++) {
    var l = []
    for(j = 0; j < width; j++) {
      l.push("e")
    }
    cells.push(l)
  }
  var lastcoords = [
    [randint(width - 1), randint(height - 1)]
  ]
  cells[lastcoords[0][1]][lastcoords[0][0]] = "f"
  var filled = 1
  while(filled < width * height) {
    var x = lastcoords[lastcoords.length - 1][0]
    var y = lastcoords[lastcoords.length - 1][1]
    cells[y][x] = "f"
    var u = checkdone(cells, x, y - 1)
    var d = checkdone(cells, x, y + 1)
    var l = checkdone(cells, x - 1, y)
    var r = checkdone(cells, x + 1, y)
    var empty = []
    if(u == false) empty.push("u")
    if(d == false) empty.push("d")
    if(l == false) empty.push("l")
    if(r == false) empty.push("r")
    if(empty.length == 0) {
      lastcoords.pop()
      continue
    } else {
      filled++
      var direction = choice(empty)
      var newx = 0
      var newy = 0
      if(direction == "u") {
        newx = x
        newy = y - 1
        o[2 * (y + 1) - 2][2 * (x + 1) - 1] = " "
      } else if(direction == "d") {
        newx = x
        newy = y + 1
        o[2 * (y + 1)][2 * (x + 1) - 1] = " "
      } else if(direction == "l") {
        newx = x - 1
        newy = y
        o[2 * (y + 1) - 1][2 * (x + 1) - 2] = " "
      } else if(direction == "r") {
        newx = x + 1
        newy = y
        o[2 * (y + 1) - 1][2 * (x + 1)] = " "
      }
      lastcoords.push([newx, newy])
    }
  }
  for(i = 0; i < o.length; i++) {
    var l = o[i]
    for(j = 0; j < l.length; j++) {
      var c = l[j]
      if(c == "#") {
        document.getElementById("R" + i.toString(16).toUpperCase() + "C" + j.toString(16).toUpperCase()).className = "Wall"
        walls.push("R" + i.toString(16).toUpperCase() + "C" + j.toString(16).toUpperCase())
      } else if(c == " ") {
        emptys.push("R" + i.toString(16).toUpperCase() + "C" + j.toString(16).toUpperCase())
      } else {
        document.getElementById("R" + i.toString(16).toUpperCase() + "C" + j.toString(16).toUpperCase()).className = "Kill"
        kills.push("R" + i.toString(16).toUpperCase() + "C" + j.toString(16).toUpperCase())
      }
    }
  }
}