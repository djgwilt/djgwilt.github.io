// listen for keypress (to detect arrow keys)
document.onkeydown = checkKey

// to store movement direction
var xDir = 0
var yDir = 0
var flagCount = 0
var flagMax = 2
// to store current column position
var column = 0
var row = 0

// to store the handle code for the timer interval to cancel it when we crash
var intervalHandle

//car class
var carClass = "Car"

// the function called when a key is pressed - sets direction variable
function checkKey(e) {
    // this next line is a workaround for older versions of IE which didn't pass the event as a parameter
    e = e || window.event

    if (e.keyCode == '39') {
        // right arrow
        yDir = 0
	    xDir = 1
        carClass = "CarFlip"
    } else if (e.keyCode == '37') {
        // left arrow
        yDir = 0
	    xDir = -1
        carClass= "Car"
    } else if (e.keyCode == '40') {
        // down arrow
        xDir = 0
	    yDir = 1
     } else if (e.keyCode == '38') {
        // up arrow
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
		document.getElementById("r" + row + " c" + column).className = "Empty"
        // Update the column position for the car
		column += xDir
        row += yDir
        // Re-draw the car (or report a crash)
		if (handleEnd() == false) {
		   document.getElementById("r" + row + " c" + column).className = carClass
		}
	
	}
}

function handleEnd()
{
    if (!document.getElementById("r" + row + " c" + column) || document.getElementById("r" + row + " c" + column).className == "wall"){
      handleCrash()
      return true
   } else if (document.getElementById("r" + row + " c" + column).className == "flag")
   {
      handleWin()
      return true
   }
   return false
}

// if the car has gone off the table, this tidies up including crash message

function handleWin() {
    flagCount++
    if (flagCount==flagMax){
	window.clearInterval(intervalHandle)
	document.getElementById("Message").innerText = "YOU REACHED THE CLUBHOUSE!"
    }
}

function handleCrash() {
	window.clearInterval(intervalHandle)
        document.getElementById("Message").innerText = "Oops...poor mickey :("
}
