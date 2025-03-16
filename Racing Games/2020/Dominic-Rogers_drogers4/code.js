// listen for keypress (to detect arrow keys)
document.onkeydown = checkKey

// to store movement direction
var xDir = 5
var yDir = 5
var score = 0
var constant = 0
var x = 0
var y = 0
var level = 0
var current_level = 0
var add = 0
var string = 0
var query = undefined
var url = undefined
var le = undefined
var test_level = 0
var bool = false


// to store current column position
var column = 0
var row = 0

// to store the handle code for the timer interval to cancel it when we crash
var intervalHandle

// the function called when a key is pressed - sets direction variable
function checkKey(e) {
    e = e || window.event
    if (xDir == 5 && yDir == 5) {
        xDir = 0
        yDir = 0
    } if (e.keyCode == '39') {
        // right arrow
	    xDir = 1
        yDir = 0
    } else if (e.keyCode == '37') {
        // left arrow
	    xDir = -1
        yDir = 0
    } else if (e.keyCode == '38') {
        // up arrow
        yDir = -1
        xDir = 0
    } else if (e.keyCode == '40') {
        //down arrow
        yDir = 1
        xDir = 0
    }
}

// called when the page is loaded to start the timer checks
function runGame(le) {
    current_level = le
	intervalHandle = setInterval(updatePosition, 300)
    newcoin()
    document.getElementById("Message").innerText = "Level is " + current_level + " and unlcoked is " + level + " and add is " + add + " and string is " + string
    console.log("Won is " + level + " and we are currently on level " + current_level)
}

// the timer check function - runs every 300 milliseconds to update the car position
function updatePosition() {
	if (xDir != 5)  {
        // Set the cell where the car was to empty
        if (!document.getElementById("r" + (row + yDir) + " c" + (column + xDir))) {}
        else if (document.getElementById("r" + (row + yDir) + " c" + (column + xDir)).className == "Coin") {
            score += 1
            newcoin()
        }
        else if (document.getElementById("r" + (row + yDir) + " c" + (column + xDir)).className == "Wall") {
            handleCrash()
            document.getElementById("r" + row +" c" + column).className = "Empty"
            return
        }
        else if (document.getElementById("r" + (row + yDir) + " c" + (column + xDir)).className == "Flag") {
            document.getElementById("r" + row + " c" + column).className = "Empty"
            document.getElementById("r" + (row + yDir) + " c" + (column + xDir)).className = "Car"
            if (score >= (5 * current_level)) {
            win()
            }
        }
		document.getElementById("r" + row + " c" + column).className = "Empty"
        column += xDir
        row += yDir
        // Re-draw the car (or report a crash)
		if (!document.getElementById("r" + row + " c" + column)) {
			handleCrash()
		} else {
			document.getElementById("r" + row + " c" + column).className = "Car"
            if (score >= (5 * current_level) && row != 9 && column != 4) {
                document.getElementById("Message").innerText = "You have a score of " + score + "! reach the flag to continue."
            }
		}
	}
}

// if the car has gone off the table, this tidies up including crash message
function handleCrash() {
	window.clearInterval(intervalHandle)
	document.getElementById("Message").innerText = "Game Over, Score: " + score 
    document.getElementById("Button").style.display = "block"
}
function win() {
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "You Win, Score: " + score
    document.getElementById("Button_Flag").style.display = "block"
    console.log("current_level is " + current_level)
    if (bool == false) {
         level += 1   
    }
    /*if (current_level == level) {
        add = 1
    }
    else {
        add = 0
    }
    level += add
    */
    bool = true
}
function explanation() {
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "You must get " + (5 * current_level) + " or over to advance! Score: " + score
    document.getElementById("Button_Flag").style.display = "block"
}
function newcoin() {
    while (constant <= 1000000)  {
        x = Math.floor(Math.random() * 11)
        y = Math.floor(Math.random() * 10)
        if (!document.getElementById("r" + y + " c" + x)) {continue}
        if (document.getElementById("r" + y + " c" + x).className == "Empty") {
                break
            }
        constant += 1
    }
    document.getElementById("r" + y + " c" + x).className = "Coin"
    constant = 0
    document.getElementById("score").innerText = "Score: " + score
}
function Button(le) {
    document.getElementsByClassName("Coin")[0].className = "Empty"
    document.getElementById("Button").style.display = "none"
    document.getElementById("Message").innerText = ""
    add = 0
    row = 0
    column = 0
    xDir = 0
    yDir = 0
    score = 0
    runGame(current_level) 
}
function Button_Flag(le) {
    document.getElementById("Button_Flag").style.display = "none"
    document.getElementsByClassName("Car")[0].className = "Empty"
    document.getElementById("Message").innerText = ""
    document.getElementsByClassName("Coin")[0].className = "Empty"
    document.getElementById("r0 c0").className = "Car"
    document.getElementById("r0 c0").className = "Car"
    document.getElementById("r9 c4").className = "Flag"
    row = 0
    column = 0
    xDir = 0
    yDir = 0
    score = 0
    runGame(current_level)
}
function Next_Level(query, url) {
    if ((level + current_level) >= query) {
        window.location=url
    }
}
function Unlock() {
    document.getElementById("Level_" + (level + current_level)).className="Unlocked"
    document.getElementById("debug").innerText = level + "is level and current_level is " + current_level
}
function add_to_level() {
    document.getElementById("Button").style.display = "none"
    document.getElementById("Button_Flag").style.display = "none"
    document.getElementById("Return_Button").style.display = "none"
    document.getElementById("RacingTrack").style.display = "none"
    document.getElementById("Message").style.display = "none"
    document.getElementById("instruction").style.display = "none"
    document.getElementById("score-container").style.display = "none"
    document.getElementById("score").style.display = "none"
    document.getElementById("Finir").style.display = "block"
    document.getElementById("Level_1").style.display = "block"
    document.getElementById("Level_2").style.display = "block"
    document.getElementById("Level_3").style.display = "block"
    document.getElementById("add_to_level").style.display = "block"
    document.getElementById("debug").style.display = "block"
}