#############################
# Library Imports
#############################
from js import document, window
from pyodide.ffi import create_proxy

#############################
# Global Variables
#############################

# to store current position (x,y)
position = [0, 0]

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

# the timer check function - runs every 300 milliseconds to update player1's position
def updatePosition():
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
    intervalHandle = window.setInterval(create_proxy(updatePosition), 200)

#############################
# Main Program
#############################

runGame()
