// listen for keypress (to detect arrow keys)
document.onkeydown = checkKey
score = 0
// to store movement direction
var xDir = 0
var yDir = 0
// to store current column position
var column = 0
var row = 0
// to store the handle code for the timer interval to cancel it when we crash
var intervalHandle

// the function called when a key is pressed - sets direction variable
function checkKey(e) {
	// for all keys, see https://developer.mozilla.org/en-US/docs/Web/API/UI_Events/Keyboard_event_key_values
	if (e.key == "ArrowRight") {
		xDir = 1
		yDir = 0
	} else if (e.key == "ArrowLeft") {
		xDir = -1
		yDir = 0
	} else if (e.key == "ArrowUp") {
		xDir = 0
		yDir = -1
	} else if (e.key == "ArrowDown") {
		xDir = 0
		yDir = 1
	}
}

// called when the page is loaded to start the timer checks
function runGame() {
	intervalHandle = setInterval(updatePosition, 150)
}

function getCell(row, column) {
  return document.getElementById("R" + row + "C" + column)
}
function handleWin() {
	window.clearInterval(intervalHandle)
	document.getElementById("Message").innerText = "Congratulations! You've won!"
}
// the timer check function - runs every 300 milliseconds to update the car position
function updatePosition() {
	if (xDir != 0 || yDir != 0) {
		// Set the cell where the car was to empty
		getCell(row, column).className = ""
		
		// Update the column position for the car
		column += xDir
		row += yDir

		cell = getCell(row, column)
		// Re-draw the car (or report a crash)
		if (!cell || cell.className == "Wall" || cell.className == "Wall2") {
			// the target cell doesn't exist, so we are outside the game area
			crash()
		} else if (cell.className == "Trophy") {
			handleWin();
		} else if (cell.className == "Chilwell" || cell.className == "Rudiger" || cell.className == "James" || cell.className == "Havertz" || cell.className == "Kante" || cell.className == "Silva" || cell.className == "Trev" || cell.className == "Mount" || cell.className == "Mendy" || cell.className == "Timo" || cell.className == "Kova") {
			scorePoint();
		} else {
			cell.className = "Car"
		}
	}
}
function scorePoint() {
	score = score + 1
}
// if the car has gone off the table, this tidies up including crash message
function crash() {
	window.clearInterval(intervalHandle)
	document.getElementById("Message").innerText = "Oops you crashed..."
	document.getElementById("Message").innerText = "Score: ", score
}

// when the page loaded...
$( document ).ready(function() {
    runGame();
});