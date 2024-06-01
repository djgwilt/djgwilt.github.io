#############################
# Library Imports
#############################
from js import document, window

#############################
# Global Variables
#############################

# speed

# to store current position (x,y)
position = [0, 0]

# to store movement directions (x,y)
direction = [0, 0]

# to store flags left to collect and coins collected
bag = [3,0]

# to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 0

# audio variables
audioFlag = document.getElementById("audioFlag")
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

# the timer check function - runs every 300 milliseconds to update the car position
def updatePosition():
    global num_speed
    if direction[0] != 0 or direction[1] != 0:
        # Set the cell where the car was to empty
        cell = getCell()
        currClass = cell.className
        if direction[0] > 0:
            currClass = "car"
        elif direction[0] < 0:
            currClass = "CarFlip"
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
            audioCoin.play()
            bag[1] = bag[1] + 1
            document.getElementById("Message").innerText = f"You now have {bag[1]} number of coins"
        elif cell.className == "flag":
            bag[0] = bag[0] - 1
            if bag[0] == 0:
                audioWin.play()
                handleWin()
            else:
                audioFlag.play()
        else:
            cell.className = currClass

# if the car has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Oops you crashed..."

# if the car reaches the flag the uesr has won
def handleWin():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "You win!"
# called when the page is loaded to start the timer checks
def runGame():
    global intervalHandle
    speed = input("What difficulty level do you want (easy/normal/hard)")
    if speed == "easy":
        num_speed = 400
    elif speed == "normal":
        num_speed = 300
    elif speed == "hard":
        num_speed = 250
    else:
        num_speed = 600
    print("Running Game")
    document.addEventListener('keydown', checkKey)
    window.clearInterval(intervalHandle)
    intervalHandle = window.setInterval(updatePosition, num_speed)

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