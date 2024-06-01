#############################
# Library Imports
#############################
from js import document, window

#############################
# Global Variables
#############################

# to store movement direction
xDir = 0
yDir = 0

# to store current column position
column = 0
row = 0

# to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 0

#to store handle code 
interval = 0

#to store car flip
carFlipped = False 

#coins 
COINSMAX = 3 
coinsCollected = 0 

#############################
# Sub-Programs
#############################

# the function called when a key is pressed - sets direction variable
def checkKey(event):
    global xDir, yDir , carFlipped
    if event.keyCode == 39:
        # right arrow
        xDir = 1
        yDir = 0
        carFlipped = True
    elif event.keyCode == 37:
        # left arrow
        xDir = -1
        yDir = 0
        carFlipped = False
    elif event.keyCode == 38:
        # up arrow 
        yDir = -1
        xDir = 0
    elif event.keyCode == 40:
        # down arrow 
        yDir = 1
        xDir = 0

def getCell():
    return document.getElementById(f"R{row}C{column}")

# the timer check function - runs every 300 milliseconds to update the car position
def updatePosition():
    global column, row, coinsCollected, xDir, yDir 
    if xDir != 0 or yDir != 0:
        # Set the cell where the car was to empty
        cell = getCell()
        if cell.id == ("R1C11"):
            cell.className = "flag"
        else:
            cell.className = "Empty"
        
        # Update the column position for the car
        column += xDir
        row += yDir
        # Re-draw the car (or report a crash)
        cell = getCell()
        if not cell:
            handleCrash()
        elif cell.id == ("R4C5"):
            row = 5
            column = 8
            xDir = 0
            yDir = 0
            getCell().className = ("CarFlip" if carFlipped else "Car")
        elif cell.id ==("R4C0"):
            document.getElementById(f"R4C1").className = "wall2"
            document.getElementById(f"R5C1").className = "wall2"
            getCell().className = ("CarFlip" if carFlipped else "Car")
            
        elif cell.className == "wall1":
            handleCrash()
        elif cell.className == "wall2":
            handleCrash()
        elif cell.className == "flag":
            if coinsCollected == COINSMAX:
                handleWin()
            else:
                 cell.className = ("CarFlip" if carFlipped else "Car")
        elif cell.className == "coin":
            coinsCollected = coinsCollected + 1
            cell.className = ("CarFlip" if carFlipped else "Car")
        else: 
            cell.className = ("CarFlip" if carFlipped else "Car")

# if the car has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Oops you crashed..."
    
#  handle win
def handleWin():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "WELL DONE, YOU WIN!"
# called when the page is loaded to start the timer checks
def runGame():
    global intervalHandle
    print("Running Game")
    document.addEventListener('keydown', checkKey)
    intervalHandle = window.setInterval(updatePosition, 300)

#############################
# Main Program
#############################

runGame()
