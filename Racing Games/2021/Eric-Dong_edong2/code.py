#############################
# Library Imports
#############################
from js import document, window

#############################
# Global Variables
#############################
coinCollected = 0
MaxCoin = 12
# to store movement direction
xDir = 0
yDir = 0
# to store current column position
column = 0
row = 0
# to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 10
CarFlipped = False
#############################
# Sub-Programs
#############################

# the function called when a key is pressed - sets direction variable
def checkKey(event):
    global xDir, CarFlipped, yDir
    if event.keyCode == 39:
        # right arrow
        xDir = 1
        yDir = 0
        CarFlipped = False
    elif event.keyCode == 37:
        # left arrow
        xDir = -1
        yDir = 0
        CarFlipped = True
    elif event.keyCode == 38:
        xDir = 0
        yDir = -1
    elif event.keyCode == 40:
        xDir = 0
        yDir = 1
def getCell():
    return document.getElementById(f"R{row}C{column}")

# the timer check function - runs every 300 milliseconds to update the car position
def updatePosition():
    global column, row, coinCollected
    if xDir != 0 or yDir!= 0: 
        # Set the cell where the car was to empty
        cell = getCell()
        cell.className = "Empty"
        
        # Update the column position for the car
        column += xDir
        row += yDir
        # Re-draw the car (or report a crash)
        cell = getCell()
        if not cell:
            handleCrash()
        elif cell.className == "wall":
            handleCrash()
        elif cell.className == "flag":
            coinCollected = coinCollected + 1
            if coinCollected == MaxCoin:
                handleWin()
            cell.className = ("CarFlipped" if CarFlipped else "Car")    
        else:
            cell.className = ("CarFlipped" if CarFlipped else "Car")
            
def handleWin():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Great job! Thank you for helping this little guy get his lunch!"
    
# if the car has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Why did you just hop into a tree..."

# called when the page is loaded to start the timer checks
def runGame():
    global intervalHandle
    print("Running Game")
    document.addEventListener('keydown', checkKey)
    intervalHandle = window.setInterval(updatePosition, 280)

#############################
# Main Program
#############################

runGame()
