#############################
# Library Imports
#############################
from js import document, window

#############################
# Global Variables 
#############################
column = 0 
row = 0 
# to store movement direction
xDir = 0
yDir = 0

# to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 0

#############################
# Sub-Programs
#############################

# the function called when a key is pressed - sets direction variable
def checkKey(event):
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
        #up arrow
        yDir =-1
        xDir = 0
    elif event.keyCode == 40:
        #down arrow
        yDir = 1 
        xDir = 0

COINSMAX = 2
coinsCollected = 0


        
        
def getCell():
    return document.getElementById(f"R{row}C{column}")


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
            handleCrash()
        elif cell and cell.className == "wall":
            handleCrash()
        elif cell and cell.className == "walltwo":
            handleCrash()
        elif cell and cell.className == "wallthree":
            handleCrash()
        elif cell and cell.className == "wallfour":
            handleCrash()            
        elif cell and cell.className == "wallfive":
            handleCrash()
        elif cell and cell.className == "flag":
            coinsCollected = coinsCollected + 1
        elif coinsCollected == 2 and cell.className == "flag":
            handleWin()
        else:
            cell.className = "Car"

           
def handleWin():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "WELL DONE, YOU'VE WON!"
            
             
            
            

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
