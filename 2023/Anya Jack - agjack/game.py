#############################
# Library Imports
#############################
from js import document, window
import random

#############################
# Global Variables
#############################

# to store current position (x,y)
position = [0, 0]

# to store movement directions (x,y)
direction = [0, 0]

# to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 0

# to store flags left to collect and coins collected
bag = [0, 0, 0]

# audio variables
audioFlag = document.getElementById("audioFlag")
audioWin = document.getElementById("audioWin")
audioCrash = document.getElementById("audioCrash")
audioCoin = document.getElementById("audioCoin")

#random number
x = random.randint(1,5)

#############################
# Sub-Programs
#############################

# the function called when a key is pressed - sets direction variable
def checkKey(event):
    event.preventDefault()
    if event.key == "ArrowRight" or event.key == "d":
        direction[0] = 1
        direction[1] = 0
    elif event.key == "ArrowLeft" or event.key == "a":
        # left arrow
        direction[0] = -1
        direction[1] = 0
    elif event.key == "ArrowDown" or event.key == "s":
        direction[0] = 0
        direction[1] = 1
    elif event.key == "ArrowUp" or event.key == "w":
        direction[0] = 0
        direction[1] = -1

def getCell():
    return document.getElementById("R{}C{}".format(position[1], position[0]))

# the timer check function - runs every 300 milliseconds to update the car position
def updatePosition():
    handleCount()
    if direction[0] != 0 or direction[1] != 0:
        # Set the cell where the car was to empty
        cell = getCell()
        currClass = cell.className
        cell.className = ""
        locked = True
        
        # Update the column position for the car
        position[0] += direction[0]
        position[1] += direction[1]

        # Re-draw the car (or report a crash)
        
        cell = getCell()
        if cell == None:
            handleCrash()
            audioCrash.play()
        elif cell.className == "wall":
            handleCrash()
            audioCrash.play()
        #elif cell.className == "wallFake":
            #slow down
            #window.clearInterval(intervalHandle)
            #intervalHandle = window.setInterval(updatePosition, 4000)
        elif cell.className == "fish":
            cell.className = currClass
            bag[1] = bag[1] + 1
            audioCoin.play()
        elif cell.className == "icebergflag":
            cell.className = currClass
            bag[0] = bag[0] + 1
            if bag[0] == 2:
                audioWin.play()
                handleWin()
            else:
                audioFlag.play()
        elif cell.className == "key":
            cell.className = currClass
            bag[2] = bag[2] + 1
            document.getElementById("Message").innerText = "{}".format(bag[2])
            audioFlag.play()
            locked = False
        elif cell.className == "door":
            if locked and bag[2] != 1:
                handleLocked()
                position[0] -= direction[0]
                position[1] -= direction[1]
                cell = getCell()
                cell.className = "sprite"
            else:
                cell.className = currClass
        elif cell.className == "rainbow":
            cell.className = currClass
            if x == 1:
                handleDie()
                audioCrash.play()
            else:
                handleRainbow()
                audioFlag.play()
        else:
            cell.className = currClass

# if the car has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Oops you crashed... but you collected {} fish and {} flag(s)!".format(bag[1], bag[0])

# called when the page is loaded to start the timer checks
def runGame():
    global intervalHandle
    print("Running Game")
    document.addEventListener('keydown', checkKey)
    intervalHandle = window.setInterval(updatePosition, 300)

def handleWin():
    document.getElementById("Message").innerText = "You Win and scored {} fish!".format(bag[1])
    window.clearInterval(intervalHandle)

def handleCount():
    document.getElementById("Message").innerText = "Fish = {}".format(bag[1])

def handleLocked():
    document.getElementById("Message").innerText = "Collect the key to unlock the door!"    

def handleRainbow():
    document.getElementById("Message").innerText = "Yay! You were lucky and found a rainbow with 5 fish at the end!"
    bag[1] = bag[1] + 5

def handleDie():
    document.getElementById("Message").innerText = "Oh no, your rainbow had a nuclear meltdown!!💥"
    window.clearInterval(intervalHandle)

#############################
# Main Program
#############################

# load in audio files ready for use
audioFlag.autoplay = False
audioFlag.load()
audioWin.autoplay = False
audioWin.load()
audioCrash.autoplay = False
audioCrash.load()
audioCoin.autoplay = False
audioCoin.load()

runGame()