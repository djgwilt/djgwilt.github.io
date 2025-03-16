#############################
# Library Imports
#############################
from js import document, window
from pyodide.ffi import create_proxy

#############################
# Global Variables
#############################

putFlagBack = False
level = 1

# to store current position (x,y)
position = [0, 0]

# to store movement directions (x,y)
direction = [0, 0]

# to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 0

#############################
# Sub-Programs
#############################
track = [
    ["player1", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"],
    ["empty", "wall", "wall", "wall", "empty", "wall", "wall", "empty", "empty"] ,
    ["empty", "wall", "coin1", "empty", "empty", "wall", "coin2", "empty", "empty"] ,
    ["empty", "wall", "empty", "wall", "empty", "wall", "wall", "wall", "empty"] ,
    ["empty", "empty", "empty", "wall", "empty", "empty", "coin3", "wall", "empty"] ,
    ["empty", "wall", "wall", "wall", "wall", "wall", "empty", "wall", "empty"] ,
    ["empty", "empty", "empty", "empty", "flag", "wall", "empty", "empty", "empty"] ,
    ["wall", "wall", "empty", "empty", "empty", "empty", "empty", "wall", "wall"] ,
]


def checkKey(event):
    event.preventDefault()
    if event.key == "ArrowRight":
        direction[0] = 1
        direction[1] = 0
    elif event.key == "ArrowLeft":
        # left arrow
        direction[0] = -1
        direction[1] = 0
    elif event.key == "ArrowDown":
        direction[0] = 0
        direction[1] = 1
    elif event.key =="ArrowUp":
        direction[0] = 0
        direction[1] = -1 
numcoin = 0

def getCell():
    return document.getElementById("R{}C{}".format(position[1], position[0]))
    
# the timer check function - runs every 300 milliseconds to update player1's position
def updatePosition():
    global numcoin
    global putFlagBack
    if direction[0] != 0 or direction[1] != 0:
        # Set the cell where player1 was to empty
        cell = getCell()
        cell.className = ""
        if putFlagBack == True:
            cell.className = "flag"
            putFlagBack = not(putFlagBack)

        
        # Update the column position for player1
        position[0] += direction[0]
        position[1] += direction[1]

        # Re-draw player1 (or report a crash)
        cell = getCell()
        if cell == None:
            handleCrash()
        elif cell.className == "wall":
            handleCrash()
        elif cell.className == "coin1" or cell.className == "coin2" or cell.className == "coin3":
            numcoin = numcoin + 1
            cell.className = "player1"
        elif cell.className =="flag" and numcoin != 3:
            handleMorecoin()
            cell.className = "player1"
            putFlagBack = True
        elif cell.className == "flag" and numcoin == 3:
            cell.className = "player1"
            handleWin()
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
    document.addEventListener('keydown', create_proxy(checkKey))
    intervalHandle = window.setInterval(create_proxy(updatePosition), 300)

def handleWin():
    global level
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "You just completed level {} of 2".format(level)
    level = level + 1
    

def handleMorecoin():
     document.getElementById("Message").innerText = "NEED TO COLLECT ALL THE SAUCES"




# load the track
def loadTrack():
    tableInnerHTML = ""
    for row in range(len(track)):
        tableInnerHTML += "<tr>"
        for col in range(len(track[0])):
            tableInnerHTML += "<td id='R{}C{}' class='{}'></td>".format(row, col, track[row][col])
        tableInnerHTML += "</tr>"
    document.getElementById("RacingTrack").innerHTML = tableInnerHTML

    

runGame()
#############################
# Main Program
#############################


