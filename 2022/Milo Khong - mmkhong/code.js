// listen for keypress (to detect arrow keys)
var score=0
document.onkeydown = checkKey

// to store movement direction
var xDir = 0
var yDir=0
// to store current column position
var column = 0
var row=0

// to store the handle code for the timer interval to cancel it when we crash
var intervalHandle

var carClass = "Car"

var USAClass ='flag'
var au_exp = new Audio('au_exp.mp3');
var fail = new Audio('fail.mp3')
var plane_exp = new Audio('warplane_des.mp3.mp3')

var speed=200




// the function called when a key is pressed - sets direction variable
function checkKey(e) {
	// for all keys, see https://developer.mozilla.org/en-US/docs/Web/API/UI_Events/Keyboard_event_key_values
	if (e.key == "ArrowRight") {
		xDir = 1
		yDir=0
		carClass="Car"
	} else if (e.key == "ArrowLeft") {
		xDir = -1
		yDir=0
		carClass="CarL"
	}else if (e.key=="ArrowUp") {
		yDir = -1
		xDir= 0
		carClass="CarU"
	}else if (e.key=="ArrowDown") {
		yDir = 1
		xDir= 0
		carClass="CarD"
	}
}

// called when the page is loaded to start the timer checks
function runGame() {
	intervalHandle = setInterval(updatePosition, speed)
}

function getCell(row, column) {
  return document.getElementById("R" + row + "C" + column)
}



// the timer check function - runs every 300 milliseconds to update the car position
function updatePosition() {
	if (xDir != 0 || yDir!=0) {
		// Set the cell where the car was to empty
		getCell(row, column).className = ""
		
		// Update the column position for the car
		column += xDir
		row+=yDir
		
		// Re-draw the car (or report a crash)
		if (!getCell(row, column) || getCell(row,column).className==='wall') {
			if (!getCell(row, column)){
				crash2()
			}
			crash()
			// the target cell doesn't exist, so we are outside the game area
			getCell(row,column).className="destroyed"

	
		}else if(getCell(row, column).className=="flag"){
			win()
		}else if(getCell(row ,column).className=="warplane"){
			score+=10
			plane_exp.play()
			document.getElementById("score").innerText = `Score: ${score}/140 Social Credits`
			if(xDir==1){
				getCell(row, column).className="Car"
			}
			else if(xDir==-1){
				getCell(row, column).className="CarL"
			}
			else if(yDir==-1){
				getCell(row, column).className="CarU"
			}
			else{
				getCell(row, column).className="CarD"
			}
			
		}
		else {
			getCell(row, column).className = carClass
		}
	}

}

// if the car has gone off the table, this tidies up including crash message



function crash() {
	fail.play()
	window.clearInterval(intervalHandle)
	document.getElementById("Message").innerText = "You have nuked an allied chinese army. Supreme Leader is Disapointed!"

}
function win() {

	window.clearInterval(intervalHandle)
	au_exp.play();
	USAClass = 'flag_ex'
	score+=100
	getCell(row, column).className = USAClass
	document.getElementById("Message").innerText = 'You have nuked the United States of America! Good Job!'
	
	document.getElementById("lv").innerText = 'Progress to next level'
	



	var path = window.location.pathname;
	var page = path.split("/").pop();
	if (page=='lv3.html'){
		document.getElementById("score").innerText = `Score: ${score}/40 Social Credits`
	}


}
function crash2(){
	fail.play()
	window.clearInterval(intervalHandle)
	document.getElementById("Message").innerText = "You have crashed your nuclear bomb into the Korean Ocean. Supreme Leader is Disapointed!"
}

// when the page loaded...
$( document ).ready(function() {
    runGame();
});

