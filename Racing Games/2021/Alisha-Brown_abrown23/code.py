#############################
# Library Imports
#############################
from js import document, window
import random
#############################
# Global Variables
#############################

# to store movement direction
xDir = 0
yDir = 0

#to store wall movement direction
wallx = 0
wally = 0

# to store current column position
column = 2
row = 2

# to store current wall position
wColumn = 0
wRow = 0

# to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 0

#Counters:
move = 0
movesSurvived = 0

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
        #score:
        move =+ 1
    elif event.keyCode == 37:
        # left arrow
        xDir = -1
        yDir = 0
        #score:
        move =+ 1
    elif event.keyCode == 38:
        # up arrow
        xDir = 0
        yDir = -1
        #score:
        move =+ 1
    elif event.keyCode == 40:
        # down arrow
        xDir = 0
        yDir = 1
        #score:
        move =+ 1

def getCell():
    return document.getElementById(f"R{row}C{column}")

def getDoor():
    return document.getElementById(random.choice([f"R0C0", "R0C1", "R0C2", "R0C3", "R0C4", "R0C5", "R0C6", "R0C7", "R1C0", "R1C7", "R2C0", "R2C7", "R3C0", "R3C7", "R4C0", "R4C7", "R5C0", "R5C7", "R6C0", "R6C7", "R7C0", "R7C1", "R7C2", "R7C3", "R7C4", "R7C5", "R7C6", "R7C7"]))
    #["R0C0", "R0C1", "R0C2", "R0C3", "R0C4", "R0C5", "R0C6", "R0C7", "R1C0", "R1C7", "R2C0", "R2C7", "R3C0", "R3C7", "R4C0", "R4C7", "R5C0", "R5C7", "R6C0", "R6C7", "R7C0", "R7C1", "R7C2", "R7C3", "R7C4", "R7C5", "R7C6", "R7C7"]

def currentWallPos():
    return document.getElementsByClassName("wall")
    
# the timer check function - runs every 700 milliseconds to update the car position
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
        if cell and cell.className != "wall":
            cell.className = "Car"
        else:
            handleCrash()
            
def updateWall():
    global wColumn, wRow
    randomiser = ["a", "b", "c", "d"]
    choose = random.choice(randomiser)
    if choose == "a":
        # right
        wallx = 1
        wally = 0
    elif choose == "b":
        # left
        wallx = -1
        wally = 0
    elif choose == "c":
        # up
        wallx = 0
        wally = 1
    elif choose == "d":
        # down
        wallx = 0
        wally = -1
    # Set the cell where the wall was to empty
        wallCell = currentWallPos()
        wallCell.className = "Empty"
        # Update the column position for the wall
        wColumn += wallx
        wRow += wally
        # Re-draw the wall
        wallCell = currentWallPos()
        #if cell and cell.className != "wall":
        wallCell.className = "wall"
        #else:
            #handleCrash()

# if the car has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Doors are evil"

# spawns a door (/wall) on the spawner tiles
def spawnDoor():
    spawnerLocation = getDoor()
    #location = (random.choice(spawnerLocation))
    spawnerLocation.className = "wall"

# called when the page is loaded to start the timer checks
def runGame():
    global intervalHandle
    print("Running Game")
    document.addEventListener('keydown', checkKey)
    intervalHandle = window.setInterval(updatePosition, 700)
    intervalHandleTwo = window.setInterval(updateWall, 1000)
    intervalHandleThree = window.setInterval(spawnDoor, 10000)

#############################
# Main Program
#############################

runGame()
