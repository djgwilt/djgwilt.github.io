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
xDir2 = 0
yDir2 = 0
# to store current column position
column = 0
row = 1
column2 = 0
row2 = 5
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
        xDir = 0
        yDir = -1
    elif event.keyCode == 40:
        xDir = 0
        yDir = 1
        
def releaseKey(event):
    global xDir, yDir
    if event.keyCode == 39:
        #right arrow
        xDir = 0
    elif event.keyCode == 37:
        #left arrow
        xDir = 0
    elif event.keyCode == 38:
        #up arrow
        yDir = 0
    elif event.keyCode == 40:
        #down arrow
        yDir = 0
        
def getCell(r, c):
    return document.getElementById(f"R{r}C{c}")

def checkKey2(event2):
    global xDir2, yDir2
    if event2.keyCode == 68:
        # right arrow
        xDir2 = 1
        yDir2 = 0
    elif event2.keyCode == 65:
        # left arrow
        xDir2 = -1
        yDir2 = 0
    elif event2.keyCode == 87:
        # up arrow
        xDir2 = 0
        yDir2 = -1
    elif event2.keyCode == 83:
        # down arrow
        xDir2 = 0
        yDir2 = 1
        
def releaseKey2(event2):
    global xDir2, yDir2
    if event2.keyCode == 68:
        #right arrow
        xDir2 = 0
    elif event2.keyCode == 65:
        #left arrow
        xDir2 = 0
    elif event2.keyCode == 87:
        #up arrow
        yDir2 = 0
    elif event2.keyCode == 83:
        #down arrow
        yDir2 = 0

# the timer check function - runs every 300 milliseconds to update the car position
def updatePositionAll():
    updatePosition()
    updatePosition2()

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
        if not cell or cell.className == "Wall":
            handleCrash()
        elif cell.className == "Flag":
            win()
        else:
            cell.className = "Car"

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
        cell = getCell(row2,column2)
        if not cell or cell.className == "Wall":
            handleCrash2()
        elif cell.className == "Flag":
            win2()
        else:
            cell.className = "Car2"
        
# if the car has gone off the table, this tidies up including crash message
def handleCrash():
    global column, row
    column -= xDir
    row -= yDir
    cell = getCell(row, column)
    cell.className = "Car"

def handleCrash2():
    global column2, row2
    column2 -= xDir2
    row2 -= yDir2
    cell = getCell(row2, column2)
    cell.className = "Car2"

def win():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Red wins"

def win2():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Blue wins"

# called when the page is loaded to start the timer checks
def runGame():
    global intervalHandle
    print("Running Game")
    document.addEventListener('keydown', checkKey)
    document.addEventListener('keydown', checkKey2)
    document.addEventListener('keyup', releaseKey)
    document.addEventListener('keyup', releaseKey2)
    intervalHandle = window.setInterval(updatePositionAll, 150)
#############################
# Main Program
#############################

runGame()
