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
    } else if (e.keyCode == '40') {
        // down arrow
         yDir = 1
         xDir = 0
    }
}

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
        // up
	    yDir = -1
        xDir = 0
    } else if (e.keyCode == '40') {
        // down
	    yDir = 1
        xDir = 0
    }
}

// called when the page is loaded to start the timer checks
function runGame() {
	intervalHandle = setInterval(updatePosition, 300)
}

// the timer check function - runs every 300 milliseconds to update the car position
function updatePosition() {

	if (yDir != 0 || xDir != 0) {
   
		document.getElementById("r" + row + " c" + column).className = "Empty"
        
        column += xDir
		row += yDir
        
       
		if (!document.getElementById("r" + row + " c" + column) || document.getElementById("r" + row + " c" + column).className == "Wall") { 
			handleCrash()
		} else {
			document.getElementById("r" + row + " c" + column).className = "Dog"
		}
	}   
    
}

// if the car has gone off the table, this tidies up including crash message
function handleCrash() {
	window.clearInterval(intervalHandle)
	document.getElementById("Message").innerText = "Oops you crashed..."
}


