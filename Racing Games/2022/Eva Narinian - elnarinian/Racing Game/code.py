#############################
# Library Imports
#############################
from js import document, window

#############################
# Global Variables
#############################

# to store movement direction
xDir = 0

# to store current column position
column = 0

# to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 0

#############################
# Sub-Programs
#############################

# the function called when a key is pressed - sets direction variable
def checkKey(event):
    global xDir
    event.preventDefault()
    if event.key == "ArrowRight":
        xDir = 1
    elif event.key == "ArrowLeft":
        # left arrow
        xDir = -1

def getCell():
    return document.getElementById(f"R0C{column}")

# the timer check function - runs every 300 milliseconds to update the car position
def updatePosition():
    global column
    if xDir != 0:
        # Set the cell where the car was to empty
        cell = getCell()
        cell.className = ""
        
        # Update the column position for the car
        column += xDir
        # Re-draw the car (or report a crash)
        cell = getCell()
        if cell:
            cell.className = "Car"
        else:
            handleCrash()

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
