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
column = 22
row = 14
# to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 0

#############################
# Sub-Programs
#############################

# the function called when a key is pressed - sets direction variable
def checkKey(event):
    global xDir, yDir
    event.preventDefault()
    if event.key == "ArrowRight":
        xDir = 1
        yDir = 0
    elif event.key == "ArrowLeft":
        # left arrow
        xDir = -1
        yDir = 0
    elif event.key == "ArrowUp":
        xDir = 0
        yDir = -1
    elif event.key == "ArrowDown":
        xDir = 0
        yDir = 1

def getCell():
    return document.getElementById(f"R{row}C{column}")


# the timer check function - runs every 300 milliseconds to update the car position
def updatePosition():
    global column, row
    if xDir != 0 or yDir != 0:
        # Set the cell where the car was to empty
        cell = getCell()
        if "tarmac" in cell.className:
            cell.className = "tarmac"
        else:
            cell.className = ""
        
        # Update the column position for the car
        column += xDir
        row += yDir
        # Re-draw the car (or report a crash)
        cell = getCell()
        if cell.className == 'trophy':
            document.getElementById("Message").innerText = "Handle win"
            handleWin()
        elif cell and cell.className != "wall":
            if "tarmac" in cell.className:
                cell.className = "Car tarmac"
        else:
            handleCrash()

# if the car has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Verstappen wins again!"

#handle win (flag reached)
def handleWin():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "You are the champion"
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
