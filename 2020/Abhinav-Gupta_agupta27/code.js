// listen for keypress (to detect arrow keys)
document.onkeydown = checkKey

// to store movement direction
var xDir = 0
var carClass = "Car"
// to store current column position
var column = 0
var flags = 1
// to store the handle code for the timer interval to cancel it when we crash
var intervalHandle
var yDir = 0
var row = 0
var flash = 0

// the function called when a key is pressed - sets direction variable
function checkKey(e) {
    // this next line is a workaround for older versions of IE which didn't pass the event as a parameter
    e = e || window.event

    if (e.keyCode == '39') {
        // right arrow
	    xDir = 1
        yDir = 0
        carClass = "Car"
    } else if (e.keyCode == '37') {
        // left arrow
	    xDir = -1
        yDir = 0
        carClass = "Carflip"
    } else if (e.keyCode == '38') {
        // up arrow
	    yDir = -1
        xDir = 0
    } else if (e.keyCode == '40') {
        // down arrow
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
		document.getElementById("r" + row + " c" + column).className = "Empty";
        // Update the column position for the car
		column += xDir;
        row += yDir;
        // Re-draw the car (or report a crash)
        if (!document.getElementById("r" + row + " c" + column)) {
			handleCrash()
        } else if (document.getElementById("r" + row + " c" + column).className == "flag") {
            flags -= 1;
		} else if (document.getElementById("r" + row + " c" + column).className == "wall") {
            handleCrash()
        } else if (document.getElementById("r" + row + " c" + column).className == "fakeflag") {
            handleWayfinder()
        } else {
            document.getElementById("r" + row + " c" + column).className = carClass;
        }
	}

    if (flags == 0) {
        document.getElementById("r" + row + " c" + column).className = "Empty";
        handleWin();
    }
    if (flash == 2) {
        document.getElementById("r0 c1").className = "fakeD";
        document.getElementById("r0 c2").className = "fakeD";
        document.getElementById("r0 c3").className = "fakeD";
        document.getElementById("r0 c7").className = "fakeD";
        document.getElementById("r1 c1").className = "fakeD";
        document.getElementById("r1 c4").className = "fakeD";
        document.getElementById("r2 c0").className = "fakeD";
        document.getElementById("r2 c3").className = "fakeD";
        document.getElementById("r2 c5").className = "fakeD";
        document.getElementById("r2 c6").className = "fakeD";
        document.getElementById("r3 c0").className = "fakeD";
        document.getElementById("r3 c3").className = "fakeD";
    }
    flash += 1
}

// if the car has gone off the table, this tidies up including crash message
function handleCrash() {
	window.clearInterval(intervalHandle)
	document.getElementById("Message").innerText = "Oops you crashed..."
}
function handleWin() {
	window.clearInterval(intervalHandle)
	document.getElementById("Message").innerText = "CONGRADULATIONS YOU WIN!!"
}
function handleWayfinder() {
	window.clearInterval(intervalHandle)
	document.getElementById("Message").innerText = "Only 2 were made. Sadly for you Kylo Ren breaks this one, start again and avoid this broken wayfinder"
}