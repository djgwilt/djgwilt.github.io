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

// the function called when a key is pressed - sets direction variable
function checkKey(e) {
	// for all keys, see https://developer.mozilla.org/en-US/docs/Web/API/UI_Events/Keyboard_event_key_val

	if (e.key == "d") {
		xDir = 1
		yDir = 0
		carLeft = false
		carDown = false
		carUp = false
	} else if (e.key == "a") {
		xDir = -1
		yDir = 0
		carLeft = true
		carDown = false
		carUp = false
	} else if (e.key == "w") {
		xDir = 0
		yDir = -1
		carLeft = false
		carDown = false
		carUp = true
	} else if (e.key == "s") {
		xDir = 0
		yDir = 1
		carLeft = false
		carDown = true
		carUp = false
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
	console.log(row, column, xDir, yDir)
	if (xDir != 0 || yDir != 0) {
		// Set the cell where the car was to empty
		getCell(row, column).className = ""
		
		// Update the column position for the car
		column += xDir
		row += yDir

		cell = getCell(row, column)

		if (!cell || cell.className == "wall") {
			crash()
		} else if (cell.className == 'winning_flag') {
			handlewin()
		} else {
			if (carLeft) {
                cell.className = "CarLeft"
            } else if (carDown) {
                cell.className = "CarDown"
            } else if (carUp) {
                cell.className = "CarUp"
            } else {
                cell.className = "Car"
		}
		}
	}
}

// if the car has gone off the table, this tidies up including crash message
function crash() {
	window.clearInterval(intervalHandle)
	document.getElementById("Message").innerText = "LMAO, get better at the game!"
	audio = document.getElementById("CrashSound")
	audio.autoplay = True
	audio.load()

}

function handlewin() {
	window.clearInterval(intervalHandle)
	document.getElementById("Message").innerText = "CONGRATS you won..."
}
// when the page loaded...
$( document ).ready(function() {
    runGame();
});