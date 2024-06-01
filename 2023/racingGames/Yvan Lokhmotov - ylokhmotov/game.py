#############################
# Library Imports
#############################
from js import document, window

#############################
# Global Variables
#############################

audioFinish = document.getElementById("audioFinish")
audioPlayback = document.getElementById("audioPlay")
audioCrash = document.getElementById("audioCrash")

# to store current position (x,y)
position = [0, 0]

# to store movement directions (x,y)
direction = [0, 0]

# to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 0

# idk why this is here
bag = [2,0]

# restart button
restartButton = document.getElementById('restartButton')

#############################
# Sub-Programs
#############################

# the function called when a key is pressed - sets direction variable
def checkKey(event):
    event.preventDefault()  # this will prevent the down arrow from scrolling the page
    if event.key == "ArrowRight":
        direction[0] = 1
        direction[1] = 0
    elif event.key == "ArrowLeft":
        # left arrow
        direction[0] = -1
        direction[1] = 0
    elif event.key == "ArrowDown":
        # down arrow
        direction[0] = 0
        direction[1] = 1
    elif event.key == "ArrowUp":
        # up arrow
        direction[0] = 0
        direction[1] = -1

def getCell():
    return document.getElementById("R{}C{}".format(position[1], position[0]))

# the timer check function - runs every 300 milliseconds to update the car position
def updatePosition():
    if direction[0] != 0 or direction[1] != 0:
        # Set the cell where the car was to empty
        cell = getCell()
        currClass = "car"
        
        if direction[0] > 0:
            currClass = "car"
        elif direction[0] < 0:
            currClass = "carFlip"
        
        cell.className = ""

        # Update the column position for the car
        position[0] += direction[0]
        position[1] += direction[1]

        # Re-draw the car (or report a crash)
        cell = getCell()
        if cell is None:
            handleCrash()
        elif cell.className == "flag":
            bag[0] -= 1
            if bag[1] == 10:
                handleWin()
        elif cell.className == "coin":
            bag[1] += 1
            cell.className = currClass
            coinsCounter()
        elif cell.className == "wall":
            handleCrash()
        else:
            cell.className = currClass


# if the car has gone off the table, this tidies up including crash message
def handleCrash():
    audioPlayback.pause()
    audioCrash.play()
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Oops you crashed..."
    restartButton.textContent = "Play again!"


def coinsCounter():
    document.getElementById("coinsCounter").innerText = "Coins collected: {}".format(bag[1]) 


def getCell():
    return document.getElementById("R{}C{}".format(position[1], position[0]))


# called when the page is loaded to start the timer checks
def runGame():
    global intervalHandle
    print("Running Game")
    document.addEventListener('keydown', checkKey)
    intervalHandle = window.setInterval(updatePosition, 300)

def handleWin():
    audioPlayback.pause()
    audioFinish.play()
    window.clearInterval(intervalHandle)
    document.getElementById('Message').innerHTML = "You won and scored {} coins!".format(bag[1])
    restartButton.textContent = "Play again!"

#############################
# Main Program
#############################

audioFinish.autoplay = False
audioFinish.load()

audioCrash.autoplay = False
audioCrash.load()

audioPlayback.autoplay = True
audioPlayback.load()
audioPlayback.play()


runGame()
