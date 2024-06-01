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

var carLeft = false
var carDown = false
var carUp = false
var sight_cell_list = []

// the function called when a key is pressed - sets direction variable
function checkKey(e) {
	// for all keys, see https://developer.mozilla.org/en-US/docs/Web/API/UI_Events/Keyboard_event_key_values
	if (e.key == "ArrowRight" || e.key == 'd') {
		xDir = 1
		yDir = 0
		carDown = false
		carLeft = false
		carUp = false
	} else if (e.key == "ArrowLeft" || e.key == 'a') {
		xDir = -1
		yDir = 0
		carDown = false
		carLeft = true
		carUp = false
	} else if (e.key == "ArrowUp" || e.key == 'w') {
		xDir = 0
		yDir = -1
		carDown = false
		carLeft = false
		carUp = true
	} else if (e.key == "ArrowDown" || e.key == 's') {
		xDir = 0
		yDir = 1
		carDown = true
		carLeft = false
		carUp = false
	}
	e.preventDefault()
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
		// Set the cell where the car was to empty
		getCell(row, column).className = ""
		// Update the column position for the car
		column += xDir
		row += yDir
		cell = getCell(row,column)
		// Re-draw the car (or report a crash)
		if (!cell || cell.className == "wall") {
			// the target cell doesn't exist, so we are outside the game area
			crash()
		} else if (cell.className == "door") {
			win()
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
	sight()
}

// if the car has gone off the table, this tidies up including crash message
function crash() {
	window.clearInterval(intervalHandle)
	document.getElementById("Message").innerText = "Oops you crashed..."
}

function win() {
	window.clearInterval(intervalHandle)
	document.getElementById("Message").innerText = "Well done!"
}

function sight() {
	row_count = row
	column_count = column
	$(".CarSight").removeClass("CarSight")
	while (row_count < 7) {
		row_count += 1
		sight_cell = getCell(row_count, column)
		if (sight_cell.className) {
			break
		} else {
			sight_cell.className = "CarSight"
		}
	}
	row_count = row
	while (row_count > 0) {
		row_count -= 1
		sight_cell = getCell(row_count, column)
		if (sight_cell.className) {
			break
		} else {
			sight_cell.className = "CarSight"
		}
	}
	while (column_count < 8) {
		column_count += 1
		sight_cell = getCell(row, column_count)
		if (sight_cell.className) {
			break
		} else {
			sight_cell.className = "CarSight"
		}
	}
	column_count = column
	while (column_count > 0) {
		column_count -= 1
		sight_cell = getCell(row, column_count)
		if (sight_cell.className) {
			break
		} else {
			sight_cell.className = "CarSight"
		}
	}
}
// when the page loaded...
$( document ).ready(function() {
    runGame();
});