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

var firstMove = true

var Carflip = false
// the function called when a key is pressed - sets direction variable
function checkKey(e) {
	// for all keys, see https://developer.mozilla.org/en-US/docs/Web/API/UI_Events/Keyboard_event_key_values
	if (e.key == "d") {
		xDir = 1
		yDir = 0 
		Carflip = false
	} else if (e.key == "a") {
		xDir = -1
		yDir = 0
		Carflip = true
	} else if (e.key == "w") {
		xDir = 0
		yDir = -1
	} else if (e.key == "s") {
		xDir = 0
		yDir = 1
	}
	event.preventDefault()
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
	if (xDir != 0  || yDir != 0) {
		if (firstMove == true) {
			audio = document.getElementById("Bomb")
			audio.autoplay = true
			audio.load()
			firstMove = false
		}
		// Set the cell where the car was to empty
		document.getElementById("R" + row + "C" + column).className = "B"
		
		// Update the column position for the car
		column += xDir
		row += yDir
		
		// Re-draw the car (or report a crash)
		cell = document.getElementById("R" + row + "C" + column)
		if (!cell || cell.className == "Wall") {
			crash()
		} else if (cell.className == "Flag") {
			win()
			console.log("hello")
		}   else {
			if (cell.className == "Coin") {
			audio = document.getElementById("Nik")
			audio.autoplay = true
			audio.load()
}
{
			}
			if(Carflip) {
				cell.className = "Carflip"
			} else {
				cell.className = "Car"
			}
		}	
	}
}



// if the car has gone off the table, this tidies up including crash message
function crash() {
	window.clearInterval(intervalHandle)
	document.getElementById("Message").innerText = "lmao drive better..."
	audio = document.getElementById("Die")
	audio.autoplay = true
	audio.load()
}

function win() {
	window.clearInterval(intervalHandle)
	document.getElementById("Message").innerText = "Good Job."
	audio = document.getElementById("Sewey")
	audio.autoplay = true
	audio.load()

}

// when the page loaded...
$( document ).ready(function() {
    runGame();
});