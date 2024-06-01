// listen for keypress (to detect arrow keys)
document.onkeydown = checkKey
var coinscollected = 0
var coinsmax = 10

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
	} else if (e.key == "ArrowDown") {
		yDir = 1
		xDir = 0
	} else if (e.key == "ArrowUp") {
		yDir = -1
		xDir = 0
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
	if (xDir != 0 || yDir != 0)  {
		// Set the cell where the car was to empty
		getCell(row, column).className = ""
		
		// Update the column position for the car
		column += xDir
		row += yDir

		cell = getCell(row, column)
		// Re-draw the car (or report a crash)
		if (!cell || cell.className == "wall") {
			// the target cell doesn't exist, so we are outside the game area
			crash() 
		} else if (cell.className == "coin") {
			coinscollected += 1
			if (coinscollected == coinsmax) {
				handleWin()
			}
		} else {
			cell.className = "Car"
		}
	}
}

function handleWin() { 
	window.clearInterval(intervalHandle) 
	document.getElementById("Message").innerText = "Well done, you've won!"
	
} 
// if the car has		 gone off the table, this tidies up including crash message
function crash() {
	window.clearInterval(intervalHandle)
	document.getElementById("Message").innerText = "You crashed..."
	audio = document.getElementById("Death")
	audio.autoplay = true
	audio.load()
}





// when the page loaded...
$( document ).ready(function() {
    runGame();
});


