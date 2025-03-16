#############################
# Library Imports
#############################
from js import document, window
from pyodide.ffi import create_proxy

############################
# Grid
############################

track = [ ["player1"] + 29*["empty"], ["empty" for i in range(30)] ]

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

# position (int)
posint = [0,0]

# position (float)
posflo = [0, 0]

# velocity 
vel = [0,0]

#acceleration
acc = [0,0]

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
    return document.getElementById("R{}C{}".format(posint[1], posint[0]))

# the timer check function - runs every 300 milliseconds to update player1's position
def updatePosition():
        # Update acceleration
        if "w" in keys: acc[1] += 0.1
        if "a" in keys: acc[0] += -0.1
        if "s" in keys: acc[1] += -0.1
        if "d" in keys: acc[0] += 0.1
        # Update Velocity
        vel[0] += acc[0]
        vel[1] += acc[1]
        # Update Position Float
        posflo[0] += vel[0]
        posflo[1] -= vel[1]

        # Check if Position Integer update
        move = False
        if posint[0] != int(posflo[0]) or posint[1] != int(posflo[1]):
            cell = getCell()
            cell.className = ""
            posint[0] = int(posflo[0])
            posint[1] = int(posflo[1])
            # Set the cell where player1 was to empty
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
    intervalHandle = window.setInterval(create_proxy(updatePosition), 300)

#############################
# Main Program
#############################

loadTrack()
runGame()
