#############################
# Library Imports
#############################
import random
from js import document, window

#############################
# Global Variables
#############################

# to store current position (x,y)
position = [0, 0]

# to store movement directions (x,y)
direction = [0, 0]

# to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 0

WIDTH = 20
HEIGHT = 20
myTrack = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]
myTrack[0][0] = 9
coins = 0

#############################
# Sub-Programs
#############################

# the function called when a key is pressed - sets direction variable
def checkKey(event):
    global direction
    event.preventDefault()
    if event.key == "ArrowRight":
        direction = [1, 0]
    elif event.key == "ArrowLeft":
        # left arrow
        direction = [-1, 0]
    elif event.key == "ArrowDown":
        direction = [0, 1]
    elif event.key == "ArrowUp":
        direction = [0, -1]

def addCoin():
    document.getElementById(f"R{random.randrange(HEIGHT)}C{random.randrange(WIDTH)}").className = "coin"

def displayCoins(coins):
    document.getElementById("Message").innerText = str(coins)

def getCell():
    return document.getElementById("R{}C{}".format(position[1], position[0]))

# the timer check function - runs every 300 milliseconds to update the car position
def updatePosition():
    global position, coins
    if direction != [0, 0]:
        # Set the cell where the car was to empty
        cell = getCell()
        cell.className = ""
        
        # Update the column position for the car
        position[0] += direction[0]
        # Update the row position for the car
        position[1] += direction[1]

        # Re-draw the car (or report a crash)
        cell = getCell()
        if cell == None or cell.className == "wall":
            handleCrash()
        elif cell.className == "coin":
            coins += 1
            displayCoins(coins)
            cell.className = "player"
            addCoin()

        else:
            cell.className = "player"

# if the car has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Oops you crashed..."

# called when the page is loaded to start the timer checks

def convertTrack(myTrack):
    '''converts the numbers in the track to the names of the objects they represent'''
    convert = {0: "empty", 1: "wall", 2: "coin", 9: "player"}
    for rowx, row in enumerate(myTrack): #rowx in the row number, row is the actual values of the row
        for colx, col in enumerate(row):
            val = myTrack[rowx][colx]
            myTrack[rowx][colx] = convert[val]
    return myTrack
            

def drawTrack():
    global myTrack
    myTrack = convertTrack(myTrack) # so the html code can be edited
    trackHTML = ""
    for rowx, row in enumerate(myTrack):
        trackHTML += "<tr>"
        for colx, col in enumerate(row):
            trackHTML += f"<td id='R{rowx}C{colx}' class='{myTrack[rowx][colx]}'></td>"
        trackHTML += "</tr>"
    document.getElementById("RacingTrack").innerHTML = trackHTML


def runGame():
    global intervalHandle
    print("Running Game")
    document.addEventListener('keydown', checkKey)
    intervalHandle = window.setInterval(updatePosition, 150)

#############################
# Main Program
#############################


drawTrack()
addCoin()
displayCoins(coins)
runGame()
