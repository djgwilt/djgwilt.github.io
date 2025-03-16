// listen for keypress (to detect arrow keys)
document.onkeydown = checkKey

// to store movement direction
var xDir = 0
var yDir = 0

// to store current column position
var column = 0
var row = 0
var coins = 0

// to store the handle code for the timer interval to cancel it when we crash
var intervalHandle

// the function called when a key is pressed - sets direction variable
function checkKey(e) {
    // this next line is a workaround for older versions of IE which didn't pass the event as a parameter
    e = e || window.event

    if (e.keyCode == '39' ) {
        // right arrow
        xDir = 1
        yDir = 0
    } else if (e.keyCode == '37' ) {
        // left arrow
        
        xDir = -1
        yDir = 0
    } else if (e.keyCode == '40' ) {
        // down arrow
        yDir = 1
        xDir = 0    
    } else if (e.keyCode == '38' ) {
        // up arrow
        yDir = -1
        xDir = 0
    }   
}

// called when the page is loaded to start the timer checks
function runGame() {
    intervalHandle = setInterval(updatePosition, 250)
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
        if (!document.getElementById("r" + row + " c" + column) || document.getElementById("r" + row + " c" + column).className == "Wall") {
            handleCrash()
        }  else if (document.getElementById("r" + row + " c" + column).className == "coin") {
            handleCoin()
            document.getElementById("r" + row + " c" + column).className = "Car"
        }else if (document.getElementById("r" + row + " c" + column).className == "Flag") {
            handleWin()
        } else {
            document.getElementById("r" + row + " c" + column).className = "Car"
        }
    }    
}

// if the car has gone off the table, this tidies up including crash message
function handleCrash() {
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Oh no!"
    var audio = document.getElementById("MarioDies");
    audio.autoplay = true;
    audio.load();
}

function handleWin() {
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "You won! You scored " + coins + " out of 20"
    var audio = document.getElementById("MarioWin");
    audio.autoplay = true;
    audio.load();
}

function handleCoin() {
    coins += 1
    document.getElementById("coinScore").innerText = "Score: " + coins
}



function runWeb() {   
    // to store movement direction
    xDir = 0
    yDir = 0
    
    // to store current column position
    column = 0
    row = 0
    coins = 0
    
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = ""
    
    document.getElementById("gameArea").innerHTML = `<table id="RacingTrack">
        <!-- The table cells have an id with the row and column number -->
        <tr>
            <td id="r0 c0" class="Car"></td>
            <td id="r0 c1" class="Wall"></td>
            <td id="r0 c2" ></td>
            <td id="r0 c3" ></td>
            <td id="r0 c4" ></td>
            <td id="r0 c5" ></td>
            <td id="r0 c6" ></td>
            <td id="r0 c7" ></td>
            <td id="r0 c8"></td>
            <td id="r0 c9"></td>
            <td id="r0 c10"></td>
            <td id="r0 c11"></td>
            <td id="r0 c12"></td>
            <td id="r0 c13" class="Wall"></td>
        </tr>
        <tr>
            <td id="r1 c0"></td>
            <td id="r1 c1" class="coin"></td>
            <td id="r1 c2"></td>
            <td id="r1 c3" class="Wall"></td>
            <td id="r1 c4" class="Wall"></td>
            <td id="r1 c5" class="Wall"></td>
            <td id="r1 c6" class="Wall"></td>
            <td id="r1 c7" class="Wall"></td>
            <td id="r1 c8" class="Wall"></td>
            <td id="r1 c9" class="Wall"></td>
            <td id="r1 c10" class="Wall"></td>
            <td id="r1 c11" class="Wall"></td>
            <td id="r1 c12" class="coin"></td>
            <td id="r1 c13" class="Wall"></td>
        </tr>
        <tr>
            <td id="r2 c0" class="Wall"></td>
            <td id="r2 c1" class="Wall"></td>
            <td id="r2 c2" class="Wall"></td>
            <td id="r2 c3" class="Wall"></td>
            <td id="r2 c4"></td>
            <td id="r2 c5"></td>
            <td id="r2 c6"></td>
            <td id="r2 c7" class="coin"></td>
            <td id="r2 c8"></td>
            <td id="r2 c9"></td>
            <td id="r2 c10"></td>
            <td id="r2 c11"></td>
            <td id="r2 c12"></td>
            <td id="r2 c13" ></td>
        </tr>
        <tr>
            <td id="r3 c0"></td>
            <td id="r3 c1"></td>
            <td id="r3 c2" class="coin"></td>
            <td id="r3 c3"></td>
            <td id="r3 c4"></td>
            <td id="r3 c5" class="Wall"></td>
            <td id="r3 c6" class="Wall"></td>
            <td id="r3 c7" class="Wall"></td>
            <td id="r3 c8" class="Wall"></td>
            <td id="r3 c9" class="Wall"></td>
            <td id="r3 c10" class="Wall"></td>
            <td id="r3 c11" class="Wall"></td>
            <td id="r3 c12" class="Wall"></td>
            <td id="r3 c13" ></td>
        </tr>
        <tr>
            <td id="r4 c0"></td>
            <td id="r4 c1" class="Wall"></td>
            <td id="r4 c2" class="Wall"></td>
            <td id="r4 c3" class="Wall"></td>
            <td id="r4 c4" class="Wall"></td>
            <td id="r4 c5" class="Wall"></td>
            <td id="r4 c6" class="Wall"></td>
            <td id="r4 c7" class="coin"></td>
            <td id="r4 c8" class="Wall"></td>
            <td id="r4 c9" class="coin"></td>
            <td id="r4 c10"></td>
            <td id="r4 c11"></td>
            <td id="r4 c12"></td>
            <td id="r4 c13" ></td>
        </tr>
        <tr>
            <td id="r5 c0"></td>
            <td id="r5 c1"></td>
            <td id="r5 c2"></td>
            <td id="r5 c3" class="coin"></td>
            <td id="r5 c4"></td>
            <td id="r5 c5"></td>
            <td id="r5 c6" class="Wall"></td>
            <td id="r5 c7"></td>
            <td id="r5 c8" class="Wall"></td>
            <td id="r5 c9"></td>
            <td id="r5 c10" class="Wall"></td>
            <td id="r5 c11" class="Wall"></td>
            <td id="r5 c12" class="Wall"></td>
            <td id="r5 c13" ></td>
        </tr>
        <tr>
            <td id="r6 c0" class="Wall"></td>
            <td id="r6 c1" class="Wall"></td>
            <td id="r6 c2" class="Wall"></td>
            <td id="r6 c3" class="Wall"></td>
            <td id="r6 c4" class="Wall"></td>
            <td id="r6 c5" class="coin"></td>
            <td id="r6 c6" class="Wall"></td>
            <td id="r6 c7" ></td>
            <td id="r6 c8"></td>
            <td id="r6 c9"></td>
            <td id="r6 c10" class="Wall"></td>
            <td id="r6 c11"></td>
            <td id="r6 c12"></td>
            <td id="r6 c13" class="coin"></td>
        </tr>
        <tr>
            <td id="r7 c0"></td>
            <td id="r7 c1" class="coin"></td>
            <td id="r7 c2"></td>
            <td id="r7 c3" class="Wall"></td>
            <td id="r7 c4"></td>
            <td id="r7 c5"></td>
            <td id="r7 c6" class="Wall"></td>
            <td id="r7 c7" ></td>
            <td id="r7 c8" class="Wall"></td>
            <td id="r7 c9" class="Wall"></td>
            <td id="r7 c10"></td>
            <td id="r7 c11"></td>
            <td id="r7 c12" class="Wall"></td>
            <td id="r7 c13" class="Wall"></td>
        </tr>
        <tr>
            <td id="r8 c0"></td>
            <td id="r8 c1" class="Wall"></td>
            <td id="r8 c2"></td>
            <td id="r8 c3"></td>
            <td id="r8 c4"></td>
            <td id="r8 c5" class="Wall"></td>
            <td id="r8 c6"></td>
            <td id="r8 c7" class="coin"></td>
            <td id="r8 c8" class="Wall"></td>
            <td id="r8 c9" class="Wall"></td>
            <td id="r8 c10" class="coin"></td>
            <td id="r8 c11" class="Wall"></td>
            <td id="r8 c12" class="Wall"></td>
            <td id="r8 c13" class="Wall"></td>
        </tr>
        <tr>
            <td id="r9 c0"></td>
            <td id="r9 c1" class="Wall"></td>
            <td id="r9 c2" class="Wall"></td>
            <td id="r9 c3" class="Wall"></td>
            <td id="r9 c4" class="Wall"></td>
            <td id="r9 c5" class="Wall"></td>
            <td id="r9 c6"></td>
            <td id="r9 c7" class="Wall"></td>
            <td id="r9 c8"></td>
            <td id="r9 c9"></td>
            <td id="r9 c10"></td>
            <td id="r9 c11"></td>
            <td id="r9 c12"></td>
            <td id="r9 c13"></td>
        </tr>
        <tr>
            <td id="r10 c0"></td>
            <td id="r10 c1" class="coin"></td>
            <td id="r10 c2"></td>
            <td id="r10 c3" class="Wall"></td>
            <td id="r10 c4"></td>
            <td id="r10 c5" class="coin"></td>
            <td id="r10 c6"></td>
            <td id="r10 c7" class="Wall"></td>
            <td id="r10 c8"></td>
            <td id="r10 c9" class="Wall"></td>
            <td id="r10 c10" class="Wall"></td>
            <td id="r10 c11" class="Wall"></td>
            <td id="r10 c12" class="Wall"></td>
            <td id="r10 c13" class="coin"></td>
        </tr>
        <tr>
            <td id="r11 c0"></td>
            <td id="r11 c1" class="Wall"></td>
            <td id="r11 c2"></td>
            <td id="r11 c3"></td>
            <td id="r11 c4"></td>
            <td id="r11 c5" class="Wall"></td>
            <td id="r11 c6"></td>
            <td id="r11 c7" class="coin"></td>
            <td id="r11 c8"></td>
            <td id="r11 c9"></td>
            <td id="r11 c10"></td>
            <td id="r11 c11"></td>
            <td id="r11 c12"></td>
            <td id="r11 c13" ></td>
        </tr>
        <tr>
            <td id="r12 c0"></td>
            <td id="r12 c1" class="Wall"></td>
            <td id="r12 c2" class="Wall"></td>
            <td id="r12 c3" class="Wall"></td>
            <td id="r12 c4" class="Wall"></td>
            <td id="r12 c5" class="Wall"></td>
            <td id="r12 c6" class="Wall"></td>
            <td id="r12 c7" class="Wall"></td>
            <td id="r12 c8" class="Wall"></td>
            <td id="r12 c9" class="Wall"></td>
            <td id="r12 c10" class="Wall"></td>
            <td id="r12 c11" class="Wall"></td>
            <td id="r12 c12" class="Wall"></td>
            <td id="r12 c13" class="Wall"></td>
        </tr>
        <tr>
            <td id="r13 c0"></td>
            <td id="r13 c1"></td>
            <td id="r13 c2" class="coin"></td>
            <td id="r13 c3"></td>
            <td id="r13 c4"></td>
            <td id="r13 c5" class="coin"></td>
            <td id="r13 c6"></td>
            <td id="r13 c7"></td>
            <td id="r13 c8" class="coin"></td>
            <td id="r13 c9"></td>
            <td id="r13 c10"></td>
            <td id="r13 c11" class="coin"></td>
            <td id="r13 c12"></td>
            <td id="r13 c13" class="Flag" ></td>
        </tr>
        <tr>
            <td id="r14 c0" class="Wall"></td>
            <td id="r14 c1" class="Wall"></td>
            <td id="r14 c2" class="Wall"></td>
            <td id="r14 c3" class="Wall"></td>
            <td id="r14 c4" class="Wall"></td>
            <td id="r14 c5" class="Wall"></td>
            <td id="r14 c6" class="Wall"></td>
            <td id="r14 c7" class="Wall"></td>
            <td id="r14 c8" class="Wall"></td>
            <td id="r14 c9" class="Wall"></td>
            <td id="r14 c10" class="Wall"></td>
            <td id="r14 c11" class="Wall"></td>
            <td id="r14 c12" class="Wall"></td>
            <td id="r14 c13" class="Wall"></td>
        </tr>
    </table>`
    runGame()
}