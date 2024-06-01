// listen for keypress (to detect arrow keys)
document.onkeydown = checkKey

// to store movement direction
var xDir = 0
var yDir = 0
// to store current column position
var row = 0
var column = 0
var carClass = "CarU"
// to store the handle code for the timer interval to cancel it when we crash
var intervalHandle
var score = 0 
var speed = 0

// the function called when a key is pressed - sets direction variable
function checkKey(e) {
    // for all keys, see https://developer.mozilla.org/en-US/docs/Web/API/UI_Events/Keyboard_event_key_values
    if (e.key == "d") {
        xDir = 1
        yDir = 0
        carClass = "CarR"
    } else if (e.key == "a") {
        xDir = -1
        yDir = 0
        carClass = "CarL"
    } else if (e.key == "w") {
        yDir = -1
        xDir = 0
        carClass = "CarU"
    }else if (e.key == "s") {
        yDir = 1
        xDir = 0
        carClass = "CarD"
    }

}

// called when the page is loaded to start the timer checks
function runGame() {
    intervalHandle = setInterval(updatePosition, 300)
}

function getCell(row, column) {
  return document.getElementById("R" + row + "C" + column)
}

// the timer check function - runs every 300 milliseconds to update the car position
function updatePosition() {
    if (xDir != 0 || yDir != 0) {
        getCell(row, column).className = ""
        column += xDir
        row += yDir
        if (!getCell(row,column) || getCell(row,column).className == "wall"){
            // the target cell doesn't exist, so we are outside the game area
            crash()
        
        } else if (getCell(row, column).className == "flag") {
            if (score == 10){
                win()
            }
            else{
                crash()
            }
        }else if (getCell(row, column).className == "coin") {
            UpdateScore()
            getCell(row, column).className = carClass
        }
         else {
            getCell(row, column).className = carClass
        }

    } 

}
// if the car has gone off the table, this tidies up including crash message
function crash() {
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Oops you crashed..."
}

function UpdateScore() {
    score += 1
    document.getElementById("score").innerText = score
}

function win() {
    
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "You have reached your destination WELL DONE!"
}

// when the page loaded...
$( document ).ready(function() {
    runGame();
});

