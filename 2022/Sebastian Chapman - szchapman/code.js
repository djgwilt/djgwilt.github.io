// listen for keypress (to detect arrow keys)
document.onkeydown = checkKey
/*function checkajsq() {
	count = 0
	if (getCell(postionx+tempposx+1, postiony+tempposy).className == "") {
		count += 1
	} else if (getCell(postionx+tempposx-1, postiony+tempposy).className == "" ) {
		count += 1
	} else if (getCell(postionx+tempposx, postiony+tempposy+1).className == "") {
		count += 1
	} else if (getCell(postionx+tempposx, postiony+tempposy-1).className == "") {
		count += 1
	}
}
function generatemaze() {
	for (let i = 0; i < 7; 1++) {
		for (let n = 0; n < 7; 1++) {
			getCell(i, n).className = "wall"
			getCell(i, n).textContent = "mabye this is wall"
		}
	}
	postionx = 0
	postiony = 0
	tempposx = 0
	tempposy = 0
	while (getCell(postionx, postiony-1).className == "wall" | !getCell(postionx, postiony+1).className == "wall" | !getCell(postionx+1, postiony).className == "wall" | !getCell(postionx-1, postiony).className == "wall") {
		random = (int)(Math.random() * 4 + 1)
		next = true
		getCell(postionx)
		tempposx = 0
		tempposy = 0
		getCell(postionx, postiony).className = ""
		while (next) {
			if (random == 1) {
				tempposy = -1
				tempposx = 0
				checkajsq()
				if (!getCell(postionx, postiony) | getCell(postionx,postiony).className == "" | count > 1) {
					random = 2
				} else {
					postionx += tempposx
					postiony += tempposy
					next = false
				}
			}	else if (random == 2) {
				tempposx = 1
				tempposy = 0
				checkajsq()
				if (!getCell(postionx, postiony) | getCell(postionx,postiony).className == "" | count > 1) {
					random = 3
				} else {
					postionx += tempposx
					postiony += tempposy
					next = false
				}
			}	else if (random == 3) {
				tempposy = 1
				tempposx = 0
				checkajsq()
				if (!getCell(postionx, postiony) | getCell(postionx,postiony).className == "" | count > 1) {
					random = 4
				} else {
					postionx += tempposx
					postiony += tempposy
					next = false
				}
			}	else if (random == 4) {
				tempposx = -1
				tempposy = 0
				checkajsq()
				if (!getCell(postionx, postiony) | getCell(postionx,postiony).className == "" | count > 1) {
					random = 1
				} else {
					postionx += tempposx
					postiony += tempposy
					next = false
				}
			}
		}
	}
	
}*/
// to store movement direction
//generatemaze(2)
var xDir = 0
var yDir = 0
// to store current column position
var column = 0
var row = 0
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
}

// called when the page is loaded to start the timer checks
function runGame() {
	intervalHandle = setInterval(updatePosition, 300)
}

function getCell(row, column) {
  return document.getElementById("R" + row + "C" + column)
}

// the timer check function - runs every 300 milliseconds to update the car position
function updatePosition() {
	if (xDir != 0 | yDir != 0) {
		// Set the cell where the car was to empty
		//car = getCell(row, column).className
		getCell(row, column).className = ""
		
		// Update the column position for the car
		column += xDir
		row += yDir
		
		// Re-draw the car (or report a crash)
		if (!getCell(row, column)) {
			// the target cell doesn't exist, so we are outside the game area
			crash()
		} else if (getCell(row, column).className == "wall" | getCell(row, column).className == "hit") {
			crash()
			clash()
		} else if (getCell(row,column).className == "flag") {
			win()
		} else {
			if (xDir == 1) {
				getCell(row, column).className = "Car"
			} else if (xDir == -1) {
				getCell(row, column).className = "Carflip"
			} else if (xDir == 0) {
				getCell(row, column).className = car
			}
		}
		if (stop) {
			xDir = 0
			yDir = 0
		}
	}
}


// if the car has gone off the table, this tidies up including crash message
function crash() {
	window.clearInterval(intervalHandle)
	window.clearInterval(ticking)
	getCell(row, column).className = "explosion"

}

function win() {
	document.getElementById("Message").innerText = "you win"
}
lv = 2
t = 0
stop = true
moving = []
ticking = setInterval(tick, 300)
// when the page loaded...
$( document ).ready(function() {
    runGame();
});

function setline(rowcolumn, num, type) {
	if (rowcolumn == "row") {
		getCell(num, 0).className=type
		getCell(num, 1).className=type
		getCell(num, 2).className=type
		getCell(num, 3).className=type
		getCell(num, 4).className=type
		getCell(num, 5).className=type
		getCell(num, 6).className=type
		getCell(num, 7).className=type
	} else if (rowcolumn == "column") {
		getCell(0, num).className=type
		getCell(1, num).className=type
		getCell(2, num).className=type
		getCell(3, num).className=type
		getCell(4, num).className=type  
		getCell(5, num).className=type
		getCell(6, num).className=type
		getCell(7, num).className=type
	}
}

function moveline(rowcolumn, num, type) {
	currenttick = t
	if (num < 8) {
		if (rowcolumn == "row") {
			getCell(num, 0).className=type
			moving.append(moving.length)
			moving[moving.length-1][0] = num
			moving[moving.length-1][1] = 0
			moving[moving.length-1][1] = "2+"
		} else if (rowcolumn == "column") {
			getCell(0, num).className=type
			moving.append(moving.length)
			moving[moving.length-1][0] = 0
			moving[moving.length-1][1] = num
			moving[moving.length-1][1] = "1+"
		}
	} else {
		if (rowcolumn == "row") {
			getCell(num, 7).className=type
			moving.append(moving.length)
			moving[moving.length-1][0] = num
			moving[moving.length-1][1] = 7
			moving[moving.length-1][1] = "2-"
		} else if (rowcolumn == "column") {
			getCell(7, num).className=type
			moving.append(moving.length)
			moving[moving.length-1][0] = 7
			moving[moving.length-1][1] = num
			moving[moving.length-1][1] = "1-"
		}
	}
}

function tick() {
	if (lv == 2) {
		if (moving[i][2] == "2+") {
			getCell(moving[i][0], moving[i][1]+1) = "hit"
		} else if (moving[i][2] == "2-") {
			getCell(moving[i][0], moving[i][1]-1) = "hit"
		} else if (moving[i][2] == "1+") {
			getCell(moving[i][0]+1, moving[i][1]) = "hit"
		} else if (moving[i][2] == "1-") {
			getCell(moving[i][0]-1, moving[i][1]) = "hit"
		}
		t = t + 1
		document.getElementById("Message").innerText = t
		if (t > 10 && t < 15) {
			setline("column", 4, "warn")
		} else if (t == 15) {
			setline("column", 4, "hit")
		} else if (t == 16) {
			setline("column", 4, "")
		} else if (t > 20 && t < 25) {
			setline("column", 0, "warn")
			setline("column", 2, "warn")
			setline("column", 4, "warn")
			setline("column", 6, "warn")
			setline("row", 0, "warn")
			setline("row", 2, "warn")
			setline("row", 4, "warn")
			setline("row", 6, "warn")
		} else if (t == 25) {
			setline("column", 0, "hit")
			setline("column", 2, "hit")
			setline("column", 4, "hit")
			setline("column", 6, "hit")
			setline("row", 0, "hit")
			setline("row", 2, "hit")
			setline("row", 4, "hit")
			setline("row", 6, "hit")
		} else if (t == 26) {
			setline("column", 0, "")
			setline("column", 2, "")
			setline("column", 4, "")
			setline("column", 6, "")
			setline("row", 0, "")
			setline("row", 2, "")
			setline("row", 4, "")
			setline("row", 6, "")
		} else if (t == 30) {
			//moveline("column", 1, "hit")
		}
	}
	if (getCell(row, column).className == "wall" | getCell(row, column).className == "hit") {
		crash()
		clash()
	}
	getCell(row, column).className = car
}