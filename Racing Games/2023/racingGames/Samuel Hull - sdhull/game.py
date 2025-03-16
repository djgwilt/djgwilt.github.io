#############################
# Library Imports
#############################
from js import document, window

#############################
# Global Variables
#############################

bag = [2, 0]
# to store current position (x,y)
position = [0, 0]

# to store movement directions (x,y)
direction = [0, 0]

# to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 0

#############################
# Sub-Programs
#############################
audioFlag = document.getElementById("audioFlag")
audioWin = document.getElementById("audioWin")

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
    elif event.key == "ArrowDown":
        direction[0] = 0
        direction[1] = 1
    elif event.key == "ArrowUp":
        direction[0] = 0
        direction[1] = -1

def getCell():
    return document.getElementById("R{}C{}".format(position[1], position[0]))

# the timer check function - runs every 300 milliseconds to update the car position
def updatePosition():
    audioFlag.play()
    if direction[0] != 0 or direction[1] != 0:
        # Set the cell where the car was to empty
        cell = getCell()
        cell.className = ""
        
        # Update the column position for the car
        position[0] += direction[0]
        position[1] += direction[1]

        # Re-draw the car (or report a crash)
        cell = getCell()
        if cell == None:
            handleCrash()
        elif cell.className == "coin" :
            cell.className == "car"
            bag[1] = bag[1] + 1
        elif cell.className == "wallsam":
            handleCrash()
        elif cell.className == "wallcass":
            handleCrash
        elif cell.className == "wallalexi":
            handleCrash()
        elif cell.className == "wallchris":
            handleCrash()
        elif cell.className == "wallfelix":
            handleCrash()
        elif cell.className == "wallgeorgec":
            handleCrash()
        elif cell.className == "walljonney":
            handleCrash()
        elif cell.className == "wallneil":
            handleCrash()
        elif cell.className == "wallnoah":
            handleCrash()
        elif cell.className == "wallsam":
            handleCrash()
        elif cell.className == "wallted":
            handleCrash()
        elif cell.className == "flag":
            if bag[1] == 4:
                handleWin()
        else:
            cell.className = "car"
            

# if the car has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Oops you crashed..."

def handleWin():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "You Win you goofy goober"

# called when the page is loaded to start the timer checks
def runGame():
    global intervalHandle
    print("Running Game")
    document.addEventListener('keydown', checkKey)
    intervalHandle = window.setInterval(updatePosition, 300)

#############################
# Main Program
#############################
audioFlag.autoplay = False
audioFlag.load()
audioWin.autoplay = False
audioWin.load()

runGame()
