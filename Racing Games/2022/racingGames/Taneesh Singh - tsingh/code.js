const output = document.getElementById("output");

document.onkeydown = checkKey

 

// to store movement direction

var xDir = 0

var yDir = 0

 

// to store current column position

var column = 0

var row = 0

// to store the handle code for the timer interval to cancel it when we crash

var intervalHandle

var time = 0

 

// the function called when a key is pressed - sets direction variable

function checkKey(e) {

    // for all keys, see https://developer.mozilla.org/en-US/docs/Web/API/UI_Events/Keyboard_event_key_values

    if (e.key == "ArrowRight") {

        xDir = 1

        yDir = 0

    } else if (e.key == "ArrowLeft") {

        xDir = -1

        yDir = 0

    } else if (e.key == "ArrowDown") {

        yDir = 1

        xDir = 0

    } else if (e.key == "ArrowUp") {
        yDir = -1
        xDir = 0
    }

}

 

// called when the page is loaded to start the timer checks

function runGame() {
    
    intervalHandle = setInterval(updatePosition, 300)

}

 

function getCell(row, column) {

  return document.getElementById("r" + row + " c" + column)

}

 

// the timer check function - runs every 300 milliseconds to update the car position

function updatePosition() {
    time += 0.3
    if (Math.round(time/4) == Math.ceil(time/4)) {
        getCell(2, 5).className = "ghost"
    } else {
        getCell(2, 5).className = ""
    }

    if (Math.round(time/2) == Math.ceil(time/2)) {
        getCell(4, 2).className = "ghost2"
    } else {
        getCell(4, 2).className = ""
    }

    if (Math.round(time/3) == Math.ceil(time/3)) {
        getCell(6, 7).className = "ghost1"
    } else {
        getCell(6, 7).className = ""
    }

    if (Math.round(time/1.7) == Math.ceil(time/1.7)) {
        getCell(8, 2).className = "ghost3"
    } else {
        getCell(8, 2).className = ""
    }

    if (xDir != 0 || yDir != 0)  {

        // Set the cell where the car was to empty

        getCell(row, column).className = ""

       

        // Update the column position for the car

        column += xDir

        row += yDir

        let cell = getCell(row, column) 

        // Re-draw the car (or report a crash)

       


        if (!cell || cell.className == "ghost" || cell.className == "wall" || cell.className == "ghost1" || cell.className == "ghost2" || cell.className == "ghost3") {
            crash()
        } else if ( cell.className == "Chest") {
            handlewin();
         } else if (carFlipped)  {
            cell.className = "carFlipped"
        }  else{
            cell.className = "Car"
        }              
    }
}





 

// if the car has gone off the table, this tidies up including crash message

function crash() {

    window.clearInterval(intervalHandle)

    document.getElementById("Message").innerText = "Oops you crashed..."

}

function handlewin() {

    window.clearInterval(intervalHandle)

    document.getElementById("Message").innerText = "Congratulations, you won!!"

}

var intervalHandle

var carFlipped = false

function checkKey (e) {
    if(e.key == "ArrowRight") {
        xDir = 1
        yDir = 0 
        carFlipped = false 
    }else if (e.key == "ArrowLeft") {
        xDir = -1
        yDir = 0 
        carFlipped = true
    }else if (e.key == "ArrowUp") {
        xDir = 0
        yDir = -1 
        carinverted = true
    }else if (e.key == "ArrowDown") {
        xDir = 0
        yDir = 1
        carinverted = true       


    } 
     
}

 







