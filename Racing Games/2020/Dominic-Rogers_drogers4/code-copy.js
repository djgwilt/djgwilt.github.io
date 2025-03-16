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
var coordinates = []


// to store current column position
var column = 0
var row = 0

// to store the handle code for the timer interval to cancel it when we crash
var intervalHandle

// the function called when a key is pressed - sets direction variable
function checkKey(e) {
    // this next line is a workaround for older versions of IE which didn't pass the event as a parameter
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
	intervalHandle = setInterval(updatePosition, 300)
    newcoin()
}

// the timer check function - runs every 300 milliseconds to update the car position
function updatePosition() {
	if (xDir != 5)  {
        // Set the cell where the car was to empty
        if (!document.getElementById("r" + (row + yDir) + " c" + (column + xDir))) {}
        else if (document.getElementById("r" + (row + yDir) + " c" + (column + xDir)).className == "Coin") {
            score += 1
            newcoin()
            if (score % 5 == 0) {
                obstruction()
            }
        }
        else if (document.getElementById("r" + (row + yDir) + " c" + (column + xDir)).className == "Wall") {
            handleCrash()
            document.getElementById("r" + row +" c" + column).className = "Empty"
            return
        }
		document.getElementById("r" + row + " c" + column).className = "Empty"
        column += xDir
        row += yDir
        // Re-draw the car (or report a crash)
		if (!document.getElementById("r" + row + " c" + column)) {
			handleCrash()
		} else {
			document.getElementById("r" + row + " c" + column).className = "Car"
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
    bool = true
    }
}
function newcoin() {
    while (constant <= 100)  {
        x = Math.floor(Math.random() * 8)
        y = Math.floor(Math.random() * 10)
        if (document.getElementById("r" + y + " c" + x).className == "Empty") {
                break
            }
        constant += 1
    }
    document.getElementById("r" + y +" c" + x).className = "Coin"
    constant = 0
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
    for (var i = 0; i < coordinates.length; i+=2) {
        document.getElementById("r" + coordinates[i + 1] + " c" + coordinates[i]).className = "Empty"
    }
    coordinates = []
    runGame(current_level) 
}

function obstruction() {
    while (constant <= 100) {
        x = Math.floor(Math.random()*8)
        y = Math.floor(Math.random()*10)
        if (!document.getElementById("r" + y + " c" + x) || !document.getElementById("r" + (y + 1) + " c" + x) || !document.getElementById("r" + (y - 1) + " c" + x) || !document.getElementById("r" + y + " c" + (x + 1)) || document.getElementById("r" + y + " c" + (x - 1))) {
            console.log(x + " " + y)
        }
        if (document.getElementById("r" + y + " c" + x).className == "Empty" && (document.getElementById("r" + (y + 1) + " c" + x).className == "Empty" || document.getElementById("r" + (y - 1) + " c" + x).className == "Empty") && (document.getElementById("r" + y + " c" + (x + 1)).className == "Empty" || document.getElementById("r" + y + " c" + (x - 1)).className == "Empty")) {
            document.getElementById("r" + y + " c" + x).className = "Wall"
            coordinates.push(x)
            coordinates.push(y)
            break
        }
        else{
            console.log("Error")
        }
    }
    constant = 0
}