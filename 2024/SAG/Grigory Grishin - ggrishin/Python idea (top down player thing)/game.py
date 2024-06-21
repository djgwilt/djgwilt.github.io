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
bulpos = [1, 0]

# to store movement directions (x,y)
direction = [0, 0]
buldirection = [0, 0]
bag = [2, 0]

# to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 0

#############################
# Sub-Programs
#############################

# the function called when a key is pressed - sets direction variable
def bulcheckKey(event):
    event.preventDefault()
    if event.key == "ArrowRight":
        buldirection[0] = 1
        cell = document.getElementById("R{}C{}".format(position[1], 1))
        cell.className = "bul"

def checkKey(event):
    event.preventDefault()
    if event.key == "ArrowDown":
        direction[1] += 1
        updatePosition()
        direction[1] = 0
        updatePosition()
    elif event.key == "ArrowUp":
        direction[1] -= 1
        updatePosition()
        direction[1] = 0
        updatePosition()

def getCell():
    return document.getElementById("R{}C{}".format(position[1], position[0]))

def getbulCell():
    return document.getElementById("R{}C{}".format(bulpos[1], bulpos[0]))

def handleWin():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "You Win and collected {} coins!".format(bag[1])


def updateBP():
    bcell = getbulCell()
    bcell.className = ""
    bulclass = "bul"
    if bulpos[0] == 1:
        bulpos[1] = position[1]
        bulpos[0] += buldirection[0]
    else:
        bulpos[0] += buldirection[0]
        
        
    bcell = getbulCell()
    if bcell == None:
            print("y")
    else:
            bcell.className = bulclass
    
    
    
# the timer check function - runs every 300 milliseconds to update player1's position
def updatePosition():
    if direction[0] != 0 or direction[1] != 0:
        # Set the cell where player1 was to empty
        cell = getCell()
        cell.className = ""        
        player1Class = "player1"

        # Update the column position for player1
        position[0] += direction[0]
        position[1] += direction[1]
        # Re-draw player1 (or report a crash)
        cell = getCell()

        if cell == None:
            handleCrash()
        elif cell.className == "wall":
            handleCrash()
        elif cell.className == "coin":
            cell.className = player1Class
            bag[1] = bag[1] + 1
        elif cell.className == "portal1":
            position[0] = 0
            position[1] = 0
        elif cell.className == "flag":
            cell.className = player1Class
            bag[0] = bag[0] - 1
            if bag[0] == 0:
                handleWin() 
        else:
            cell.className = player1Class
            

# if player1 has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Oops you crashed..."

# called when the page is loaded to start the timer checks
def runGame():
    global intervalHandle
    print("Running Game")
    document.addEventListener('keydown', create_proxy(checkKey))
    document.addEventListener('keydown', create_proxy(bulcheckKey))
    intervalHandle = window.setInterval(create_proxy(updateBP), 300)

#############################
# Main Program
#############################

runGame()
