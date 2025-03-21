#############################
# Library Imports
#############################
from js import document, window
from pyodide.ffi import create_proxy

position = [0, 0]

direction = [0, 0]

bag = [2, 0]

intervalHandle = 0

audioCrash = document.getElementById("audioCrash")

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

def updatePosition():
    if direction[0] != 0 or direction[1] != 0:
        cell = getCell()
        if direction[0] > 0:
            player1Class = "player1"
        elif direction[0] < 0:
            player1Class = "player1-left"
        else:
            player1Class = cell.className  # keep the current sprite
        cell.className = ""
        
        position[0] += direction[0]
        position[1] += direction[1]

        cell = getCell()
        if cell == None:
            handleCrash()
        elif cell.className == "wall":
            handleCrash()
        elif cell.className == "coin":
            cell.className = player1Class
            bag[1] = bag[1] + 1
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
    audioCrash.play()

# if player1 reaches the flag the user has won
def handleWin():
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

audioCrash.autoplay = False
audioCrash.load()

runGame()
