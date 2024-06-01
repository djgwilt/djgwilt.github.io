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
carDirection = "right"
# to store current column position
column = 0
row = 0

# to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 0

#############################
# Sub-Programs
#############################

# the function called when a key is pressed - sets direction variable
def checkKey(event):
    global xDir
    global yDir
    global carDirection
    if event.keyCode == 39:
        # right arrow
        xDir = 1
        yDir = 0
        carDirection = "right"
    elif event.keyCode == 37:
        # left arrow
        xDir = -1
        yDir = 0
        carDirection = "left"
    elif event.keyCode == 38:
        yDir = -1
        xDir = 0
    elif event.keyCode == 40:
        yDir = 1
        xDir = 0
        
    elif event.keyCode == 68:
        # right arrow
        xDir = 1
        yDir = 0
        carDirection = "right"
    elif event.keyCode == 65:
        # left arrow
        xDir = -1
        yDir = 0
        carDirection = "left"
    elif event.keyCode == 87:
        yDir = -1
        xDir = 0
    elif event.keyCode == 83:
        yDir = 1
        xDir = 0
    event.preventDefault()

def getCell():
    return document.getElementById(f"R{row}C{column}")

# the timer check function - runs every 300 milliseconds to update the car position
def updatePosition():
    global column
    global row
    if xDir != 0 or yDir != 0:
        # Set the cell where the car was to empty
        cell = getCell()
        cell.className = "Empty"
        
        # Update the column position for the car
        column += xDir
        row += yDir
        # Re-draw the car (or report a crash)
        cell = getCell()
        if not cell or cell.className == "wall":
            handleCrash()
        elif cell.className == "invis":
            handleCrash()
        elif cell.className == "checkpoint":
            doorcell = checkpointcell()
            doorcell.className = "empty"
        elif cell.className == "flag":
            handleWin()
        elif cell:
            if carDirection == "right":
                cell.className = "Car_right"
            elif carDirection == "left":
                cell.className = "Car_left"


# if the car has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Dman bro ur kinda bad ngl"
def handleWin():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "poggers"
    
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
