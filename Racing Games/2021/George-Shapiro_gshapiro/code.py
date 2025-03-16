#############################
# Library Imports
#############################
from js import document, window

#############################
# Global Variables
#############################

audio = document.getElementById("TokyoDrift")
audio.autoplay = True
audio.load()

# to store movement direction
xDir = 0
yDir = 0

xDir2 = 0
yDir2 = 0

# to store current column position
column = 0
row = 0

column2 = 0
row2 = 1

# to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 0
intervalHandle2 = 0

HIGHSPEED = 75
LOWSPEED = 200
intervalSpeed = HIGHSPEED
intervalSpeed2 = HIGHSPEED

#############################
# Sub-Programs
#############################

# the function called when a key is pressed - sets direction variable
def checkKey(event):
    
    event.preventDefault()
    
    global xDir, yDir, xDir2, yDir2, intervalSpeed, intervalHandle, intervalHandle2, intervalSpeed2
    if event.shiftKey and intervalSpeed == HIGHSPEED:
        window.clearInterval(intervalHandle)
        intervalSpeed = LOWSPEED
        intervalHandle = window.setInterval(updatePosition, intervalSpeed)
    elif not event.shiftKey and intervalSpeed == LOWSPEED:
        window.clearInterval(intervalHandle)
        intervalSpeed = HIGHSPEED
        intervalHandle = window.setInterval(updatePosition, intervalSpeed)
    
    if event.keyCode == 67 and intervalSpeed2 == HIGHSPEED:
        window.clearInterval(intervalHandle2)
        intervalSpeed2 = LOWSPEED
        intervalHandle2 = window.setInterval(updatePosition2, intervalSpeed2)
    elif not event.keyCode == 67 and intervalSpeed2 == LOWSPEED:
        window.clearInterval(intervalHandle2)
        intervalSpeed2 = HIGHSPEED
        intervalHandle2 = window.setInterval(updatePosition2, intervalSpeed2)  
    
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
    elif event.keyCode == 65:
        # p2 left
        xDir2 = -1
        yDir2 = 0
    elif event.keyCode == 68:
        # p2 right
        xDir2 = 1
        yDir2 = 0
    elif event.keyCode == 83:
        # p2 down
        xDir2 = 0
        yDir2 = 1
    elif event.keyCode == 87:
        # p2 up
        xDir2 = 0
        yDir2 = -1

def getCell(r, c):
    return document.getElementById(f"R{r}C{c}")

# the timer check function - runs every 300 milliseconds to update the car position
def updatePosition():
    global column, row
    if xDir != 0 or yDir != 0:
        # Set the cell where the car was to empty
        cell = getCell(row, column)
        cell.className = "Empty"
        
        # Update the column position for the car
        column += xDir
        row += yDir
        
        # Re-draw the car (or report a crash)
        cell = getCell(row, column)
        if cell and cell.className != "wall":
            cell.className = "Car"
        else:
            handleCrash()
            
def updatePosition2():
    global column2, row2
    if xDir2 != 0 or yDir2 != 0:
        # Set the cell where the car was to empty
        cell = getCell(row2, column2)
        cell.className = "Empty"
        
        # Update the column position for the car
        column2 += xDir2
        row2 += yDir2
        
        # Re-draw the car (or report a crash)
        cell = getCell(row2, column2)
        if cell and cell.className != "wall":
            cell.className = "Car2"
        else:
            handleCrash2()            

# handle win (flag reached)
def handleWin():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "harder now"

# if the car has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Oops P1 crashed..."

def handleCrash2():
    window.clearInterval(intervalHandle2)
    document.getElementById("Message").innerText = "Oops P2 crashed..."
    
# called when the page is loaded to start the timer checks
def runGame():
    global intervalHandle, intervalHandle2
    print("Running Game")
    document.addEventListener('keydown', checkKey)
    intervalHandle = window.setInterval(updatePosition, intervalSpeed)
    intervalHandle2 = window.setInterval(updatePosition2, intervalSpeed)


#############################
# Main Program
#############################

runGame()
