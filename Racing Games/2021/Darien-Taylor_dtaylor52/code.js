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
var dragonClass = "dragon"
var flagClass = "flag"

// the function called when a key is pressed - sets direction variable
function checkKey(e) {
  
    // this next line is a workaround for older versions of IE which didn't pass the event as a parameter
    e = e || window.event

    if (e.keyCode == '39') {
        // right arrow
	    xDir = 1
      yDir = 0
      dragonClass = "dragon"
    } else if (e.keyCode == '37') {
        // left arrow
	    xDir = -1
      yDir = 0
      dragonClass = "flipped"
    } else if (e.keyCode == '40'){
        //up
      yDir = 1
      xDir = 0
    }if (e.keyCode == '38') {
        //down
	    xDir = 0
      yDir = -1
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
		document.getElementById("R" + row + "C" + column).className = "Empty"
        // Update the column position for the car
		column += xDir
    row += yDir
        // Re-draw the car (or report a crash)
		if (!document.getElementById("R" + row + "C" + column)) {
			handleCrash()
		} else {
			document.getElementById("R" + row + "C" + column).className = dragonClass
        console.log(dragonClass);
    }
	}
}

// if the car has gone off the table, this tidies up including crash message
function handleCrash() {
	window.clearInterval(intervalHandle)
	document.getElementById("Message").innerText = "Oops you crashed..."
}
