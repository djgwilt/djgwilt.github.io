// listen for keypress (to detect arrow keys)
document.onkeydown = checkKey

// to store movement direction
var xDir = 0
var yDir = 0
var flagCount = 0
var flagMax = 12
// to store current column position
var column = 0
var row = 0

// to store the handle code for the timer interval to cancel it when we crash
var intervalHandle

var carClass = "Dog"
var emptyClass = "Empty"
// the function called when a key is pressed - sets direction variable
function checkKey(e) {
    // this next line is a workaround for older versions of IE which didn't pass the event as a parameter
    e = e || window.event

    if (e.keyCode == '39') {
        // right arrow
	    xDir = 1
        yDir = 0
        carClass = "Dog"
        emptyClass = "Empty"
    } else if (e.keyCode == '37') {
        // left arrow
	    xDir = -1
        yDir = 0
        carClass = "Dog2"
        emptyClass = "Empty2"        
    } else if (e.keyCode == '38') {
        // up
	    yDir = -1
        xDir = 0
        emptyClass = "Empty3"

    } else if (e.keyCode == '40') {
        // down
	    yDir = 1
        xDir = 0
        emptyClass = "Empty4"
    }
}

// called when the page is loaded to start the timer checks
function runGame() {
	intervalHandle = setInterval(updatePosition, 300)
}

// the timer check function - runs every 300 milliseconds to update the car position
function updatePosition() {

	if (yDir != 0 || xDir != 0) {
   
		document.getElementById("r" + row + " c" + column).className = emptyClass
        
        column += xDir;
		row += yDir;
        
        //console.log("r" + row + " c" + column, document.getElementById("r" + row + " c" + column).className)
        
        if ( handleEnd() == false ) {
            document.getElementById("r" + row + " c" + column).className = carClass  
        }
    }
}
function handleEnd()
{
	if (!document.getElementById("r" + row + " c" + column) || document.getElementById("r" + row + " c" + column).className == "Wall") {  
     
        handleCrash()
        return true;
      } else if (document.getElementById("r" + row + " c" + column).className == "Flag") {
        handleWin();
        return true;
      } else if (document.getElementById("r" + row + " c" + column).className == "bed")  {
        handleWin();
        return true;        
      } else {
      return false;
 }
}  

// if the car has gone off the table, this tidies up including crash message
function handleCrash() {
	window.clearInterval(intervalHandle);
	document.getElementById("Message").innerText = "You hit the wall"
}
function handleWin() {
    flagCount += 1
    document.getElementById("r" + row + " c" + column).className == carClass
    if (flagCount == flagMax){
	window.clearInterval(intervalHandle);
	document.getElementById("Message").innerText = "WELL DONE YOU WIN!!!"
    }
}