
document.onkeydown = checkKey

var xDir = 0
var yDir = 0
var flagCount = 0
var flagMax = 2

var column = 0
var row = 0


var intervalHandle

var rabbitClass = "rabbit"

function checkKey(e) {
  
    e = e || window.event

    if (e.keyCode == '39') {
      
	    xDir = 1
        yDir = 0
        rabbitClass = "rabbit"
    } else if (e.keyCode == '37') {
    
	    xDir = -1
        yDir = 0
        rabbitClass = "rabbitFlip"
    } else if (e.keyCode == '38') {
        
	    yDir = -1
        xDir = 0
    } else if (e.keyCode == '40') {
        
	    yDir = 1
        xDir = 0
    }
}


function runGame() {
	intervalHandle = setInterval(updatePosition, 300)
}


function updatePosition() {
	if (xDir != 0 || yDir != 0) {
        
		document.getElementById("r" + row + " c" + column).className = "Empty"
        
		column += xDir;
        row += yDir; 
      
		if (handleEnd() == false) {
            document.getElementById("r" + row + " c" + column).className = rabbitClass;
		}
	}
    
}
    
function handleEnd()
{
    if (!document.getElementById("r" + row + " c" + column)|| document.getElementById("r" + row + " c" + column).className == "wall") { 
	handleCrash();
    return true;
  } else if(document.getElementById("r" + row + " c" + column).className == "flag")   
  {
     handleWin();
     return true;
   }   
   return false;
          
}


function handleCrash() {
	window.clearInterval(intervalHandle);
	document.getElementById("Message").innerText = "Oops you crashed..."
}

function handleWin() {
    flagCount++
    if (flagCount == flagMax){
        window.clearInterval(intervalHandle);
        document.getElementById("Message").innerText = "WELL DONE YOU WIN!!!";
    }
}