#############################
# Library Imports
#############################
from js import document, window
from pyodide.ffi import create_proxy


#############################
# Global Variables
#############################

audioWin = document.getElementById("audioWin")
audioCrash = document.getElementById("audioCrash")
audioBackground = document.getElementById("audioBackground")
# to store current position (x,y)
position = [0, 0]

# to store movement directions (x,y)
direction = [0, 0]

# to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 0
#############################
# Sub-Programs
#############################

# the function called when a key is pressed - sets direction variable
def checkKey(event):
    event.preventDefault()
    if event.key == "d":
        direction[0] = 1
        direction[1] = 0
    elif event.key == "a":
        # left arrow
        direction[0] = -1
        direction[1] = 0
    elif event.key == "s":
        direction[0] = 0
        direction[1] = 1
    elif event.key == "w":
        direction[0] = 0
        direction[1] = -1
    


def getCell():
    audioBackground.play()
    return document.getElementById("R{}C{}".format(position[1], position[0]))
    
# the timer check function - runs every 300 milliseconds to update player1's position
def updatePosition():
    if direction[0] != 0 or direction[1] != 0:
        # Set the cell where player1 was to empty
        cell = getCell()
        cell.className = ""
        
        # Update the column position for player1
        position[0] += direction[0]
        position[1] += direction[1]

        # Re-draw player1 (or report a crash)
        cell = getCell()
        if cell == None:
            handleCrash()
            audioBackground.pause()
            audioCrash.play()
        elif cell.className ==  "wall":
            handleCrash()
            audioBackground.pause()
            audioCrash.play()
        elif cell.className == "flag":
            handleWin()
            audioBackground.pause()
            audioWin.play()
        else:
            cell.className = "player1"

def handleWin():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "You win"
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

#############################
# Main Program
#############################

audioBackground.autoplay = False
audioBackground.load()
audioWin.autoplay = False
audioWin.load()
audioCrash.autoplay = False
audioCrash.load()
runGame()




