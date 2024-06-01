#############################
# Library Imports
#############################
from js import document, window

#############################
# Global Variables
#############################
COINSMAX = 5
coinscollected = 0
prev = "Empty"

# to store movement direction
xDir = 0
yDir = 0
# to store current column position
column = 0
row = 0
speed = 500

# to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 0

#############################
# Sub-Programs
#############################

# the function called when a key is pressed - sets direction variable
def checkKey(event):
    event.preventDefault()
    
    global xDir, yDir
    if event.keyCode == 39:
        # right arrow
        xDir = 1
        yDir = 0
    elif event.keyCode == 37:
        # left arrow
        xDir = -1
        yDir = 0
    elif event.keyCode == 38:
        # up arrow
        xDir = 0
        yDir = -1
    elif event.keyCode == 40:
        # down arrow
        xDir = 0
        yDir = 1

def getCell():
    return document.getElementById(f"R{row}C{column}")

# the timer check function - runs every 300 milliseconds to update the car position
def updatePosition():
    global column, row, coinscollected, prev
    if xDir != 0 or yDir != 0:
        # Set the cell where the car was to empty
        cell = getCell()
        cell.className = prev
        
        # Update the column position for the car
        column += xDir
        row += yDir
        # Re-draw the car (or report a crash)
        cell = getCell()
        prev = cell.className
        if not cell:
            handleCrash()
        elif cell.className == "wall":
            handleCrash()
        elif cell.className == "flag":
            handleWin()
        elif cell.className == "bone":
            coinscollected = coinscollected + 1
            prev = "Empty"
        else:
            cell.className = "Car"

    

def handleWin():
    if coinscollected == COINSMAX: 
        window.clearInterval(intervalHandle)
        document.getElementById("Message").innerText = "WELL DONE, YOU'VE WON!"
    else:
        document.getElementById("Message").innerText = "You need to collect all the coins"

# if the car has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Oops you crashed..."

# called when the page is loaded to start the timer checks
def runGame():
    global intervalHandle
    print("Running Game")
    document.addEventListener('keydown', checkKey)
    intervalHandle = window.setInterval(updatePosition, 301)

#############################
# Main Program
#############################

runGame()
