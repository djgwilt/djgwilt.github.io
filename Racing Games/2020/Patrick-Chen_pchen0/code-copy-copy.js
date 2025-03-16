// listen for keypress (to detect arrow keys)
document.onkeydown = checkKey

// to store movement direction
var xDir = 0
var yDir = 0
var flagCount = 0
var flagMax = 7
var audio = new Audio("coin.mp3")
// to store current column position
var column = 0
var row = 0
// to store the handle code for the timer interval to cancel it when we crash
var intervalHandle

// to remember car direction
var carclass = "Car"
// the function called when a key is pressed - sets direction variable
function checkKey(e) {
    // this next line is a workaround for older versions of IE which didn't pass the event as a parameter
    e = e || window.event

    if (e.keyCode == '68') {
        // right arrow
	    xDir = 1
        yDir = 0
        carclass = "Car"
    } else if (e.keyCode == '65') {
        // left arrow
	    xDir = -1
        yDir = 0
        carclass = "CarFlip"
    } else if (e.keyCode == '87') {
        // up arrow
	    yDir = -1
        xDir = 0
    } else if (e.keyCode == '83') {
        // down arrow
	    yDir = 1
        xDir = 0
}
}

// called when the page is loaded to start the timer checks
function runGame() {
	intervalHandle = setInterval(updatePosition, 500)
}

// the timer check function - runs every 300 milliseconds to update the car position
function updatePosition() {
	if (xDir != 0 || yDir != 0) {
        // Set the cell where the car was to empty
		document.getElementById("r" +row+ " c" + column).className = "Empty";
        // Update the column position for the car
		column += xDir;
        row += yDir
        // Re-draw the car (or report a crash)
        }
        if (!document.getElementById("r" + row + " c" + column) || document.getElementById("r" + row + " c" + column).className == "wall" || document.getElementById("r"+ row + " c" + column).className == "meanwall") {
			handleCrash();
        } else if (document.getElementById("r" + row + " c" + column).className == "flag"){
            handleWin();
            document.getElementById("r" + row + " c" + column).className = carclass;
		} else {
			document.getElementById("r" + row + " c" + column).className = carclass;
	}

}


// if the car has gone off the table, this tidies up including crash message
function handleCrash() {
	window.clearInterval(intervalHandle)
    for (i = 0; i < 20 ; i++) {
        for (j = 0; j < 13; j++) {
            document.getElementById("r"+j+" c"+i).className = "Empty"
        }
    }
    document.getElementById("r0 c5").className = "letterY"
    document.getElementById("r0 c6").className = "letterO"
    document.getElementById("r0 c7").className = "letterU"
    document.getElementById("r1 c5").className = "letterL"
    document.getElementById("r1 c6").className = "letterO"
    document.getElementById("r1 c7").className = "letterS"
    document.getElementById("r1 c8").className = "letterE"
	document.getElementById("Message").innerText = "Oops you crashed into katchin..."
}

function handleWin() {
    flagCount += 1
    audio.play()
    if (flagCount == flagMax){
        for (i = 0; i < 20 ; i++) {
            for (j = 0; j < 13; j++) {                
                document.getElementById("r"+j+" c"+i).className = "Empty"                
            }
        }
        window.clearInterval(intervalHandle)
        document.getElementById("r0 c5").className = "letterW"
        document.getElementById("r0 c6").className = "letterE"
        document.getElementById("r0 c7").className = "letterL"
        document.getElementById("r0 c8").className = "letterL"
        document.getElementById("r1 c5").className = "letterD"
        document.getElementById("r1 c6").className = "letterO"
        document.getElementById("r1 c7").className = "letterN"
        document.getElementById("r1 c8").className = "letterE"
        document.getElementById("Message").innerText = "Well Done!!!"
        }   
        }
    


