#############################
# Library Imports
#############################
from js import document, window

#############################
# Global Variables
#############################
# audio variables
audioFlag = document.getElementById("audioFlag")
audioWin = document.getElementById("audioWin")
audioCrash = document.getElementById("audioCrash")
audioCoin = document.getElementById("audioCoin")
# to store current position (x,y)
position = [0, 0]

# to store movement directions (x,y)
direction = [0, 0]

# to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 0
# storing flags left to collect + coins collected
bag = [2,0]

#############################
# Sub-Programs
#############################

# the function called when a key is pressed - sets direction variable
def handleWin():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "You Win and scored {} coins!".format(bag[1])


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
    return document.getElementById("R{}C{}".format(position[1],position[0]))

# the timer check function - runs every 500 milliseconds to update the car position
def updatePosition():
    if direction[0] != 0 or direction[1] != 0:
        # Set the cell where the car was to empty
        cell = getCell()
        cell.className = ""
        if direction[0] >= 0:
            currClass = "car"
        elif direction[0] < 0:
            currClass = "carFlip"
        
        # Update the column position for the car
        position[0] += direction[0]
        position[1] += direction[1]
        # Re-draw the car (or report a crash)
        cell = getCell()
        if cell.className == "wall" or cell == None:
            handleCrash()
            audioCrash.play()
        elif cell.className == "coin":
            cell.className = currClass
            bag[1] = bag[1] + 1
            audioCoin.play()
        elif cell.className == "flag":
            cell.className = currClass
            bag[0] = bag[0] - 1
            if bag[0] == 0:
                audioWin.play()
                handleWin()
            else:
                audioFlag.play()

        elif cell.className == "wall" or cell == None:
            handleCrash()
            audioCrash.play()
     
        

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
    intervalHandle = window.setInterval(updatePosition, 500)

#############################
# Main Program
#############################
audioFlag.autoplay = False
audioFlag.load()
audioWin.autoplay = False
audioWin.load()
audioCoin.autoplay = False
audioCoin.load()
audioCrash.autoplay = False
audioCrash.load()

runGame()
