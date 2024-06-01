// listen for keypress (to detect arrow keys)
document.onkeydown = checkKey

// to store movement direction
var xDir = 0
var yDir = 0

// moving obstacle


// to store current column position
var row = 8
var column = 5
var score = 0
var numb = 200
var show = 0
// to store the handle code for the timer interval to cancel it when we crash
var intervalHandle
var score = 0 
// the function called when a key is pressed - sets direction variable
function checkKey(e) {
	// for all keys, see https://developer.mozilla.org/en-US/docs/Web/API/UI_Events/Keyboard_event_key_values
	if (e.key == "ArrowRight") {
		xDir = 1
		
	}else if (e.key == "ArrowLeft") {
		xDir = -1
		
	}
	e.preventDefault()

}
function easy() {
	numb = 250;
	document.getElementById("speed").innerText = numb
}
function medium() {
	numb = 200;
	document.getElementById("speed").innerText = numb
}
function hard() {
	numb = 150;
	document.getElementById("speed").innerText = numb
}

function win() {
	window.clearInterval(intervalHandle)
	document.getElementById("Message").innerText = "Well done you won"
}

// called when the page is loaded to start the timer checks
function runGame() {
	if (numb == 150) {
		intervalHandle = setInterval(updatePosition, 150);
		
	} else if (numb == 200){
		intervalHandle = setInterval(updatePosition, 200);
		
	} else if (numb == 250) {
		intervalHandle = setInterval(updatePosition, 250);
		
	}
	for (let i = 0; i < 15; i++) {
		audio1 = document.getElementById("music")
		audio1.autoplay = true
		audio1.load()
		audio1.volume = 0.7;
		audio1.playbackRate = 1.5;
	}
	
	
	
	// audio.play()
	
	
}

function getCell(row, column) {
  return document.getElementById("R" + row + "C" + column)
}

// the timer check function - runs every 300 milliseconds to update the car position
function updatePosition() {
	
	obsupdatePosition();
	obsupdatePosition2();
	obsupdatePosition3();
	obsupdatePosition4();
	obsupdatePosition5();
	obsupdatePosition6();
	obsupdatePosition7();
	show = 0
	if (xDir != 0) {
		// Set the cell where the car was to empty
		getCell(row, column).className = ""
		
		// Update the column position for the car
		column += xDir
		xDir = 0
		// Re-draw the car (or report a crash)	
	}

	let cell = getCell(row,column)
	if (!cell || cell.className == "Wall2"){
		crash()
		
		cell.className = "Wall2"
	}
	
		else {
		cell.className = "Car"
	}

	
}



// if the car has gone off the table, this tidies up including crash message
function crash() {
	window.clearInterval(intervalHandle)
	document.getElementById("Message").innerText = "Game over!"
	document.getElementById("Final").innerText ="You got " + score
	score = 0
	audio = document.getElementById("crasho")
	audio.autoplay = true
	audio.load()
	audio1.pause()
	
	
}

var obrow = 0
var obcolumn = 4
var a = 0
var b = 0
var c = 0
var w = Math.floor(Math.random() * 2)
function obsupdatePosition() {
	
	
	// Set the cell where the car was to empty
	
	getCell(obrow, 0).className = ""
	getCell(obrow, 1).className = ""
	getCell(obrow, 2).className = ""
	getCell(obrow, 3).className = ""
	getCell(obrow, 4).className = ""
	getCell(obrow, 5).className = ""
	getCell(obrow, 6).className = ""
	getCell(obrow, 7).className = ""
	getCell(obrow, 8).className = ""
	getCell(obrow, 9).className = ""
	
	
	// Update the column position for the car
	obrow += 1
	if (obrow > 8) {
		score+= 1
		w = Math.floor(Math.random() * 2);
		
		
		obrow = 0
		document.getElementById("Score").innerText = score
		
		
	}
	
	// Re-draw the car (or report a crash)
	let cell1 = getCell(obrow,obcolumn)
	/*if (cell1.className == "Car"){
		
		crash()
	}else{
		cell1.className = "Coin"
	}*/
	getCell(obrow, 0).className = "Wall2"
	getCell(obrow, 1).className = "Wall2"
	getCell(obrow, 2).className = "Wall2"
	getCell(obrow, 3).className = "Wall2"
	getCell(obrow, 4).className = "Wall2"
	getCell(obrow, 5).className = "Wall2"
	getCell(obrow, 6).className = "Wall2"
	getCell(obrow, 7).className = "Wall2"
	getCell(obrow, 8).className = "Wall2"
	getCell(obrow, 9).className = "Wall2"
	getCell(obrow,obcolumn -1).className = ""
	cell1.className = ""
	getCell(obrow,obcolumn + 1).className = ""
	getCell(obrow,obcolumn + 2).className = ""
	
	
}



var obrow2 = -1
var obcolumn2 = 4
function obsupdatePosition2() {
	
	
	// Set the cell where the car was to empty
	if (obrow2 >= 0 ){
		
	
		getCell(obrow2, 0).className = ""
		getCell(obrow2, 1).className = ""
		getCell(obrow2, 2).className = ""
		getCell(obrow2, 3).className = ""
		getCell(obrow2, 4).className = ""
		getCell(obrow2, 5).className = ""
		getCell(obrow2, 6).className = ""
		getCell(obrow2, 7).className = ""
		getCell(obrow2, 8).className = ""
		getCell(obrow2, 9).className = ""
		
		
		
		// Update the column position for the car
		obrow2 += 1
		if (obrow2 > 8) {
			w2 = Math.floor(Math.random() * 3);
			if (w2== 1) {
				obcolumn2 = obcolumn - 1
			} else if (w2 == 2) {
				obcolumn2 = obcolumn + 1
			} else {
				obcolum2 = obcolumn 
			}
			
			obrow2 = 0
			document.getElementById("Score").innerText = score
			
			
		}
		
		// Re-draw the car (or report a crash)
		let cell2 = getCell(obrow2,obcolumn2)
		/*if (cell1.className == "Car"){
			
			crash()
		}else{
			cell1.className = "Coin"
		}*/
		getCell(obrow2, 0).className = "Wall2"
		getCell(obrow2, 1).className = "Wall2"
		getCell(obrow2, 2).className = "Wall2"
		getCell(obrow2, 3).className = "Wall2"
		getCell(obrow2, 4).className = "Wall2"
		getCell(obrow2, 5).className = "Wall2"
		getCell(obrow2, 6).className = "Wall2"
		getCell(obrow2, 7).className = "Wall2"
		getCell(obrow2, 8).className = "Wall2"
		getCell(obrow2, 9).className = "Wall2"
		getCell(obrow2,obcolumn2 -1).className = ""
		cell2.className = ""
		getCell(obrow2,obcolumn2 + 1).className = ""
		getCell(obrow2,obcolumn2 + 2).className = ""
	}
	else {
		obrow2 += 1
	}
	
	
}


var obrow3 = -2
var obcolumn3 = 4
function obsupdatePosition3() {
	
	
	// Set the cell where the car was to empty
	if (obrow3 >= 0 ){
		
	
		getCell(obrow3, 0).className = ""
		getCell(obrow3, 1).className = ""
		getCell(obrow3, 2).className = ""
		getCell(obrow3, 3).className = ""
		getCell(obrow3, 4).className = ""
		getCell(obrow3, 5).className = ""
		getCell(obrow3, 6).className = ""
		getCell(obrow3, 7).className = ""
		getCell(obrow3, 8).className = ""
		getCell(obrow3, 9).className = ""
		
		
		
		// Update the column position for the car
		obrow3 += 1
		if (obrow3 > 8) {
			w3 = Math.floor(Math.random() * 3);
			if (w3== 1) {
				obcolumn3 = obcolumn2 - 1
			} else if (w3 == 2) {
				obcolumn3 = obcolumn2 + 1
			} else {
				obcolum3 = obcolumn2
			}
			
			obrow3 = 0
			document.getElementById("Score").innerText = score
			
			
		}
		
		// Re-draw the car (or report a crash)
		let cell3 = getCell(obrow3,obcolumn3)
		/*if (cell1.className == "Car"){
			
			crash()
		}else{
			cell1.className = "Coin"
		}*/
		getCell(obrow3, 0).className = "Wall2"
		getCell(obrow3, 1).className = "Wall2"
		getCell(obrow3, 2).className = "Wall2"
		getCell(obrow3, 3).className = "Wall2"
		getCell(obrow3, 4).className = "Wall2"
		getCell(obrow3, 5).className = "Wall2"
		getCell(obrow3, 6).className = "Wall2"
		getCell(obrow3, 7).className = "Wall2"
		getCell(obrow3, 8).className = "Wall2"
		getCell(obrow3, 9).className = "Wall2"
		getCell(obrow3,obcolumn3 -1).className = ""
		cell3.className = ""
		getCell(obrow3,obcolumn3 + 1).className = ""
		getCell(obrow3,obcolumn3 + 2).className = ""
	}
	else {
		obrow3 += 1
	}
	
	
}

var obrow4 = -3
var obcolumn4 = 4
function obsupdatePosition4() {
	
	
	// Set the cell where the car was to empty
	if (obrow4 >= 0 ){
		
	
		getCell(obrow4, 0).className = ""
		getCell(obrow4, 1).className = ""
		getCell(obrow4, 2).className = ""
		getCell(obrow4, 3).className = ""
		getCell(obrow4, 4).className = ""
		getCell(obrow4, 5).className = ""
		getCell(obrow4, 6).className = ""
		getCell(obrow4, 7).className = ""
		getCell(obrow4, 8).className = ""
		getCell(obrow4, 9).className = ""
		
		
		
		// Update the column position for the car
		obrow4 += 1
		if (obrow4 > 8) {
			w4 = Math.floor(Math.random() * 3);
			if (w4== 1) {
				obcolumn4 = obcolumn3 - 1
			} else if (w4 == 2) {
				obcolumn4 = obcolumn3 + 1
			} else {
				obcolum4 = obcolumn3
			}
			
			obrow4 = 0
			document.getElementById("Score").innerText = score
			
			
		}
		
		// Re-draw the car (or report a crash)
		let cell4 = getCell(obrow4,obcolumn4)
		/*if (cell1.className == "Car"){
			
			crash()
		}else{
			cell1.className = "Coin"
		}*/
		getCell(obrow4, 0).className = "Wall2"
		getCell(obrow4, 1).className = "Wall2"
		getCell(obrow4, 2).className = "Wall2"
		getCell(obrow4, 3).className = "Wall2"
		getCell(obrow4, 4).className = "Wall2"
		getCell(obrow4, 5).className = "Wall2"
		getCell(obrow4, 6).className = "Wall2"
		getCell(obrow4, 7).className = "Wall2"
		getCell(obrow4, 8).className = "Wall2"
		getCell(obrow4, 9).className = "Wall2"
		getCell(obrow4,obcolumn4 -1).className = ""
		cell4.className = ""
		getCell(obrow4,obcolumn4 + 1).className = ""
		getCell(obrow4,obcolumn4 + 2).className = ""
	}
	else {
		obrow4 += 1
	}
	
	
}
var obrow5 = -4
var obcolumn5 = 4
function obsupdatePosition5() {
	
	
	// Set the cell where the car was to empty
	if (obrow5 >= 0 ){
		
	
		getCell(obrow5, 0).className = ""
		getCell(obrow5, 1).className = ""
		getCell(obrow5, 2).className = ""
		getCell(obrow5, 3).className = ""
		getCell(obrow5, 4).className = ""
		getCell(obrow5, 5).className = ""
		getCell(obrow5, 6).className = ""
		getCell(obrow5, 7).className = ""
		getCell(obrow5, 8).className = ""
		getCell(obrow5, 9).className = ""
		
		
		
		// Update the column position for the car
		obrow5 += 1
		if (obrow5 > 8) {
			w5 = Math.floor(Math.random() * 3);
			if (w5== 1) {
				obcolumn5 = obcolumn4 - 1
			} else if (w5 == 2) {
				obcolumn5 = obcolumn4 + 1
			} else {
				obcolum5 = obcolumn4
			}
			
			obrow5 = 0
			document.getElementById("Score").innerText = score
			
			
		}
		
		// Re-draw the car (or report a crash)
		let cell5 = getCell(obrow5,obcolumn5)
		/*if (cell1.className == "Car"){
			
			crash()
		}else{
			cell1.className = "Coin"
		}*/
		getCell(obrow5, 0).className = "Wall2"
		getCell(obrow5, 1).className = "Wall2"
		getCell(obrow5, 2).className = "Wall2"
		getCell(obrow5, 3).className = "Wall2"
		getCell(obrow5, 4).className = "Wall2"
		getCell(obrow5, 5).className = "Wall2"
		getCell(obrow5, 6).className = "Wall2"
		getCell(obrow5, 7).className = "Wall2"
		getCell(obrow5, 8).className = "Wall2"
		getCell(obrow5, 9).className = "Wall2"
		getCell(obrow5,obcolumn5 -1).className = ""
		cell5.className = ""
		getCell(obrow5,obcolumn5 + 1).className = ""
		getCell(obrow5,obcolumn5 + 2).className = ""
	}
	else {
		obrow5 += 1
	}
	
	
}


var obrow6 = -5
var obcolumn6 = 4
function obsupdatePosition6() {
	
	
	// Set the cell where the car was to empty
	if (obrow6 >= 0 ){
		
	
		getCell(obrow6, 0).className = ""
		getCell(obrow6, 1).className = ""
		getCell(obrow6, 2).className = ""
		getCell(obrow6, 3).className = ""
		getCell(obrow6, 4).className = ""
		getCell(obrow6, 5).className = ""
		getCell(obrow6, 6).className = ""
		getCell(obrow6, 7).className = ""
		getCell(obrow6, 8).className = ""
		getCell(obrow6, 9).className = ""
		
		
		
		// Update the column position for the car
		obrow6 += 1
		if (obrow6 > 8) {
			w6 = Math.floor(Math.random() * 3);
			if (w6== 1) {
				obcolumn6 = obcolumn5 - 1
			} else if (w6 == 2) {
				obcolumn6 = obcolumn5 + 1
			} else {
				obcolum6 = obcolumn5
			}
			
			obrow6 = 0
			document.getElementById("Score").innerText = score
			
			
		}
		
		// Re-draw the car (or report a crash)
		let cell6 = getCell(obrow6,obcolumn6)
		/*if (cell1.className == "Car"){
			
			crash()
		}else{
			cell1.className = "Coin"
		}*/
		getCell(obrow6, 0).className = "Wall2"
		getCell(obrow6, 1).className = "Wall2"
		getCell(obrow6, 2).className = "Wall2"
		getCell(obrow6, 3).className = "Wall2"
		getCell(obrow6, 4).className = "Wall2"
		getCell(obrow6, 5).className = "Wall2"
		getCell(obrow6, 6).className = "Wall2"
		getCell(obrow6, 7).className = "Wall2"
		getCell(obrow6, 8).className = "Wall2"
		getCell(obrow6, 9).className = "Wall2"
		getCell(obrow6,obcolumn6 -1).className = ""
		cell6.className = ""
		getCell(obrow6,obcolumn6 + 1).className = ""
		getCell(obrow6,obcolumn6 + 2).className = ""
	}
	else {
		obrow6 += 1
	}
	
	
}
var obrow7 = -6
var obcolumn7 = 4
function obsupdatePosition7() {
	
	
	// Set the cell where the car was to empty
	if (obrow7 >= 0 ){
		
	
		getCell(obrow7, 0).className = ""
		getCell(obrow7, 1).className = ""
		getCell(obrow7, 2).className = ""
		getCell(obrow7, 3).className = ""
		getCell(obrow7, 4).className = ""
		getCell(obrow7, 5).className = ""
		getCell(obrow7, 6).className = ""
		getCell(obrow7, 7).className = ""
		getCell(obrow7, 8).className = ""
		getCell(obrow7, 9).className = ""
		
		
		
		// Update the column position for the car
		obrow7 += 1
		if (obrow7 > 8) {
			w7 = Math.floor(Math.random() * 3);
			if (w7== 1) {
				obcolumn7 = obcolumn6 - 1
			} else if (w7 == 2) {
				obcolumn7 = obcolumn6 + 1
			} else {
				obcolum7 = obcolumn6
			}
			
			obrow7 = 0
			document.getElementById("Score").innerText = score
			
			
		}
		
		// Re-draw the car (or report a crash)
		let cell7 = getCell(obrow7,obcolumn7)
		/*if (cell1.className == "Car"){
			
			crash()
		}else{
			cell1.className = "Coin"
		}*/
		getCell(obrow7, 0).className = "Wall2"
		getCell(obrow7, 1).className = "Wall2"
		getCell(obrow7, 2).className = "Wall2"
		getCell(obrow7, 3).className = "Wall2"
		getCell(obrow7, 4).className = "Wall2"
		getCell(obrow7, 5).className = "Wall2"
		getCell(obrow7, 6).className = "Wall2"
		getCell(obrow7, 7).className = "Wall2"
		getCell(obrow7, 8).className = "Wall2"
		getCell(obrow7, 9).className = "Wall2"
		getCell(obrow7,obcolumn7 -1).className = ""
		cell7.className = ""
		getCell(obrow7,obcolumn7 + 1).className = ""
		getCell(obrow7,obcolumn7 + 2).className = ""
	}
	else {
		obrow7 += 1
	}
	
	
}
function start() {
	// when the page loaded...
	$( document ).ready(function() {
		runGame()
		
	});
}
