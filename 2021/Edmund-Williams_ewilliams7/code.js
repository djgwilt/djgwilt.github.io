// listen for keypress (to detect arrow keys)
document.onkeydown = checkKey
function switch(){
   window.location.href = "index2.html";
}; 

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

    if (e.keyCode == '68') {
        // right arrow
	    xDir = 1
        yDir = 0
    } else if (e.keyCode == '65') {
        // left arrow
	    xDir = -1
        yDir = 0
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
		if (!document.getElementById("r" + row + " c" + column)) { 
			handleCrash()
        } if (document.getElementById("r" + row + " c" + column).className == "wall") {
            handleCrash()
            document.getElementById("r" + row + " c" + column).className = "blue"
            yDir = 0
            xDir = 0
		} else {
			document.getElementById("r" + row + " c" + column).className = "blob"
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
		if (!document.getElementById("r" + row + " c" + column)) { 
			handleCrash()
        } if (document.getElementById("r" + row + " c" + column).className == "wall") {
            handleCrash()
            document.getElementById("r" + row + " c" + column).className = "blue"
            yDir = 0
            xDir = 0
        } else {
			document.getElementById("r" + row + " c" + column).className = "blob"
		}
	}    // ********************
    
}

// if the car has gone off the table, this tidies up including crash message
function handleCrash() {
	window.clearInterval(intervalHandle)
	document.getElementById("Message").innerText = "You died..."
}
function reset() {   
    // to store movement direction
    xDir = 0
    yDir = 0
    
    // to store current column position
    column = 0
    row = 0

    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = ""
    
    document.getElementById("RacingTrack").innerHTML = `<table id="RacingTrack">
        <tr>
            <td id="r0 c0" class="blob"></td>
            <td id="r0 c1"></td>
            <td id="r0 c2"></td>
            <td id="r0 c3"></td>
            <td id="r0 c4"></td>
            <td id="r0 c5"></td>
            <td id="r0 c6"></td>
            <td id="r0 c7"></td>
        </tr>
        <!-- Add another table row here -->
        <tr>
            <td id="r1 c0" class="wall"></td>
            <td id="r1 c1" class="wall"></td>
            <td id="r1 c2"></td>
            <td id="r1 c3" class="wall"></td>
            <td id="r1 c4" class="wall"></td>
            <td id="r1 c5" class="wall"></td>
            <td id="r1 c6"></td>
            <td id="r1 c7" class="wall"></td>
        </tr>
                <tr>
            <td id="r2 c0" class="wall"></td>
            <td id="r2 c1"></td>
            <td id="r2 c2"></td>
            <td id="r2 c3" class="wall"></td>
            <td id="r2 c4" class="wall"></td>
            <td id="r2 c5" class="wall"></td>
            <td id="r2 c6"></td>
            <td id="r2 c7"></td>
        </tr>
                <tr>
            <td id="r3 c0"></td>
            <td id="r3 c1"></td>
            <td id="r3 c2"></td>
            <td id="r3 c3"></td>
            <td id="r3 c4"></td>
            <td id="r3 c5"></td>
            <td id="r3 c6"></td>
            <td id="r3 c7"></td>
        </tr>
                <tr>
            <td id="r4 c0"></td>
            <td id="r4 c1"></td>
            <td id="r4 c2"></td>
            <td id="r4 c3"></td>
            <td id="r4 c4"></td>
            <td id="r4 c5"></td>
            <td id="r4 c6"></td>
            <td id="r4 c7"></td>
        </tr>
                <tr>
            <td id="r5 c0"></td>
            <td id="r5 c1"></td>
            <td id="r5 c2"></td>
            <td id="r5 c3"></td>
            <td id="r5 c4"></td>
            <td id="r5 c5"></td>
            <td id="r5 c6"></td>
            <td id="r5 c7"></td>
        </tr>
                <tr>
            <td id="r6 c0"></td>
            <td id="r6 c1"></td>
            <td id="r6 c2"></td>
            <td id="r6 c3"></td>
            <td id="r6 c4"></td>
            <td id="r6 c5"></td>
            <td id="r6 c6"></td>
            <td id="r6 c7"></td>
        </tr>
                <tr>
            <td id="r7 c0"></td>
            <td id="r7 c1"></td>
            <td id="r7 c2"></td>
            <td id="r7 c3"></td>
            <td id="r7 c4"></td>
            <td id="r7 c5"></td>
            <td id="r7 c6"></td>
            <td id="r7 c7" class="goal"></td>
        </tr>
        
    </table>`
    runGame()
}
