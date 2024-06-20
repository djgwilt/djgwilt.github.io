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

# to store movement directions (x,y)
direction = [0, 0]

bag = [2, 0]
# to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 0

audioFlag = document.getElementById("audioFlag")
audioLose = document.getElementById("audioLose")
#############################
# Sub-Programs
#############################

# the function called when a key is pressed - sets direction variable
def checkKey(event):
    event.preventDefault()
    if event.key == "ArrowRight":
        direction[0] = 1
        direction[1] = 0
    elif event.key == "ArrowLeft":
        # left arrow
        direction[0] = -1
        direction[1] = 0
    elif event.key == "ArrowUp":
        direction[0] = 0
        direction[1] = -1
    elif event.key == "ArrowDown":
        direction[0] = 0
        direction[1] = 1

def getCell():
    return document.getElementById("R{}C{}".format(position[1], position[0]))

# the timer check function - runs every 300 milliseconds to update player1's position
def updatePosition():
    if direction[0] != 0 or direction[1] != 0:
        # Set the cell where player1 was to empty
        cell = getCell()
        if direction[0] > 0:
            player1Class = "player1"
        elif direction[0] < 0:
            player1Class = "player1-left"
        else:
            player1Class = cell.className
        cell.className = ""
        
        # Update the column position for player1
        position[0] += direction[0]
        position[1] += direction[1]

        # Re-draw player1 (or report a crash)
        cell = getCell()
        if cell == None:
            audioLose.play()
            handleCrash()
        elif cell.className == "wall":
            audioLose.play()
            handleCrash()
        elif cell.className == "flag":
            audioFlag.play()
            handleWin()
        elif cell.className == "coin":
            cell.className = player1Class
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
    intervalHandle = window.setInterval(create_proxy(updatePosition), 300)



def handleWin():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "You Win!"
#############################
# Main Program
#############################

audioFlag.autoplay = False
audioFlag.load()
audioLose.autoplay = False
audioLose.load()

runGame()
