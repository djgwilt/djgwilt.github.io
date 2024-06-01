// listen for keypress (to detect arrow keys)
document.onkeydown = checkKey

// to store movement direction
var xDir = 0
var yDir = 0
// to store current column position
var row = 0
var column = 1
var score = 0
// to store the handle code for the timer interval to cancel it when we crash
var intervalHandle
var score = 0 
var pac = true

var frameCount = 0
// the function called when a key is pressed - sets direction variable
function checkKey(e) {
	// for all keys, see https://developer.mozilla.org/en-US/docs/Web/API/UI_Events/Keyboard_event_key_values
	if (e.key == "ArrowRight") {
		xDir = 1
		yDir = 0
		pac = true
	} else if (e.key == "ArrowLeft") {
		xDir = -1
		yDir = 0
		pac = false
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
	audio1.pause();
	audio4 = document.getElementById("win")
	audio4.autoplay =  true
	audio4.load()
}
// called when the page is loaded to start the timer checks
function runGame() {
	intervalHandle = setInterval(updatePosition, 300)
	audio1 = document.getElementById("music3")
	audio1.autoplay =  true
	audio1.load()
	audio1.volume = 0.5
}

function getCell(row, column) {
  return document.getElementById("R" + row + "C" + column)
}

// the timer check function - runs every 300 milliseconds to update the car position
function updatePosition() {
	frameCount++
	if (frameCount % 2 == 0) {
		ghostupdatePosition ()
		ghostupdatePosition2 ()
	}
	if (yDir != 0 || xDir != 0) {
		
		// Set the cell where the car was to empty
		getCell(row, column).className = ""
		
		// Update the column position for the car
		row += yDir
		column += xDir
		// Re-draw the car (or report a crash)
		let cell = getCell(row,column)
		if (!cell|| cell.className == "ghost" || cell.className == "ghost2"||cell.className == "Wall"|| cell.className == "Wally"|| cell.className == "Wally2"){
			// the target cell doesn't exist, so we are outside the game area
			crash()
		} else if (cell.className == "Coin"){
			score += 1
			document.getElementById("Score").innerText = score
			cell.className = "pac"
			audio2 = document.getElementById("coin")
			audio2.autoplay =  true
			audio2.load()
		}else if (cell.className == "flag") {
			score += 5
			document.getElementById("Score").innerText = score
			cell.className = "pac"
			audio2 = document.getElementById("coin")
			audio2.autoplay =  true
			audio2.load()
		} else if (score == 18) {
			win()
			document.getElementById("Four").innerText = "level 5"
		}else {
			if (pac){
				cell.className = "pac"
			} else {
				cell.className = "pac2"
			}
		}
		
	}
}

// if the car has gone off the table, this tidies up including crash message
function crash() {
	window.clearInterval(intervalHandle)
	document.getElementById("Message").innerText = "Game Over!"
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
//var num = 2
var num = 0
var grow = 2
var gcolumn = 4
function ghostupdatePosition (){
	let cellg  = getCell(grow, gcolumn)
	cellg.className = ""
	igrow = grow
	igcolumn = gcolumn
	/*if (num == 1) {
		grow --
	} else if (num == 2){
		gcolumn --
	} else if (num == 3){
		gcolumn += 1
	} else {
		grow += 1
	}*/
	if ((column - gcolumn) < 0) {
		gcolumn --
	} else if ((column - gcolumn) > 0){
		gcolumn += 1
	} else if ((row - grow) > 0){
		grow += 1
	} else if ((row - grow) < 0){
		grow --
	}

	cellg  = getCell(grow, gcolumn)
	//num = Math.floor(Math.random() * 4)
	if (cellg && cellg.className != "Wall" && cellg.className != "Wally" && cellg.className != "Wally2"&& cellg.className != "Coin" && cellg.className != "flag" && cellg.className != "ghost2") {
		cellg.className = "ghost"
	} else {
		grow = igrow
		gcolumn = igcolumn
		cellg = getCell(grow, gcolumn)
		cellg.className = "ghost"
	}
	
}

//var num2 = 2
var num2 = 0
var grow2 = 4
var gcolumn2 = 8
function ghostupdatePosition2 (){
	let cellg2  = getCell(grow2, gcolumn2)
	cellg2.className = ""
	igrow2 = grow2
	igcolumn2 = gcolumn2
	/*if (num2 == 1) {
		grow2 --
	} else if (num2 == 2){
		gcolumn2 --
	} else if (num2 == 3){
		gcolumn2 += 1
	} else {
		grow2 += 1
	}*/
	if ((column - gcolumn2) < 0) {
		gcolumn2 --
	} else if ((column - gcolumn2) > 0){
		gcolumn2 += 1
	} else if ((row - grow2) > 0){
		grow2 += 1
	} else if ((row - grow2) < 0){
		grow2 --
	}
	cellg2  = getCell(grow2, gcolumn2)
	//num2 = Math.floor(Math.random() * 4)
	if (cellg2 && cellg2.className != "Wall" && cellg2.className != "Wally" && cellg2.className != "Wally2"&& cellg2.className != "Coin" && cellg2.className != "flag"  && cellg2.className != "ghost") {
		cellg2.className = "ghost2"
	} else {
		grow2 = igrow2
		gcolumn2 = igcolumn2
		cellg2 = getCell(grow2, gcolumn2)
		cellg2.className = "ghost2"
	}
	
}
