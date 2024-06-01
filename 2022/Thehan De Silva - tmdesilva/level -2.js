// listen for keypress (to detect arrow keys)
document.onkeydown = checkKey

// to store movement direction
var xDir = 0
var yDir = 0
// to store current column position
var row = 0
var column = 0
var score = 0
// to store the handle code for the timer interval to cancel it when we crash
var intervalHandle
var score = 0 
var car = true
// the function called when a key is pressed - sets direction variable
function checkKey(e) {
	// for all keys, see https://developer.mozilla.org/en-US/docs/Web/API/UI_Events/Keyboard_event_key_values
	if (e.key == "ArrowRight") {
		xDir = 1
		yDir = 0
		car = true
	} else if (e.key == "ArrowLeft") {
		xDir = -1
		yDir = 0
		car = false
	} else if (e.key == "ArrowDown") {
		yDir = 1
		xDir = 0
		
	}else if (e.key == "ArrowUp") {
		yDir = -1
		xDir = 0
		
	}
	e.preventDefault()

}

function win() {
	window.clearInterval(intervalHandle)
	document.getElementById("Message").innerText = "Well done, you won!"
	document.getElementById("Four").innerText = "Level -1"
	audio1.pause();
	audio4 = document.getElementById("win")
	audio4.autoplay =  true
	audio4.load()
}
// called when the page is loaded to start the timer checks
function runGame() {
	intervalHandle = setInterval(updatePosition, 200)
	
}

function getCell(row, column) {
  return document.getElementById("R" + row + "C" + column)
}

// the timer check function - runs every 300 milliseconds to update the car position
function updatePosition() {
	if (yDir != 0 || xDir != 0) {
		// Set the cell where the car was to empty
		getCell(row, column).className = ""
		
		// Update the column position for the car
		row += yDir
		column += xDir
		// Re-draw the car (or report a crash)
		let cell = getCell(row,column)
		if (!cell || cell.className == "Wall"){
			// the target cell doesn't exist, so we are outside the game area
			crash()
		} else if (cell.className == "Coin"){
			score += 1
			document.getElementById("Score").innerText = score
			cell.className = "Car"
			audio2 = document.getElementById("coin")
			audio2.autoplay =  true
			audio2.load()
		}else if (cell.className == "flag") {
			win();
		} else {
			if (car){
				cell.className = "Car"
			} else {
				cell.className = "Car2"
			}
		}
	
	}
}

// if the car has gone off the table, this tidies up including crash message
function crash() {
	window.clearInterval(intervalHandle)
	document.getElementById("Message").innerText = "Game Over!"
	//document.getElementById("Five").innerText = "Level -2"
	audio1.pause();
	audio3 = document.getElementById("crasho")
	audio3.autoplay =  true
	audio3.load()
	
}
function start (){
	row = 0
	column = 0
	// when the page loaded...
	$( document ).ready(function() {
		runGame();
	});
}