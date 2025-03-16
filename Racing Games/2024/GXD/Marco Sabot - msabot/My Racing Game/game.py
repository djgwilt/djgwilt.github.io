#############################
# Library Imports
#############################
from js import document, window
from pyodide.ffi import create_proxy
import random

############################
# Grid
############################

track = [ ["empty" for i in range(40)] for _ in range(39) ] + ["player1" + 39*"empty"]

def loadTrack():
    tableInnerHTML = ""
    for row in range(len(track)):
        tableInnerHTML += "<tr>"
        for col in range(len(track[0])):
            tableInnerHTML += "<td id='R{}C{}' class='{}'></td>".format(row, col, track[row][col])
        tableInnerHTML += "</tr>"
    document.getElementById("RacingTrack").innerHTML = tableInnerHTML


#############################
# Global Variables
#############################

# to store current position (x,y)
position = [20, 35]

numberOfEnemies = 10
enemypositions = [[random.randrange(0,39+1), 0] for _ in range(numberOfEnemies)]
enemydirection = [[random.randrange(-1,1+1),random.randrange(1,2+1)] for _ in range(numberOfEnemies)]

# to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 0

keys = set()

#############################
# Sub-Programs
#############################

# the function called when a key is pressed - sets direction variable
def checkKeydown(event):
    event.preventDefault()
    keys.add(event.key)
    
def checkKeyup(event):
    event.preventDefault()
    keys.remove(event.key)

def getCell():
    return document.getElementById("R{}C{}".format(position[1], position[0]))

def getEnemyCell(i):
    return document.getElementById("R{}C{}".format(enemypositions[i][1], enemypositions[i][0]))

# the timer check function - runs every 300 milliseconds to update player1's position
def updatePosition():
    for i in range(len(enemypositions)):
        cell = getEnemyCell(i)
        cell.className = ""

        enemypositions[i][0] += enemydirection[i][0]
        enemypositions[i][1] += enemydirection[i][1]

        cell = getEnemyCell(i)
        if cell == None:
            enemypositions[i][0] = random.randrange(0,39+1)
            enemypositions[i][1] = 0
            enemydirection[i][0] = random.randrange(-1,1+1)
            enemydirection[i][1] = random.randrange(1,2+1)
        elif cell.className == "player1":
            handleCrash()
        else:
            cell.className = "wall"

    if keys != set():
        # Set the cell where player1 was to empty
        cell = getCell()
        cell.className = ""
        
        # Update the position for player1
        if "w" in keys: position[1] += -1
        if "a" in keys: position[0] += -1
        if "s" in keys: position[1] += 1
        if "d" in keys: position[0] += 1

        # Re-draw player1 (or report a crash)
        cell = getCell()
        if cell == None or cell.className == "wall":
            handleCrash()
        else:
            cell.className = "player1"

# if player1 has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Oops you crashed..."

# called when the page is loaded to start the timer checks
def runGame():
    global intervalHandle
    print("Running Game")
    document.addEventListener('keydown', create_proxy(checkKeydown))
    document.addEventListener('keyup', create_proxy(checkKeyup))
    intervalHandle = window.setInterval(create_proxy(updatePosition), 50)

#############################
# Main Program
#############################

loadTrack()
runGame()
