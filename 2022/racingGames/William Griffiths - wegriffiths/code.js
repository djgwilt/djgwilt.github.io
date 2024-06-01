// listen for keypress (to detect arrow keys)
document.onkeydown = checkKey

// to store movement direction
var xDir = 0

// to store current column position
var column = 0

// to store the handle code for the timer interval to cancel it when we crash
var intervalHandle

// the function called when a key is pressed - sets direction variable
function checkKey(e) {
	// for all keys, see https://developer.mozilla.org/en-US/docs/Web/API/UI_Events/Keyboard_event_key_values
	if (e.key == "ArrowRight") {
		xDir = 1
	} else if (e.key == "ArrowLeft") {
		xDir = -1
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
	if (xDir != 0) {
		// Set the cell where the car was to empty
		getCell(0, column).className = ""
		
		// Update the column position for the car
		column += xDir
		
		// Re-draw the car (or report a crash)
		if (!getCell(0, column)) {
			// the target cell doesn't exist, so we are outside the game area
			crash()
		} else {
			getCell(0, column).className = "Car"
		}
	}
}

// if the car has gone off the table, this tidies up including crash message
function crash() {
	window.clearInterval(intervalHandle)
	document.getElementById("Message").innerText = "Oops you crashed..."
}

// when the page loaded...
$( document ).ready(function() {
    runGame();
});