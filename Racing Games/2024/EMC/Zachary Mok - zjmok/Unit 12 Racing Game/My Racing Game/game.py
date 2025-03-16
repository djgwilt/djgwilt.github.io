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

# to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 0

audioFlag = document.getElementById("audioFlag")
audioWin = document.getElementById("audioWin")
audioRunning = document.getElementById("audioRunning")
audioDeath = document.getElementById("audioDeath")

bag = [1,0]
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
        direction[1] = -1
        direction[0] = 0
    elif event.key == "ArrowDown":
        direction[1] = 1
        direction[0] = 0        

def getCell():
    return document.getElementById("R{}C{}".format(position[1], position[0]))

# the timer check function - runs every 300 milliseconds to update the car position
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
            handleCrash()
        elif cell.className == "wall":
            audioDeath.play()
            handleCrash()
        elif cell.className == "coin":
            cell.className = player1Class
            audioWin.play()
            bag[1] = bag[1] + 1
        elif cell.className == "flag":
            cell.className = player1Class
            bag[0] = bag[0] - 1
            audioFlag.play()
            handleWin()
        elif cell.className == "Thief":
            import random
            chance = random.randint(1,2)
            if chance == 1:
                bag[1] = bag[1] + 5
            else:
                audioDeath.play()
                handleCrash()
        else:
            cell.className = player1Class

# if player1 has gone off the table, this tidies up including crash message
def handleCrash():
    audioRunning.stop()
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Oops you died..."

# if player1 reaches the flag the user has won
def handleWin():
    audioRunning.stop()
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "You win and scored {} coins".format(bag[1])

# called when the page is loaded to start the timer checks
def runGame():
    global intervalHandle
    print("Running Game")
    document.addEventListener('keydown', create_proxy(checkKey))
    intervalHandle = window.setInterval(create_proxy(updatePosition), 300)
    

#############################
# Main Program
#############################

audioFlag.autoplay = False
audioFlag.load()
audioFlag.autoplay = False
audioWin.load()
audioFlag.autoplay = False
audioWin.load()
audioFlag.autoplay = False
audioRunning.load()
audioFlag.autoplay = False
audioDeath.load()
runGame()