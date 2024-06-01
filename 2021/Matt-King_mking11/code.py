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

# to store how many coins need to be collected
COINSMAX = 3

# to store how many coins the player has collected
coinsCollected = 0

# to store current row and column position
column = 0
row = 1

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
    global column, row, coinsCollected
    if xDir != 0 or yDir != 0:
        # Set the cell where the car was to empty
        cell = getCell()
        cell.className = "Empty"
        
        # Update the column position for the car
        column += xDir
        row += yDir
        
        # Re-draw the car (or report a crash)
        cell = getCell()
        if not cell:
            # gone off grid
            handleCrash()
        elif cell.className == "coin":
            coinsCollected += 1            
        elif cell.className == "wall1" or cell.className == "wall2":
            handleCrash()
        elif cell.className == "flag" and coinsCollected == COINSMAX:
            handleWin()
        else:
            cell.className = "Car"
        




# if the car has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Oops you crashed..."

def handleWin():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "WELL DONE, YOU'VE WON!"




# called when the page is loaded to start the timer checks
def runGame():
    global intervalHandle
    print("Running Game")
    document.addEventListener('keydown', checkKey)
    intervalHandle = window.setInterval(updatePosition, 250)

#############################
# Main Program
#############################

runGame()
