#############################
# Library Imports
#############################
from js import document, window

#############################
# Global Variables
#############################

# Number of Flags
FlagsMax = 4
FlagsCollected = 0

# to store movement direction
xDir = 0
yDir = 0

# to store current column position
column = 0
row = 0

# to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 0
# to score car flip(reflection) status
carFlipped = False


#############################
# Sub-Programs
#############################


# the function called when a key is pressed - sets direction variable
def checkKey(event):
    global xDir, carFlipped, yDir
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
        #up Arrow
        xDir = 0
        yDir = -1
    elif event.keyCode == 40:
        #down arrow
        xDir = 0
        yDir = 1

def getCell():
    return document.getElementById(f"R{row}C{column}")

# the timer check function - runs every 300 milliseconds to update the car position
def updatePosition():
    global column, row, FlagsCollected
    if xDir != 0 or yDir!=0:
        # Set the cell where the car was to empty
        cell = getCell()
        cell.className = "Empty"
        
        # Update the column position for the car
        column += xDir
        row += yDir
        # Re-draw the car (or report a crash)
        cell = getCell()
        if cell and cell.className == "wall" or not cell:
            handleCrash()
        elif cell and cell.className == "flag":
            cell.className = "Car"
            FlagsCollected+=1
            if FlagsCollected == FlagsMax:
                handleWin()
        else:
            cell.className = ("CarFlip" if carFlipped else "Car")

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

# handle Win (flag reached)
def handleWin():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Good Job, You finished the race"
    
#############################
# Main Program
#############################

runGame()
