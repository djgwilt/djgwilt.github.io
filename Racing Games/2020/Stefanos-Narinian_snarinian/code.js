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
var carClass = "CarRight"
var xRand = 0
var yRand = 0
var score = 0
var Time = 100
var realTime = 30
var newWall = 0
var newFlag = 0
var timeHandle
// the function called when a key is pressed - sets direction variable
function checkKey(e) {
    // this next line is a workaround for older versions of IE which didn't pass the event as a parameter
    e = e || window.event

    if (e.keyCode == '39') {
        // right arrow
	    xDir = 1
        yDir = 0
        carClass = "CarRight"
    } else if (e.keyCode == '37') {
        // left arrow
	    xDir = -1
        yDir = 0
        carClass = "CarLeft"
    } else if (e.keyCode == '40') {
        // down arrow
	    yDir = 1
        xDir = 0
        
    } else if (e.keyCode == '38'){
        //up arrow
        yDir = -1
        xDir = 0
        
    }
}

// called when the page is loaded to start the timer checks
function runGame() {
    document.getElementById("Game").style.display = "block"
    document.getElementById("Start").style.display = "none"
	intervalHandle = setInterval(updatePosition, 300)
    timeHandle = setInterval(updateTime, 1000)
}

// the timer check function - runs every 300 milliseconds to update the car position
function updatePosition() {
    xRand = Math.floor(Math.random() * 8)
    yRand = Math.floor(Math.random() * 8)
    if (Time > 0) {
        Time -= 1
        if (newFlag == 6) {
            document.getElementById("r" + yRand + " c" + xRand).className = "flag"
            newFlag = 0
        } else {
            newFlag += 1
        }  
        if (newWall == 10) {
            document.getElementById("r" + yRand + " c" + xRand).className = "wall"
            newWall = 0
        } else{
            newWall += 1
        }
        if (xDir != 0 || yDir != 0){
            document.getElementById("r" + row + " c" + column).className = "Empty"
            column += xDir
            row += yDir
            if (!document.getElementById("r" + row + " c" + column) || document.getElementById("r" + row + " c" + column).className == "wall" ){
                handleCrash()
            } else if (document.getElementById("r" + row + " c" + column).className == "flag") {
                score += 1
                document.getElementById("r" + row + " c" + column).className = carClass
            } else {
                document.getElementById("r" + row + " c" + column).className = carClass
            }
            
        }
        
		 
    } else {
        youWin()
    }
}
function updateTime() {
    realTime -= 1
    document.getElementById("RealTime").innerText = "Time left: " + realTime
}
    
	
    
	


// if the car has gone off the table, this tidies up including crash message
function handleCrash() {
	window.clearInterval(intervalHandle)
    window.clearInterval(timeHandle)
    document.getElementById("RealTime").style.display = "none"
	document.getElementById("Message").innerText = "Oops you crashed... Your score was " + score
}
function youWin() {
    window.clearInterval(intervalHandle)
    window.clearInterval(timeHandle)
    document.getElementById("RealTime").style.display = "none"
    document.getElementById("Message").innerText = "Well Done, your score was " + score
}
function restart() {
    location.reload()
}