// listen for keypress (to detect arrow keys)
document.onkeydown = checkKey

// to store movement direction
var xDir = 0
var yDir = 0
// to store current column position
var row = 1
var column = 0
// to store the handle code for the timer interval to cancel it when we crash
var intervalHandle
var intervalHandle2

var score = 0 

c = 0

// the function called when a key is pressed - sets direction variable
function checkKey(e) {
    // for all keys, see https://developer.mozilla.org/en-US/docs/Web/API/UI_Events/Keyboard_event_key_values
    if (e.key == "ArrowUp") {
        yDir = -1
        xDir = 0

    } else if (e.key == "ArrowDown") {
        yDir = 1
        xDir = 0

    }

}

// called when the page is loaded to start the timer checks
function runGame() {
    intervalHandle = setInterval(updatePosition, 300)
    intervalHandle2 = setInterval(pipeupdatePosition, 400)
}

function getCell(row, column) {
  return document.getElementById("R" + row + "C" + column)
}



// the timer check function - runs every 300 milliseconds to update the car position
function updatePosition() {
    } if (yDir != 0) {
        // Set the cell where the car was to empty
        getCell(row, column).className = ""
        
        // Update the column position for the car
        row += yDir
        
        // Re-draw the car (or report a crash)
        
        if (!getCell(row,column) || getCell(row,column+1).className == "Wall"){
            // the target cell doesn't exist, so we are outside the game area
            crash()
        
        } else if (getCell(row, column+1).className == "Coin") {
			score += 1
			document.getElementById("score").innerText = ("score:"+ score)

		} else {
            getCell(row, column).className = "Car"
        }
        yDir = 0
    
	}
	
	

var pipecolumn = 9
var coinrow = Math.floor(Math.random()* 9)
function pipeupdatePosition() {
    if (pipecolumn != 0) {

        for (let i = 1;i < 10;i++){
            if (getCell(i,pipecolumn).className == "Car"){
                crash()
            } else {
                getCell(i,pipecolumn).className == "Wall"
            }
        }
        pipecolumn -= 1
        
        for (let i = 1;i < 10;i++){
            if (getCell(i,pipecolumn).className == "Car"){
                crash()
            } else {
                getCell(i,pipecolumn).className == "Wall"
            }
        }
        
        
        getCell(coinrow+1,pipecolumn).className = ""
        getCell(coinrow-1,pipecolumn).className = ""
        getCell(coinrow,pipecolumn).className = "Coin"
        
        for (let i = 1;i < 10;i++){
            getCell(i,pipecolumn+1).className == ""
        }

        if (pipecolumn == 0){
            getCell(1,0).className = ""
            getCell(2,0).className = ""
            getCell(3,0).className = ""
            getCell(4,0).className = ""
            getCell(5,0).className = ""
            getCell(6,0).className = ""
            getCell(7,0).className = ""
            getCell(8,0).className = ""
            getCell(9,0).className = ""
            pipecolumn = 9
            coinrow = Math.floor(Math.random()* 10)
        }
    }

}



// if the car has gone off the table, this tidies up including crash message
function crash() {
	window.clearInterval(intervalHandle)
	document.getElementById("Message").innerText = "Oops you crashed..."
}

// when the page loaded...
$( document ).ready(function() {
    runGame();
});