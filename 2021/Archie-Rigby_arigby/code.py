#############################
# Library Imports
#############################
from js import document, window

#############################
# Global Variables
#############################

COINSMAX = 73
coinsCollected = 0

# to store movement direction
xDir = 0
yDir = 0

# to store current column position
column = 0
row = 0

# to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 0
carFlipped = False
#############################
# Sub-Programs
#############################

# the function called when a key is pressed - sets direction variable
def checkKey(event):
    global xDir, yDir, CarFlipped
    if event.keyCode == 39:
        # right arrow
        xDir = 1
        yDir = 0
        carFlipped = False
        event.preventDefault()
    elif event.keyCode == 37:
        # left arrow
        xDir = -1
        yDir = 0
        carFlipped = True
        event.preventDefault()
    elif event.keyCode == 38:
        # up arrow
        yDir = -1
        xDir = 0
        event.preventDefault()
    elif event.keyCode == 40:
        # down arrow
        yDir = 1
        xDir = 0
        event.preventDefault()

def getCell():
    return document.getElementById(f"R{row}C{column}")

# the timer check function - runs every 300 milliseconds to update the car position
def updatePosition():
    global column, row
    global carFlipped, coinsCollected
    if xDir != 0 or yDir != 0:
        # Set the cell where the car was to empty
        cell = getCell()
        cell.className = "wall`1    "
        
        # Update the column position for the car
        column += xDir
        row += yDir
        # Re-draw the car (or report a crash)
        cell = getCell()
        if cell and cell.className != "wall":
            if cell.className == "portal":
                if coinsCollected == COINSMAX:
                    handleWin()
            if cell.className == "coin":
                coinsCollected = coinsCollected + 1
                
            #cell.className = "Car"
            
            if carFlipped:
                cell.className = "CarFlip"
            else:
                cell.className = "Car"
        else:
            handleCrash()

# if the car has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)    
    document.getElementById("Message").innerText = "HA YOU CRASHED"

# called when the page is loaded to start the timer checks
def runGame():
    global intervalHandle
    print("you may play the game now")
    document.addEventListener('keydown', checkKey)
    intervalHandle = window.setInterval(updatePosition, 300)
def getCell():
    return document.getElementById(f"R{row}C{column}")

def handleWin():  
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Your bad you still lost you just went into a portal, why did you think that was a good idea?"
#############################
# Main Program
#############################

runGame()
