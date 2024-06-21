// listen for keypress (to detect arrow keys)
document.onkeydown = checkKey

// to store movement direction
var xDir = 0
// DJG Need to define the variable yDir
var yDir = 0
// to store current column position
var column = 0
var row = 0
// to store the handle code for the timer interval to cancel it when we crash
var intervalHandle

// the function called when a key is pressed - sets direction variable
function checkKey(e) {
    // this next line is a workaround for older versions of IE which didn't pass the event as a parameter
    e = e || window.event

    if (e.keyCode == '39') {
        // right arrow
	    xDir = 1
        yDir = 0
    } else if (e.keyCode == '37') {
        // left arrow
	    xDir = -1
        yDir = 0
    } else if (e.keyCode == '38') {
        // down arrow
        // DJG Y should get bigger when you go down, smaller when you go up.
	    xDir = 0
        yDir = -1
    } else if (e.keyCode == '40') {
        // up arrow
	    xDir = 0
        yDir = 1
    }
}

// called when the page is loaded to start the timer checks
function runGame() {
	intervalHandle = setInterval(updatePosition, 300)
}

// the timer check function - runs every 300 milliseconds to update the car position
function updatePosition() {
	if (xDir != 0 || yDir != 0) {
        // Set the cell where the car was to empty
		document.getElementById("r" + row + " c" + column).className = "Empty"
        // Update the column position for the car
		column += xDir
        row += yDir
        // Re-draw the car (or report a crash)
		if (handleEnd() == false) {
		    document.getElementById("r" + row + " c" + column).className = "Car"
		}
	}
}

function handleEnd(){
    if (!document.getElementById("r" + row + " c" + column) || document.getElementById("r" + row + " c" + column).className == "plant1") {
        handleCrash()
        return true; 
    }else if (document.getElementById("r" + row + " c" + column).className == "brainzombie"){
        handleWin()
        return true;
    }
    return false;
}

// if the car has gone off the table, this tidies up including crash message
function handleCrash() {
	window.clearInterval(intervalHandle)
	document.getElementById("Message").innerText = "Oops you crashed..."
}

function handleWin() {
	 window.clearInterval(intervalHandle)
	document.getElementById("Message").innerText = "The Walrus has reached the Brain! YOU WIN"
}