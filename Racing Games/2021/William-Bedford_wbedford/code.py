#############################
# Library Imports
#############################
from js import document, window

#############################
# Global Variables
#############################
score = 0

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
        yDir = -1
        xDir = 0
    elif event.keyCode == 40:
        yDir = 1
        xDir = 0
def getCell():
    return document.getElementById(f"R{row}C{column}")

# the timer check function - runs every 300 milliseconds to update the car position
def updatePosition():
    global column, row, score
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
        elif cell.className == "wall" or cell.className == "wall1" or cell.className == "wall2" or cell.className == "wall3" or cell.className == "wall4":
            handleCrash()
                
        elif cell.className == "flag":
            handleWin()
        else:
            if cell.className == "coin":
                score += 1
            cell.className = "Car"
# if the car has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Oops you crashed..."
    audio = document.getElementById("CrashSound")
    audio.autoplay = True
    audio.load()

def handleWin():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "WELL DONE, YOU MADE IT TO THE KWIK-E-MART!" 
    audio = document.getElementById("WinSound")
    audio.autoplay = True
    audio.load()

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
