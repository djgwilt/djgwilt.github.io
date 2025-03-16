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

// to remeber car class (pacman or pacman2)
var carClass = "pacman"


// the function called when a key is pressed - sets direction variable
function checkKey(e) {
    // this next line is a workaround for older versions of IE which didn't pass the event as a parameter
    e = e || window.event

    if (e.keyCode == '39') {
        // right arrow
	    xDir = 1
        yDir = 0
        carClass = "pacman"
    } else if (e.keyCode == '37') {
        // left arrow
	    xDir = -1
        yDir = 0
        carClass = "pacmanflip"
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
	if (xDir != 0) {
        // Set the cell where the car was to empty
		document.getElementById("r" + row + " c" + column).className = "Empty"
        // Update the column position for the car
		column += xDir
 
        // Re-draw the car (or report a crash)
        // ! means not in JS. Next line means if the cell when you will move to does not exist.. you've gone off the map
            if (handleEnd() == false) { 
			document.getElementById("r" + row + " c" + column).className = carClass
		}
	}
    
    // ***********new code here
	if (yDir != 0) {
        // Set the cell where the car was to empty
		document.getElementById("r" + row + " c" + column).className = "Empty"
        
        // Update the column position for the car
		row += yDir
        
        // Re-draw the car (or report a crash)
        // ! means not in JS. Next line means if the cell when you will move to does not exist.. you've gone off the map        
		 if (handleEnd() == false) { 
			document.getElementById("r" + row + " c" + column).className = "pacman"
		}
	}    // ********************
    
}

function handleEnd()
{
    if (!document.getElementById("r" + row + " c" + column) || document.getElementById("r" + row + " c" + column).className == "wall") {
       handleCrash();
       return true;
    } else if( document.getElementById("r" + row + " c" + column).className == "portal")
    {
        handleWin();
        return true;
          
          
    }
    return false;
        
        
        
}

// if the car has gone off the table, this tidies up including crash message
function handleCrash() {
	window.clearInterval(intervalHandle)
	document.getElementById("Message").innerText = "RESTART"
}

function handleWin() {
	window.clearInterval(intervalHandle)
	document.getElementById("Message").innerText = "NEXT LVL"
}

