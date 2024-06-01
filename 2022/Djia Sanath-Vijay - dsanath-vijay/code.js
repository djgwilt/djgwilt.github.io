// listen for keypress (to detect arrow keys)
document.onkeydown = checkKey
// to store movement direction
var xDir = 0
var yDir = 0
// to store current column position
var column = 0
var row = 0
var xDir2 = 0
var yDir2 = 0
// to store current column position
var column2 = 0
var row2 = 9
var MoveA=0
var MoveB=0
var score = 0
var score2 = 0
var phonex=9
var phoney=1
var computerx = 9
var computery = 9
// to store the handle code for the timer interval to cancel it when we crash
var intervalHandle
// the function called when a key is pressed - sets direction variable
function checkKey(e) {
	// for all keys, see https://developer.mozilla.org/en-US/docs/Web/API/UI_Events/Keyboard_event_key_values
	if (e.key == "ArrowRight") {
		xDir = 1
		yDir = 0
	} else if (e.key == "ArrowLeft") {
		xDir = -1
		yDir = 0
	} else if (e.key == "ArrowUp") {
		yDir = -1
		xDir = 0
	} else if (e.key == "ArrowDown") {
		yDir = 1
		xDir = 0
	}
	if (e.key == "d") {
		xDir2 = 1
		yDir2 = 0
	} else if (e.key == "a") {
		xDir2 = -1
		yDir2 = 0
	} else if (e.key == "w") {
		yDir2 = -1
		xDir2 = 0
	} else if (e.key == "s") {
		yDir2 = 1
		xDir2 = 0
	}
}
// called when the page is loaded to start the timer checks
function runGame() {
	intervalHandle = setInterval(updatePosition, 250)
}
function getCell(row, column) {
	return document.getElementById("R" + row + "C" + column)
}
// the timer check function - runs every 300 milliseconds to update the car position
function updatePosition() {
	if (xDir != 0 & MoveA==0) {
		// Set the cell where the car was to empty
		getCell(row, column).className = ""

		// Update the column position for the car
		column += xDir

		// Re-draw the car (or report a crash)
		if (!getCell(row, column) || getCell(row, column).className == "wall") {
			// the target cell doesn't exist, so we are outside the game area
			crash()
		} else if(getCell(row,column).className == "Coin") {
			incrementScore()
		} else if (getCell(row,column).className == "Car2") {
			hitPerson()
		} else if (getCell(row, column).className == "computer" & score > score2) {
			win()
		} else if (getCell(row, column).className == "phone") {
			getCell(row,column).className = "phone"
			hitPhone()
		} else {
			getCell(row, column).className = "Car"
		}
	}
	if (yDir != 0 & MoveA==0) {
		// Set the cell where the car was to empty
		getCell(row, column).className = ""

		// Update the column position for the car
		row += yDir

		// Re-draw the car (or report a crash)
		if (!getCell(row, column) || getCell(row, column).className == "wall") {
			// the target cell doesn't exist, so we are outside the game area
			crash()
		} else if(getCell(row,column).className == "Coin") {
			incrementScore()
		} else if (getCell(row,column).className == "Car2") {
			hitPerson()
		} else if (getCell(row, column).className == "computer" & score > score2) {
			win()
		} else if (getCell(row, column).className == "phone") {
			getCell(row,column).className = "phone"
			hitPhone()
			getCell(row,column).className = "phone"
		} else {
			getCell(row, column).className = "Car"
		}
	}
	if (xDir2 != 0 & MoveB == 0) {
		// Set the cell where the car was to empty
		getCell(row2, column2).className = ""

		// Update the column position for the car
		column2 += xDir2

		// Re-draw the car (or report a crash)
		if (!getCell(row2, column2) || getCell(row2, column2).className == "wall") {
			// the target cell doesn't exist, so we are outside the game area
			crash_2()
		} else if(getCell(row2,column2).className == "Coin") {
			incrementScore2()
			getCell(row2, column2).className = "Car2"
		} else if (getCell(row2,column2).className == "Car") {
			hitPerson()
		} else if (getCell(row2, column2).className == "phone" & score2 > score) {
			win2()
		} else if (getCell(row2, column2).className == "computer") {
			getCell(row2,column2).className = "computer"
			hitComputer()
		} else {
			getCell(row2, column2).className = "Car2"
		}
	}
	if (yDir2 != 0 & MoveB == 0) {
		// Set the cell where the car was to empty
		getCell(row2, column2).className = ""

		// Update the column position for the car
		row2 += yDir2

		// Re-draw the car (or report a crash)
		if (!getCell(row2, column2) || getCell(row2, column2).className == "wall") {
			// the target cell doesn't exist, so we are outside the game area
			crash_2()
		} else if(getCell(row2,column2).className == "Coin") {
			incrementScore2()
			getCell(row2, column2).className = "Car2"
		} else if (getCell(row2,column2).className == "Car") {
			hitPerson()
		} else if (getCell(row2, column2).className == "phone" & score2 > score) {
			win2()
		} else if (getCell(row2, column2).className == "computer") {
			getCell(row2,column2).className = "computer"
			hitComputer()
		} else {
			getCell(row2, column2).className = "Car2"
		}
	}
}
// Returns Mr Attenborough to original position
function returnsquare() {
	getCell(phoney, phonex).className = "phone"
	row = 0
	column = 0
	MoveA=0
	getCell(row, column).className = "Car"

}
//Returns Dr Denes to original position
function returnsquare_2() {
	getCell(computery,computerx).className == "computer"
	row2 = 9
	column2 = 0
	MoveB = 0
	getCell(row2, column2).className = "Car2"
	getCell(computery,computerx).className = "computer"
}
// Returns Mr Attenborough to the start if he picks up the phone
function hitPhone() {
	//window.clearInterval(intervalHandle)
	document.getElementById("Message").innerText = "Player 1: Wrong item, return to start..."
	window.setTimeout(returnsquare, 500)
	window.setTimeout(clearText, 1000)
}
function hitComputer() {
	//window.clearInterval(intervalHandle)
	document.getElementById("Message").innerText = "Player 2: Wrong item, return to start..."
	window.setTimeout(returnsquare_2, 500)
	window.setTimeout(clearText, 1000)
}
// if the car has gone off the table, this tidies up including crash message
//CRASH FUNCTION FOR MR. ATTENBOROUGH
function crash() {
	//window.clearInterval(intervalHandle)
	MoveA=1
	row = 0
	column = 0
	xDir=0
	yDir=0
	document.getElementById("Message").innerText = "Player 1: Oops you crashed...";
	// Sets it to after a crash, retruns Mr Attenborough to (0,0) after 1/2 of a second
	window.setTimeout(returnsquare, 500);
	window.setTimeout(clearText, 1000)
}
//CRASH FUNCTION FOR DR.DENES
function crash_2() {
	//window.clearInterval(intervalHandle)
	MoveB=1
	row2 = 9
	column2 = 0
	xDir2=0
	yDir2=0
	document.getElementById("Message").innerText = "Player 2: Oops you crashed...";
	// Sets it to after a crash, retruns Mr Attenborough to (0,0) after 1/2 of a second
	window.setTimeout(returnsquare_2, 500);
	window.setTimeout(clearText, 1000)
}
//WIN FOR MR ATTENBOROUGH
function win() {
	window.clearInterval(intervalHandle)
	document.getElementById("Message").innerText = "Player 1: You have won!"
	window.setTimeout(returnsquare, 500)
}
//WIN FOR DR DENES
function win2() {
	window.clearInterval(intervalHandle)
	document.getElementById("Message").innerText = "Player 2: You have won!"
	window.setTimeout(returnsquare_2, 500)
}
//Clear the text bar
function clearText() {
	document.getElementById("Message").innerText = " "
}
//Hit other Person
function returnBothSquare(){
	returnsquare();
	returnsquare_2();
	clearText();
	moveRestart();
}
function hitPerson() {
	getCell(row, column).className = ""
	getCell(row2, column2).className = ""
	MoveA = 1
	MoveB = 1
	row = 0
	row2 = 9
	column = 0
	column2 = 0
	xDir = 0
	xDir2 = 0
	yDir = 0
	yDir2 = 0
	document.getElementById("Message").innerText = "Both Players: Crashed into eachother..."
	getCell(row, column).className = ""
	getCell(row2, column2).className = ""
	// window.setTimeout(returnsquare, 200)
	// window.setTimeout(returnsquare_2, 200)
	// window.setTimeout(clearText, 300)
	// window.setTimeout(moveRestart,200)
	window.setTimeout(returnBothSquare,200)
}
function moveRestart() {
	MoveA = 0
	MoveB = 0
}
//Increments score for Attenborough
function incrementScore() {
	getCell(row,column).className = "Car"
	score += 1
	document.getElementById("score").innerText = score
	console.log(score)
}
//Increments score for Denes
function incrementScore2() {
	getCell(row2,column2).className == "Car2"
	score2 += 1
	document.getElementById("score2").innerText = score2
	console.log(score2)
}
// when the page loaded...
$(document).ready(function () {
	runGame();
});