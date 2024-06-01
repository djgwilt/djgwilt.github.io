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

#############################
# Sub-Programs
#############################

# the function called when a key is pressed - sets direction variable

def checkkey(event):
    global xDir, yDir
    if event.keyCode == 39:
        xDir = 1
        yDir = 0
    elif event.keyCode == 37:
        xDir = -1
        yDir = 0

    elif event.keyCode == 38:
        yDir = -1
        xDir = 0
    
    elif event.keyCode == 40:
        yDir = 1
        xDir = 0


def getCell(): 
    return document.getElementById(f"R{row}C{column}")

# the timer check function - runs every 300 milliseconds to update the car
def updatePosition():
    global column, row
    if xDir != 0 or yDir != 0:
        cell = getCell()
        cell.className = "Empty"
        
        column += xDir
        row += yDir
        
        cell = getCell()

        if not cell:
            handleCrash()
        elif cell.className == "Wall":
            handleCrash()
        elif cell.className == "Flag":
            handleWin()
        else:
            cell.className = "Car"
            

# if the car has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Oops you crashed..."

# called when the page is loaded to start the timer checks
def runGame():
    global intervalHandle
    print("Running Game")
    document.addEventListener("keydown", checkkey)
    intervalHandle = window.setInterval(updatePosition, 300)
    
def handleWin():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Well done! We got Endeavor back for all the childhood trauma!"
   

#############################
# Main Program
#############################

runGame()