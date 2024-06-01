// listen for keypress (to detect arrow keys)
document.onkeydown = checkKey

// to store movement direction
var xDir = 0
var yDir = 0

// moving obstacle


// to store current column position
var row = 0
var column = 1
var score = 0
// to store the handle code for the timer interval to cancel it when we crash
var intervalHandle
var score = 0 
// the function called when a key is pressed - sets direction variable
function checkKey(e) {
	// for all keys, see https://developer.mozilla.org/en-US/docs/Web/API/UI_Events/Keyboard_event_key_values
	if (e.key == "ArrowDown") {
		yDir = 1
		
	}else if (e.key == "ArrowUp") {
		yDir = -1
		
	}

}

function win() {
	window.clearInterval(intervalHandle)
	document.getElementById("Message").innerText = "Well done you won"
}
// called when the page is loaded to start the timer checks
function runGame() {
	intervalHandle = setInterval(updatePosition, 200)
	audio1 = document.getElementById("music2")
	audio1.autoplay =  true
	audio1.load()
	
}

function getCell(row, column) {
  return document.getElementById("R" + row + "C" + column)
}

// the timer check function - runs every 300 milliseconds to update the car position
function updatePosition() {
	obsupdatePosition();
	if (yDir != 0) {
		// Set the cell where the car was to empty
		getCell(row, column).className = ""
		
		// Update the column position for the car
		row += yDir
		
		// Re-draw the car (or report a crash)	
	}

	let cell = getCell(row,column)
	if (!cell || cell.className == "Enem"){
		crash()
	} 
		else {
		cell.className = "Car"
	}
	if (score == 5){
		document.getElementById("Four").innerText = "level 3"
	}
	
}



// if the car has gone off the table, this tidies up including crash message
function crash() {
	window.clearInterval(intervalHandle)
	document.getElementById("Message").innerText = "Oops you crashed..."
	audio = document.getElementById("crasho")
	audio.autoplay = true
	audio.load()
	score = 0
	audio1.pause()
}

var obrow = 0
var obcolumn = 7
function obsupdatePosition() {
	
	// Set the cell where the car was to empty
	getCell(obrow, obcolumn).className = ""
	
	// Update the column position for the car
	obcolumn--
	if (obcolumn < 0) {
		obrow = Math.floor(Math.random() * 4);
		obcolumn = 7
		score += 1
		document.getElementById("Score").innerText = score
	}
	
	// Re-draw the car (or report a crash)
	let cell1 = getCell(obrow,obcolumn)
	/*if (cell1.className == "Car"){
		
		crash()
	}else{
		cell1.className = "Coin"
	}*/

	cell1.className = "Enem"
}
function start () {
// when the page loaded...
	$( document ).ready(function() {
		runGame()});
}