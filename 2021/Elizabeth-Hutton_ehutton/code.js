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


function updatePosition() {
    //if you are moving LR or UD
	if (xDir != 0 || yDir != 0) {
        // Set the cell where the car was to empty
		document.getElementById("r" + row + " c" + column).className = "Empty"
        // Update the column position for the car
		column += xDir;
        row += yDir;
        
        //console.log helps a LOT!
        console.log(column, row)
        console.log(document.getElementById("r" + row + " c" + column).className)
       
		if (handleEnd() == false) {
			document.getElementById("r" + row + " c" + column).className = "Fire";

		}
	}
    
}

function handleEnd()
{
    if (!document.getElementById("r" + row + " c" + column) ||document.getElementById("r" + row + " c" + column).className == "Wall") {
        handleCrash();
        return true;
    } else if(document.getElementById("r" + row + " c" + column).className == "Volcano")
    {
       handleWin();
        return true;   
    }
    return false;
}
// if the car has gone off the table, this tidies up including crash message
function handleCrash() {
	window.clearInterval(intervalHandle)
document.getElementById("Message").innerText = "Oops the fire was put out"

}

function handleWin() {
	window.clearInterval(intervalHandle)
document.getElementById("Message").innerText = "WELL DONE YOU WIN!"
    
}