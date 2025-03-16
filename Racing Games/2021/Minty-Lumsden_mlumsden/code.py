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

coinsmax = 3
coinscollect = 0

# to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 0

# to store car flip (reflection) status
carFlipped = False

#############################
# Sub-Progra
#############################

# the function called when a key is pressed - sets direction variable
def checkKey(event):
    global xDir, yDir, carFlipped
    if event.keyCode == 39:
        # right arrow
        xDir = 1
        yDir = 0
        carFlipped = False
    elif event.keyCode == 37:
        # left arrow
        xDir = -1
        yDir = 0
        carFlipped = True
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
    global column, row, coinscollect
    if xDir != 0 or yDir != 0:
        # Set the cell where the car was to empty
        cell = getCell()
        cell.className = "Empty"
        
        # Update the column position for the car
        column += xDir
        row += yDir
        print(row,column)
        # Re-draw the car (or report a crash)
        cell = getCell()
        if not cell: 
            # gone off grid
            handleCrash()
        elif cell.className == "wall":
            handleCrash()
        elif cell.className == "flag":
            coinscollect =coinscollect + 1
            if coinscollect == coinsmax:
                handleWin()
        else:
            cell.className = ("CarFlip" if carFlipped else "Car")
            
#handle win (flag reached)
def handleWin():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "WELL DONE, YOU'VE WON!"

# if the car has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Oops you crashed..."

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
