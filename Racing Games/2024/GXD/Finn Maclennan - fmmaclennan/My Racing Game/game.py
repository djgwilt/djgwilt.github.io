#############################
# Library Imports
#############################
from js import document, window
from pyodide.ffi import create_proxy
import random

#############################
# Global Variables
#############################

# to store current position (x,y)
position = [0, 0]

# to store movement directions (x,y)
direction = [0, 0]

# to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 0

WhenWallGen = 0


Score = -1
#############################
# Sub-Programs
#############################

# the function called when a key is pressed - sets direction variable
def checkKey(event):
    direction[1] = 1
    if event.key == "ArrowUp":
        direction[1] = -1


def getCell():
    return document.getElementById("R{}C{}".format(position[1], position[0]))

def getCellXY(x, y):
    return document.getElementById("R{}C{}".format(y, x))

def wallgen(x,y):
    return document.getElementById("R{}C{}".format(y, x))

# the timer check function - runs every 300 milliseconds to update player1's position
def updatePosition():  
    global WhenWallGen
    global Score
    global time
    for x in range(5):
        for y in range(6):
            getCellXY(x, y).className = getCellXY(x+1, y).className

    WhenWallGen +=  1
    if WhenWallGen == 5:
        Score += 1
        GapPlace = random.randint(1,4)
        for y in range(6):
            x = 5
            if y > GapPlace:
                wallgen(x,y).className = "wall"

            elif y+1 < GapPlace:
                wallgen(x,y).className = "wall"
            else:
                wallgen(x,y).className = ""
        WhenWallGen = 0
    else:
        for y in range(6):
            x=5
            wallgen(x,y).className = ""




    if direction[0] != 0 or direction[1] != 0:
        # Set the cell where player1 was to empty
        cell = getCell()
        cell.className = ""
        
        # Update the column position for player1
        position[0] += direction[0]
        position[1] += direction[1]
        direction[1] = 1
        # Re-draw player1 (or report a crash)
        cell = getCell()
        if cell == None:
            handleCrash()
        elif cell.className == "wall":
            handleCrash()
        else:
            cell.className = "player1"

        

# if player1 has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Your score was ",Score

# called when the page is loaded to start the timer checks
def runGame():
    global intervalHandle
    difficulty = int(input("how many miliseconds do you want per tick (guide: 400 = esay 325 = medium 250 = hard):"))
    print("Running Game")
    document.addEventListener('keydown', create_proxy(checkKey))
    intervalHandle = window.setInterval(create_proxy(updatePosition), difficulty)

#############################
# Main Program
#############################

runGame()

