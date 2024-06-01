// listen for keypress (to detect arrow keys)
document.onkeydown = checkKey

// to store movement direction
var xDir = 0
var yDir = 0

// moving obstacle


// to store current column position
var row = 3
var column = 1
var score = 0
var numb = 200
var show = 0
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
	e.preventDefault()

}
function easy() {
	numb = 250;
	document.getElementById("speed").innerText = numb
}
function medium() {
	numb = 200;
	document.getElementById("speed").innerText = numb
}
function hard() {
	numb = 150;
	document.getElementById("speed").innerText = numb
}

function win() {
	window.clearInterval(intervalHandle)
	document.getElementById("Message").innerText = "Well done you won"
}

// called when the page is loaded to start the timer checks
function runGame() {
	if (numb == 150) {
		intervalHandle = setInterval(updatePosition, 150);
		
	} else if (numb == 200){
		intervalHandle = setInterval(updatePosition, 200);
		
	} else if (numb == 250) {
		intervalHandle = setInterval(updatePosition, 250);
		
	}
	for (let i = 0; i < 15; i++) {
		audio1 = document.getElementById("music")
		audio1.autoplay = true
		audio1.load()
		audio1.volume = 0.7;
		audio1.playbackRate = 1.5;
	}
	
	
	
	// audio.play()
	
	
}

function getCell(row, column) {
  return document.getElementById("R" + row + "C" + column)
}

// the timer check function - runs every 300 milliseconds to update the car position
function updatePosition() {
	
	obsupdatePosition();
	show = 0
	if (yDir != 0) {
		// Set the cell where the car was to empty
		getCell(row, column).className = ""
		
		// Update the column position for the car
		row += yDir
		yDir = 0
		// Re-draw the car (or report a crash)	
	}

	let cell = getCell(row,column)
	if (!cell || cell.className == "Wall2"){
		crash()
		
		cell.className = "Wall2"
	}else if (cell.className == "Enem"){
		crash()
		cell.className = "Enem"
		
	} else if (cell.className == "Coin"){
		score += 1
		audio3 = document.getElementById("coin")
		audio3.autoplay = true
		audio3.load()
		show = 1
		
		cell.className = "Car"
	} 
	
		else {
		cell.className = "Car"
	}
	if (score == 7) {
		document.getElementById("Five").innerText = "level 4"
	}
	
}



// if the car has gone off the table, this tidies up including crash message
function crash() {
	window.clearInterval(intervalHandle)
	document.getElementById("Message").innerText = "Game over!"
	document.getElementById("Final").innerText ="You got " + score
	score = 0
	audio = document.getElementById("crasho")
	audio.autoplay = true
	audio.load()
	audio1.pause()
	
	
}

var obrow = 3
var obcolumn = 7
var a = 0
var b = 0
var c = 0
var w = Math.floor(Math.random() * 2)
function obsupdatePosition() {
	
	a = Math.floor(Math.random() * 4)
	b = Math.floor(Math.random() * 6)
	c = Math.floor(Math.random() * 9)
	// Set the cell where the car was to empty
	getCell(a,3).className = "cloud"
	getCell(b,2).className = "cloud"
	getCell(c,1).className = "cloud"
	getCell(b,5).className = "cloud"
	getCell(a,6).className = "cloud"
	getCell(0, obcolumn).className = ""
	getCell(1, obcolumn).className = ""
	getCell(2, obcolumn).className = ""
	getCell(3, obcolumn).className = ""
	getCell(4, obcolumn).className = ""
	getCell(5, obcolumn).className = ""
	getCell(6, obcolumn).className = ""
	getCell(7, obcolumn).className = ""
	getCell(8, obcolumn).className = ""
	
	
	// Update the column position for the car
	obcolumn--
	if (obcolumn < 0) {
		obrow = Math.floor(Math.random() * 7) + 1;
		obcolumn = 7
		w = Math.floor(Math.random() * 2)
		document.getElementById("Score").innerText = score
		
		
	}
	
	// Re-draw the car (or report a crash)
	let cell1 = getCell(obrow,obcolumn)
	/*if (cell1.className == "Car"){
		
		crash()
	}else{
		cell1.className = "Coin"
	}*/
	getCell(0, obcolumn).className = "Wall2"
	getCell(1, obcolumn).className = "Wall2"
	getCell(2, obcolumn).className = "Wall2"
	getCell(3, obcolumn).className = "Wall2"
	getCell(4, obcolumn).className = "Wall2"
	getCell(5, obcolumn).className = "Wall2"
	getCell(6, obcolumn).className = "Wall2"
	getCell(7, obcolumn).className = "Wall2"
	getCell(8, obcolumn).className = "Wall2"
	getCell(obrow -1,obcolumn).className = ""
	if (w == 1){
		if (show == 0){
			cell1.className = "Coin"
		} else{
			cell1.className = ""
		}
	} else{
		cell1.className = "Enem"
	}
	
}

function start() {
	// when the page loaded...
	$( document ).ready(function() {
		runGame()
		
	});
}
