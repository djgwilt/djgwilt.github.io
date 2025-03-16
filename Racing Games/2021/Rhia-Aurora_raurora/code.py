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

#for the maximum amount of coins needed to pass the level
coinsMax = 4
coinsCollected = 0

#############################
# Sub-Programs
#############################

# the function called when a key is pressed - sets direction variable
def checkKey(event):
    global xDir, yDir
    
    event.preventDefault()
    
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
    global column, row
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
            #gone off grid
            handleCrash()
        elif cell.className == "Wall":
            handleCrash()
        elif cell.className == "Coin":
            global coinsCollected
            coinsCollected = coinsCollected + 1
        elif cell.className == "Flag":
            if coinsCollected == coinsMax:
                handleWin()
            else:
                moreCoins()
        else:
            cell.className = "Car"

# if the car has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Oops you crashed..."
    
#when the car hasn't got enough coins
def moreCoins():
    global coinsMax
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "You need to collect all three cinnamon sticks to win"

# called when the page is loaded to start the timer checks
def runGame():
    global intervalHandle
    print("Running Game")
    document.addEventListener('keydown', checkKey)
    intervalHandle = window.setInterval(updatePosition, 300)

#handle win (flag reached)
def handleWin():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "WELL DONE, YOU'VE WON!"
#############################
# Main Program
#############################

runGame()
