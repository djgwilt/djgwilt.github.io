// listen for keypress (to detect arrow keys)
document.onkeydown = checkKey

// to store movement direction
var xDir = 0

// to store current column position
var column = 5
var row = 11
var tick = 150


var obrows = [0,0,0,0,0]
var ocolumns = [7,4, 5, 6, 3]
var speeds = [240, 230, 220, 240, 240]
score = 0;
game = true
// to store the handle code for the timer interval to cancel it when we crash
var intervalHandle
var intervalHandle2
var intervalHandle3
var intervalHandle4
var intervalHandle5



// the function called when a key is pressed - sets direction variable
function checkKey(e) {
	// for all keys, see https://developer.mozilla.org/en-US/docs/Web/API/UI_Events/Keyboard_event_key_values
	if (e.key == "ArrowRight") {
		xDir = 1
	} else if (e.key == "ArrowLeft") {
		xDir = -1
	}
}

// called when the page is loaded to start the timer checks
function runGame(ctick) {
	intervalHandle = setInterval(updatePosition, ctick)
	
	intervalHandle2 = setInterval(() => obsupdatePosition(0), speeds[0])
	intervalHandle3 = setInterval(() => obsupdatePosition(1), speeds[1])
	intervalHandle4 = setInterval(() => obsupdatePosition(2), speeds[2])
	intervalHandle5 = setInterval(() => obsupdatePosition(3), speeds[3])
	intervalHandle6 = setInterval(() => obsupdatePosition(4), speeds[4])
	
	
	
}

function getCell(row, column) {
  return document.getElementById("R" + row + "C" + column)
}

// the timer check function - runs every 300 milliseconds to update the car position
function updatePosition() {
	if (xDir != 0) {
		// Set the cell where the car was to empty
		getCell(row, column).className = ""
		
		// Update the column position for the car
		column += xDir
		// Re-draw the car (or report a crash)
		
	}
	let cell = getCell(row, column)
	if (!cell || cell.className == "obstacle") {
		// the target cell doesn't exist, so we are outside the game area
		crash();

	} else {
		cell.className = "Car"
	}
}

// if the car has gone off the table, this tidies up including crash message
function crash() {
	window.clearInterval(intervalHandle)
	window.clearInterval(intervalHandle2)
	window.clearInterval(intervalHandle3)
	window.clearInterval(intervalHandle4)
	window.clearInterval(intervalHandle5)
	window.clearInterval(intervalHandle6)
	// document.getElementById("Message").innerText = "Oops, a boulder hit you."
	game = false
}

function obsupdatePosition(i) {
    // Set the cell where the car was to empty
    getCell(obrows[i], ocolumns[i]).className = ""
    
    // Update the column position for the car
    obrows[i] += 1
    if (obrows[i] > 11) {
        ocolumns[i] = Math.floor(Math.random() * 10);
        obrows[i] = 0;
        score += 1;
        document.getElementById("Score").innerText = "Score: "+score
    }
    
    // Re-draw the car (or report a crash)
    let cell1 = getCell(obrows[i],ocolumns[i]);
    cell1.className = "obstacle"
}


// when the page loaded...
$( document ).ready(function() {
	

	
    runGame(150);
});