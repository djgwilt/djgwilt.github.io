// listen for keypress (to detect arrow keys)
document.onkeydown = checkKey

// to store movement direction
var xDir = 0
var yDir = 0

// to store current column position
var column = 0
var row = 0
var score = 0

// to store the handle code for the timer interval to cancel it when we crash
var intervalHandle

//to store the orientation of the car
var carClass = "Car"

// the function called when a key is pressed - sets direction variable
function checkKey(e) {
	// for all keys, see https://developer.mozilla.org/en-US/docs/Web/API/UI_Events/Keyboard_event_key_values
	if (e.key == "ArrowRight") {
		xDir = 1
		yDir = 0
		carClass ="Car"
	} else if (e.key == "ArrowLeft") {
		xDir = -1
		yDir = 0
		carClass = "Car"
	} else if (e.key == "ArrowUp") {
		yDir = -1
		xDir = 0
		carClass = "ReverseCar"
	} else if (e.key == "ArrowDown") {
		yDir = 1
		xDir = 0
		carClass = "ReverseCar"
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
		//set cell where the car was to empty
		getCell(row, column).className = ""

		//update the column position for the car
		column += xDir
		row += yDir

		//re-draw the car or report a crash
		//there is no cell or we hit wall
		if (!getCell(row, column) || getCell(row, column).className == "wall") {
			crash()
		} else if (getCell(row, column).className == "goal") {
			win()
		}
		else if (getCell(row, column).className == "coin") {
			increaseScore()
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
	document.getElementById("Message").innerText = "you crashed lol"
}

function win() {
	window.clearInterval(intervalHandle)
	document.getElementById("Message").innerText = "you win at life congrats"
}

function increaseScore() {
	score += 1
	document.getElementById("score").innerText = score
}

// when the page loaded...
$( document ).ready(function() {
    runGame();
});