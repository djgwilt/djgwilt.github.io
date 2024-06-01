#############################
# Library Imports
#############################
from js import document, window
from random import randint
#############################
# Global Variables
#############################
FLAGMAX = 2 
FLAGSCOLLECTED = 0
speed = randint(100, 1000)
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

def winGame():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Well done!"
    document.getElementById("winner pic").style.display="block"    
        
# the function called when a key is pressed - sets direction variable
def checkKey(event):
    global xDir, yDir, carFlipped
    if event.keyCode == 39 or event.keyCode == 68:
        # d
        xDir = 1
        yDir = 0
        carFlipped = True
    elif event.keyCode == 37 or event.keyCode == 65:
        # a
        xDir = -1
        yDir = 0
        carFlipped = False
    elif event.keyCode == 38 or event.keyCode == 87:
        # w
        yDir = -1
        xDir = 0
        carFlipped = False
    elif event.keyCode == 40 or event.keyCode == 83:
        # s
        yDir = 1
        xDir = 0
        carFlipped = True
    elif event.keyCode == 32:
        window.location.reload()
def getCell():
    return document.getElementById(f"R{row}C{column}")

# the timer check function - runs every 300 milliseconds to update the car position
def updatePosition():
    global column, row, FLAGSCOLLECTED, FLAGMAX
    if xDir != 0 or yDir !=0:
        # Set the cell where the car was to empty
        cell = getCell()
        cell.className = "road"
        
        # Update the column position for the car
        column += xDir
        row+= yDir
        # Re-draw the car (or report a crash)
        cell = getCell()
        if not cell:
            #gone off grid
            handleCrash()
        elif cell.className ==  "wall":
            handleCrash()
        elif cell.className == "flag":
            cell.className = "Car"
            FLAGSCOLLECTED += 1
            if FLAGSCOLLECTED == FLAGMAX:
                winGame()
        else:
            cell.className = ("CarFlip" if carFlipped else "Car")

# if the car has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Oops you crashed! Reload to try again by pressing the space bara."

# called when the page is loaded to start the timer checks
def runGame():
    global intervalHandle
    print("Let's go!")
    print(f"Your speed in this round is {speed}! Remember the lower the number the faster you go!")
    document.addEventListener('keydown', checkKey)
    intervalHandle = window.setInterval(updatePosition, speed)


#############################
# Main Program
#############################

runGame()
