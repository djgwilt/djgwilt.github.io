// listen for keypress (to detect arrow keys)
document.onkeydown = checkKey

// to store movement direction
var xDir = 0
var yDir = 0

// to store current column position
var column = 0
var row = 0

// to store the handle code for the timer interval to cancel it when we crash
var intervalHandle

var CarFlipped = false

COINSMAX = 2

var coinsCollected = 0

// the function called when a key is pressed - sets direction variable
function checkKey(e) {
	// for all keys, see https://developer.mozilla.org/en-US/docs/Web/API/UI_Events/Keyboard_event_key_values
	if (e.key == "ArrowRight") {
		xDir = 1
		yDir = 0
		CarFlipped = true
	} else if (e.key == "ArrowLeft") {
		xDir = -1
		yDir = 0
		CarFlipped = false
	} else if (e.key == "ArrowUp") {
		xDir = 0
		yDir = -1
	} else if (e.key == "ArrowDown") {
		xDir = 0
		yDir = 1
	}
	event.preventDefault()
}

// called when the page is loaded to start the timer checks
function runGame(speed = 300) {
	intervalHandle = setInterval(updatePosition, speed)
}

function getCell(row, column) {
  return document.getElementById("R" + row + "C" + column)
}

// the timer check function - runs every 300 milliseconds to update the car position
function updatePosition() {
	if (xDir != 0 || yDir != 0) {
		// Set the cell where the car was to empty
		getCell(row, column).className = ""
		
		// Update the column position for the car
		column += xDir
		row += yDir
		
		// Re-draw the car (or report a crash)
		cell = getCell(row, column)
			// the target cell doesn't exist, so we are outside the game area
		if (!cell || cell.className == "wall"|| (cell.className == "flag" && coinsCollected != COINSMAX)) {
			handleCrash()
		} else if (cell.className == "coin") {
			coinsCollected = coinsCollected + 1
			cell.className = "Car"
		} else if (cell.className == "flag" && coinsCollected == COINSMAX) {
			handleWin();
		} else if (CarFlipped) {
			cell.className = "CarFlipped"
		} else {
			cell.className = "Car"
		}
	}
}

// if the car has gone off the table, this tidies up including crash message
function handleCrash() {
	window.clearInterval(intervalHandle)
	document.getElementById("Message").innerText = "Oops you crashed... "
}
function handleWin() {
	window.clearInterval(intervalHandle)
	document.getElementById("Message").innerText = "Well done, you've won!"
}

// when the page loaded...
$( document ).ready(function() {
    
});