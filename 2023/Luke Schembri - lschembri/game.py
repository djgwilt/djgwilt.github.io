#############################
# Library Imports
#############################
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

bag = [0]

audioWin = document.getElementById("audioWin")
audioCoin = document.getElementById("audioCoin")
audioCrash = document.getElementById("audioCrash")


#############################
# Sub-Programs
#############################

# the function called when a key is pressed - sets direction variable
def checkKey(event):
    event.preventDefault()
    if event.key == "ArrowRight":
        direction[0] = 0
        direction[1] = 1
    elif event.key == "ArrowLeft":
        # left arrow
        direction[0] = 0
        direction[1] = -1
    elif event.key == "ArrowUp":
        direction[0] = -1
        direction[1] = 0
    elif event.key == "ArrowDown":
        direction[0] = 1
        direction[1] = 0

def getCell():
    return document.getElementById("R{}C{}".format(position[0],position[1]))

# the timer check function - runs every 300 milliseconds to update the car position
def updatePosition():
    if direction[0] != 0 or direction[1] != 0:
        # Set the cell where the car was to empty
        cell = getCell()
        currClass = cell.className
        if direction[1] > 0:
            currClass = "car"
        elif direction[1] <= 0:
            currClass = "carFlip"
        cell.className = ""
        # Update the column position for the car
        position[0] += direction[0]
        position[1] += direction[1]
        # Re-draw the car (or report a crash)
        cell = getCell()
        if cell == None:
            handleCrash()
        elif cell.className == "wall":
            audioCrash.play()
            handleCrash()
        elif cell.className == "flag":
            audioWin.play()
            handleWin()
        elif cell.className == "coin":
            cell.className = currClass
            bag[0] = bag[0] + 1
            audioCoin.play()
        else:
            cell.className = currClass

# if the car has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Oops you crashed and lost all your coins because you suck at the game"
    audioCrash.play()

def handleWin():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "You Win! and scored {} coins for Shrek Wazowski!".format(bag[0])

# called when the page is loaded to start the timer checks
def runGame():
    global intervalHandle
    print("Running Game")
    document.addEventListener('keydown', checkKey)
    intervalHandle = window.setInterval(updatePosition, 200)

#############################
# Main Program
#############################

audioWin.autoplay = False
audioWin.load()
audioCoin.autoplay = False
audioCoin.load()
audioCrash.autoplay = False
audioCrash.load()

runGame()
