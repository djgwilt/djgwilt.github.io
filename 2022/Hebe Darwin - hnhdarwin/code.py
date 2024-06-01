#############################
# Library Imports
#############################
from sqlite3 import Row
from js import document, window

#############################
# Global Variables
#############################

# to store movement direction
xDir = 0
score = 0
# to store current column position
column = 0

# to store the direction vertically
yDir = 0 
# to store current row position
height = 0

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
        yDir = 0
    elif event.key == "ArrowLeft":
        # left arrow
        xDir = -1
        yDir = 0
    elif event.key == "ArrowUp":
        yDir = -1
        xDir = 0
    elif event.key == "ArrowDown":
        yDir = 1
        xDir = 0


def getCell():
    return document.getElementById(f"R0C{column}")

# the timer check function - runs every 300 milliseconds to update the car position
def updatePosition():
    global column, score
    if xDir != 0:
        # Set the cell where the car was to empty
        cell = getCell()
        cell.className = ""
        # Update the column position for the car
        column += xDir
        # Re-draw the car (or reporst a crash)
        cell = getCell()
        if cell:
            score = score + 1
            cell.className = "Car"
        else:
            handleCrash()
# if the car has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Oops you crashed..."
    print(f"You got {score} points! Well Done! \n Can you do better next time? Press Refresh to find out.")
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
