// listen for keypress (to detect arrow keys)
document.onkeydown = checkKey
var Key = false 
var door = false
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
        console.log("right")
    } else if (e.keyCode == '37') {
        // left arrow
        console.log("left")
	    xDir = -1
        yDir = 0
    } else if (e.keyCode == '38') {
        // up arrow
        console.log("up")
	    yDir = -1
        xDir = 0
    } else if (e.keyCode == '40') {
        // down arrow
        console.log("down")
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
	if (xDir != 0 || yDir != 0) {
        // Set the cell where the car was to empty
		document.getElementById("r" + row + " c" + column).className = "Empty"
        // Update the column position for the car
		column += xDir
        row += yDir
        // Key
        if (document.getElementById("r" + row + " c" + column).className == "Key") {
           Key = true  
        }
        // Door
        if (document.getElementById("r" + row + " c" + column).className == "Door" && Key == true){
            document.getElementById("r" + row + " c" + column).className = "Man"
            door = true
        } else if (document.getElementById("r" + row + " c" + column).className == "Door" &&) {
            handleCrash()
        }
        // Re-draw the car (or report a crash)
		if (handleEnd() == false) {
			document.getElementById("r" + row + " c" + column).className = "Man"
		}
	}

}

function handleEnd()
{
    if (!document.getElementById("r" + row + " c" + column) || document.getElementById("r" + row + " c" + column).className == "wall") {
			handleCrash();
            return true;
    } else if (document.getElementById("r" + row + " c" + column).className == "flag")
    {
            handleWin();
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
	document.getElementById("Message").innerText = "Well done! You win!"
}
