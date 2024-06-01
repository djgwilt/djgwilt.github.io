// listen for keypress (to detect arrow keys)
document.onkeydown = checkKey

var coinsmax = 27
var coinscollectedA = 0
var countdown = 3
var countdown2 = 0
var go = false
var go2 = 5


var coinscollectedB = 0



var exploded = false







// to store movement direction
var xDirA = 0
var yDirA = 0
var xDirB = 0
var yDirB = 0



// to store current column position
var columnA = 0
var rowA = 0
var columnB = 11
var rowB = 11

// to store the handle code for the timer interval to cancel it when we crash
var intervalHandle

var dirA = 0
var dirB = 0


// the function called when a key is pressed - sets direction variable
function checkKey(e) {
	// for all keys, see https://developer.mozilla.org/en-US/docs/Web/API/UI_Events/Keyboard_event_key_values
	if (e.key == "d") {
		if (getCellA(rowA, columnA+1) && document.getElementById("R" + (rowA) + "C" + (columnA+1)).className != "Wall"){
			xDirA = 1
			yDirA = 0
		} 
		
	} else if (e.key == "a") {
		if (getCellA(rowA, columnA-1) && document.getElementById("R" + (rowA) + "C" + (columnA-1)).className != "Wall"){
			xDirA = -1
			yDirA = 0
		} 
	
	} else if (e.key == "w") {
		if (getCellA(rowA-1, columnA) && document.getElementById("R" + (rowA-1) + "C" + (columnA)).className != "Wall"){
		
			yDirA = -1
			xDirA = 0
		} 
	} else if (e.key == "s") {
		if (getCellA(rowA+1, columnA) && document.getElementById("R" + (rowA+1) + "C" + (columnA)).className != "Wall"){
		
			yDirA = 1
			xDirA = 0
		}
	}
	if (e.key == "l") {
		if (getCellB(rowB, columnB+1) && document.getElementById("R" + (rowB) + "C" + (columnB+1)).className != "Wall"){
			xDirB = 1
			yDirB = 0
		} 
		
	} else if (e.key == "j") {
		if (getCellB(rowB, columnB-1) && document.getElementById("R" + (rowB) + "C" + (columnB-1)).className != "Wall"){
			xDirB = -1
			yDirB = 0
		} 
	} else if (e.key == "i") {
		if (getCellB(rowB-1, columnB) && document.getElementById("R" + (rowB-1) + "C" + (columnB)).className != "Wall"){
		
			yDirB = -1
			xDirB = 0
		}
	} else if (e.key == "k") {
		if (getCellB(rowB+1, columnB) && document.getElementById("R" + (rowB+1) + "C" + (columnB)).className != "Wall"){
			yDirB = 1
			xDirB = 0
		}
	
	}
}







// called when the page is loaded to start the timer checks
function runGame() {
	intervalHandle = setInterval(updatePosition, 200)
	

}

function getCellA(rowA, columnA) {
  	return document.getElementById("R" + rowA + "C" + columnA)
}
function getCellB(rowB, columnB) {
	return document.getElementById("R" + rowB + "C" + columnB)
}

// the timer check function - runs every 300 milliseconds to update the car position
function updatePosition() {
	if ((xDirA != 0 || yDirA != 0)  && go == true) {
		// Set the cell where the car was to empty
		getCellA(rowA, columnA).className = ""
		
		// Update the column position for the car

		columnA += xDirA
		rowA += yDirA
		
		
		// Re-draw the car (or report a crash)
		if (!getCellA(rowA, columnA) || document.getElementById("R" + rowA + "C" + columnA).className == "Wall") {
			// the target cell doesn't exist, so we are outside the game area
			columnA -= xDirA
			rowA -= yDirA
			getCellA(rowA, columnA).className = "Car"
			xDirA = 0
			yDirA = 0

		} else if (getCellA(rowA, columnA) == getCellB(rowB, columnB)) {
			explode()
		

		} else if (document.getElementById("R" + rowA + "C" + columnA).className == "Goal") {
			coinscollectedA = coinscollectedA + 1
			getCellA(rowA, columnA).className = "Car"
			if (coinscollectedA+coinscollectedB == coinsmax) {
				win()
			}
			coin()
		
			

			

		} else {
	
			getCellA(rowA, columnA).className = "Car"

		if (coinscollectedA+coinscollectedB==coinsmax) {
			win()
		}
			

		
	}
		
	}
	if ((xDirB != 0 || yDirB != 0) && go == true) {
		// Set the cell where the car was to empty
		getCellB(rowB, columnB).className = ""
		
		// Update the column position for the car
		columnB += xDirB
		rowB += yDirB

		
		
		
		// Re-draw the car (or report a crash)
		if (!getCellB(rowB, columnB) || document.getElementById("R" + rowB + "C" + columnB).className == "Wall") {
			// the target cell doesn't exist, so we are outside the game area
			columnB -= xDirB
			rowB -= yDirB
			getCellB(rowB, columnB).className = "CarB"
			xDirB = 0
			yDirB = 0
		} else if (getCellA(rowA, columnA) == getCellB(rowB, columnB)) {
			explode()


		} else if (getCellB(rowB,columnB).className == "Goal") {
			coinscollectedB = coinscollectedB+1
			
			getCellB(rowB,columnB).className = "CarB"
			if (coinscollectedA+coinscollectedB == coinsmax) {
				win()
			}
			coin()
			
			

		} else {
			if (exploded == false) {
			getCellB(rowB,columnB).className = "CarB"
			} else {
				getCellB(rowB,columnB).className = "explode"
			}

		} 
		


	}
	//console.log(coinscollectedA+coinscollectedB)

	if (countdown == 0 && countdown2 == 0) {
		if (go == false) {
			document.getElementById("Message4").innerText = "GO!"
		}
		go = true
		countdown2 -= 1
	} else if (countdown > 0 && countdown2 == 0) {
		document.getElementById("Message4").innerText = countdown
		countdown -= 1
		countdown2 = 4
	} else if (countdown == -2) {
		document.getElementById("Message4").innerText = ""
	} else {
		countdown2 -= 1
	}
	
	if (go == true) {
		if (go2 == 0) {
		document.getElementById("Message4").innerText = ""
		} else {
			go2 -= 1
		}
		
	}


	
			

}
		
	



	


	







function win() {
	if (coinscollectedA > coinscollectedB) {
		window.clearInterval(intervalHandle)
		document.getElementById("Message1").innerText = "P1 WINS!!!"
		getCellA(rowA, columnA).className = "greenwin"
	} else if (coinscollectedB > coinscollectedA) {
		window.clearInterval(intervalHandle)
		document.getElementById("Message1").innerText = "P2 WINS!!!"
		getCellB(rowB, columnB).className = "bluewin"
	}
	winsound()
}
// if the car has gone off the table, this tidies up including crash message
function crashA() {
	window.clearInterval(intervalHandle)
	document.getElementById("Message3").innerText = "Oops player 1 crashed..."
	getCellB(rowB, columnB).className="bluewin"
}



function crashB() {
	window.clearInterval(intervalHandle)
	document.getElementById("Message3").innerText = "Oops player 2 crashed..."
	getCellA(rowA, columnA).className="greenwin"
}

function explode() {
	window.clearInterval(intervalHandle)
	document.getElementById("Message2").innerText = "EXPLODED!!"
	getCellA(rowA, columnA).className="explode"
	getCellB(rowB, columnB).className="explode"
	document.getElementsByClassName("Car").className = "explode"
	document.getElementsByClassName("CarB").className = "explode"
	exploded = true
	death()
}
function start() {
	document.getElementById("start").className = "hidden"
	startsound()
	// when the page loaded...
	$( document ).ready(function() {
		
		runGame();
	});
}

function coin() {
	audio = document.getElementById("coincollect")
	audio.autoplay = true
	audio.load()
}
function death() {
	audio = document.getElementById("death")
	audio.autoplay = true
	audio.load()
}
function winsound() {
	audio = document.getElementById("win")
	audio.autoplay = true
	audio.load()
}

function startsound() {
	audio = document.getElementById("startnoise")
	audio.autoplay = true
	audio.load()
}