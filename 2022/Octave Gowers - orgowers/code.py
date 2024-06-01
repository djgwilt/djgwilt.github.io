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

carFlipped = False
    
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
        carFlipped = False
    elif event.key == "ArrowLeft":
        # left arrow
        xDir = -1
        yDir = 0
        carFlipped = True 
    elif event.key == "ArrowUp":
        xDir = 0
        yDir = -1
    elif event.key == "ArrowDown":
        xDir = 0
        yDir = 1
    event.preventDefault()

def updatePosition():
    global column
    if xDir != 0:
        cell = getCell()
        cell.className = " "
def getCell():
    return document.getElementById(f"R{row}C{column}")
# the timer check function - runs every 300 milliseconds to update the car position
def updatePosition():
    global column, row
    if xDir != 0 or yDir != 0:
        # Set the cell where the car was to empty
        cell = getCell()
        cell.className = ""
        
        # Update the column position for the car
        column += xDir
        row += yDir
        # Re-draw the car (or report a crash)
        cell = getCell()

        if not cell:
            handleCrash()
        elif cell.className == "wall":
            cell.className = "wallCrashed"
            audio = document.getElementById("crashSound")
            audio.autoplay = True
            audio.load()
            handleCrash()
        elif cell.className == "tree":
            handleCrash()
        elif cell.className == "flag":
            audio = document.getElementById("winSound")
            audio.autoplay = True
            audio.load()
            handleWin()
        #elif cell.classname == "":

        elif cell and cell.className != "wall":
             cell.className = "Car"
        else:
            cell.className = ("CarFlip" if carFlipped else "Car")
        

# if the car has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Some of you may die, but that is a sacrifice I am willing to make..."
def handleWin():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "ONIONS HAVE LAYERS"

# called when the page is louaded to start the timer checks
def runGame():
    global intervalHandle
    print("Running Game")
    document.addEventListener('keydown', checkKey)
    intervalHandle = window.setInterval(updatePosition, 300)
    



#############################
# Main Program
#############################

runGame()
