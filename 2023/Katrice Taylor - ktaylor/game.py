#############################
# Library Imports
#############################
from js import document, window

#############################
# Global Variables
#############################

# audio variables
audioWin = document.getElementById("audioWin")
audioCoin = document.getElementById("audioCoin")
audioCrash = document.getElementById("audioCrash")

# to store current position (x,y)
position = [0, 0]

# to store movement directions (x,y)
direction = [0, 0]

# to store flags left to collect and coins collected
bag = [2, 0]

# to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 0

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
        # up arrow
        direction[0] = 0
        direction[1] = -1
    elif event.key == "ArrowDown":
        # down arrow
        direction[0] = 0
        direction[1] = 1

def getCell():
    return document.getElementById("R{}C{}".format(position[1],position[0]))

# the timer check function - runs every 300 milliseconds to update the car position
def updatePosition():
    if direction[0] != 0 or direction[1] != 0 :
        # Set the cell where the car was to empty
        cell = getCell()
        currClass = cell.className
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
        if cell == None:
            handleCrash()
        elif cell.className == "wall":
            audioCrash.play()
            handleCrash()
        elif cell.className == "coin":
            cell.className = currClass
            bag[1] = bag[1] + 1
            if bag[1] == 1:
                audioCoin.play()
            if bag[1] == 2:
                audioCoin.play()
            if bag[1] == 3:
                audioCoin.play()
            if bag[1] == 4:
                audioCoin.play()
            if bag[1] == 5:
                audioCoin.play()
        elif cell.className == "flag":
            audioWin.play()
            handleWin()
        else:
            cell.className = currClass

        
def handleWin():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "well played you scored {} coins!".format(bag[1])            

# if the car has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "hahah you crashed"

# called when the page is loaded to start the timer checks
def runGame():
    global intervalHandle
    print("running Game")
    document.addEventListener('keydown', checkKey)
    intervalHandle = window.setInterval(updatePosition, 300)

#############################
# Main Program
#############################

# load in audio files ready for use
audioCoin.autoplay = False
audioCoin.load()
audioWin.autoplay = False
audioWin.load()
audioCrash.autoplay = False
audioCrash.load()

runGame()
