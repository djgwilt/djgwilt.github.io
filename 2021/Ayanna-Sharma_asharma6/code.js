// listen for keypress (to detect arrow keys)
document.onkeydown = checkKey

// to store movement direction
var xDir = 0

// to store current column position
var column = 0

// to store the handle code for the timer interval to cancel it when we crash
var intervalHandle

// the function called when a key is pressed - sets direction variable
function checkKey(e) {
    // this next line is a workaround for older versions of IE which didn't pass the event as a parameter
    e = e || window.event

    if (e.keyCode == '39') {
        // right arrow
	    xDir = 1
    } else if (e.keyCode == '37') {
        // left arrow
	    xDir = -1
    }
}

// called when the page is loaded to start the timer checks
function runGame() {
	intervalHandle = setInterval(updatePosition, 300)
}

// the timer check function - runs every 300 milliseconds to update the Sprite position
function updatePosition() {
	if (xDir != 0) {
        // Set the cell where the Sprite was to empty
		document.getElementById("r0 c" + column).className = "Empty"
        // Update the column position for the Sprite
		column += xDir
        // Re-draw the Sprite (or report a crash)
		if (!document.getElementById("r0 c" + column)) {
			handleCrash()
		} else {
			document.getElementById("r0 c" + column).className = "Sprite"
		}
	}
}

// if the Sprite has gone off the table, this tidies up including crash message
function handleCrash() {
	window.clearInterval(intervalHandle)
	document.getElementById("Message").innerText = "Oops you crashed..."
}
