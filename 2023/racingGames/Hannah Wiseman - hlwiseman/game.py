#############################
# Library Imports
#############################
from js import document, window
import time

#############################
# Global Variables
#############################

# to store current position (x,y)
position = [0, 0]

# to store movement directions (x,y)
direction = [0, 0]

# to store flags left to collect and coins collected
bag = [3, 0]

# to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 0
ticker = 0
# audio variables
audioFlag = document.getElementById("audioFlag")
audioCrash = document.getElementById("audioCrash")
audioCoin = document.getElementById("audioCoin")
audioWin = document.getElementById("audioWin")

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


def handleWin():
    if bag[0] > 0:
        print('Unfortunately you have failed to collect all 3 flags, so you must start again. Refresh the page.')
    else:
        window.clearInterval(intervalHandle)
        document.getElementById("Message").innerText = "Mickey Mouse has arrived safely back home thanks to you! Well done! You collected {} coins and {} flag(s)!".format(bag[1], 3 - bag[0])
    
def getCell():
    return document.getElementById(f"R{position[1]}C{position[0]}")

# the timer check function - runs every 300 milliseconds to update the car position

def updatePosition():
    if direction[0] != 0 or direction[1] != 0:
        # Set the cell where the car was to empty
        cell = getCell()
        currClass = cell.className
        if direction[0] > 0:
            currClass = 'car'
        elif direction[0] < 0:
            currClass = 'carFlip'
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
        elif cell.className == "coin":
            cell.className = currClass
            bag[1] = bag[1] + 1
            audioCoin.play()
        elif cell.className == "flag":
            cell.className = currClass
            bag[0] = bag[0] - 1
            audioFlag.play()
        elif cell.className == "house":
            audioWin.play()
            handleWin()
        else:
            cell.className = currClass
            

# if the car has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Oops you crashed..."

# called when the page is loaded to start the timer checks
def runGame():
    global intervalHandle
    print("Running Game")
    document.addEventListener('keydown', checkKey)
    speed = input('Please enter the level of difficulty you would like, and the speed will be altered. Enter slow, medium or fast.')
    if speed == 'slow' or speed == 'Slow':
        intervalHandle = window.setInterval(updatePosition, 500)
    elif speed == 'medium' or speed == 'Medium':
        intervalHandle = window.setInterval(updatePosition, 300)
    elif speed == 'fast' or speed == 'Fast':
        intervalHandle = window.setInterval(updatePosition, 100)
    else:
        print('Please enter a valid response.')
        time.sleep(1)
        runGame()

#############################
# Main Program
#############################

# load in audio files ready for use
audioFlag.autoplay = False
audioFlag.load()
audioCrash.autoplay = False
audioCrash.load()
audioCoin.autoplay = False
audioCoin.load()
audioWin.autoplay = False
audioWin.load()

runGame()
