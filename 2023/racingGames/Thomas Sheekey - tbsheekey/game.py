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

#audio variables
audioWin = document.getElementById("audioWin")
audioCrash = document.getElementById("audioCrash")

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
    return document.getElementById("R{}C{}".format(position[1],position[0]))

# the timer check function - runs every 300 milliseconds to update the car position
def updatePosition():
    if direction[0] != 0 or direction[1] != 0:
        # Set the cell where the car was to empty
        cell = getCell()
        currClass = cell.className
        if direction[0] > 0:
            currClass = "car"
        elif direction[0] < 0:
            currClass = "carflip"
        elif direction[1] < 0:
            currClass = "carup"
        elif direction[1] > 0:
            currClass = "cardown"
        cell.className = ""
        position[0] += direction[0]
        position[1] += direction[1]


        # Re-draw the car (or report a crash)
        cell = getCell()
        if cell == None:
            handleCrash()
            audioCrash.play()
        elif cell.className == "wall":
            audioCrash.play()
            handleCrash()
        elif cell.className == "cone":
            audioCrash.play()
            handleCrash()
        elif cell.className == "flag":
            audioWin.play()
            handleWin()
        else:
            cell.className = currClass

# if the car has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Oops you crashed..."

def handleWin():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Yay you won :)))"

# called when the page is loaded to start the timer checks
def runGame():
    global intervalHandle
    print("Running Game")
    document.addEventListener('keydown', checkKey)
    intervalHandle = window.setInterval(updatePosition, 620)


#############################
# Main Program
#############################

audioWin.autoplay = False
audioWin.load()
audioCrash.autoplay = False
audioCrash.load()

runGame()