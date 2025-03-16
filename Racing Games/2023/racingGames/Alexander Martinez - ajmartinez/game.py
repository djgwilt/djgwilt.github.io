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

#to store flags left and count coins collected
bag = [1, 0]

# to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 0

# audio variables
audioWin = document.getElementById("audioWin")
audioFlag = document.getElementById("audioFlag")
audioCoin = document.getElementById("audioCoin")
audioCrash = document.getElementById("audioCrash")


#############################
# Sub-Programs
#############################



def handleWin():
    window.clearInterval(intervalHandle)
    document.GetElementById("SaysStuff").innertext = "You Win!"

# the function called when a key is pressed - sets direction variable
def checkKey(event):
    event.preventDefault()  # this will prevent the down arrow from scrolling the page
    if event.key == "ArrowRight":
        direction[0] = 0
        direction[1] = 1
    elif event.key == "ArrowLeft":
        direction[0] = 0
        direction[1] = -1
    elif event.key == "ArrowDown":
        direction[0] = 1
        direction[1] = 0
    elif event.key == "ArrowUp":
        direction[0] = -1
        direction[1] = 0
    elif event.key == "w":
        handleWin


def getCell():
    return document.getElementById("R{}C{}".format(position[0], position[1]))

# the timer check function - runs every 300 milliseconds to update the car position
def updatePosition():
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
        elif cell.className == "wall":
            audioCrash.play()
            handleCrash()
        elif cell.className == "coin":
            bag[1] = bag[1] + 1
            audioCoin.play()
        elif cell.className == "flag":
            bag[0] = bag[0] - 1
            if bag[0] == 0:
                audioWin.play()
                handleWin()
            else:
                audioFlag.play()
        else:
            cell.className = "sprite"
        


# if the car has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Oops you crashed..."

# called when the page is loaded to start the timer checks
def runGame():
    global intervalHandle
    print("Running Game")
    document.addEventListener('keydown', checkKey)
    intervalHandle = window.setInterval(updatePosition, 300)

#############################
# Main Program
#############################

# load in audio files ready for use
audioFlag.autoplay = False
audioFlag.load()
audioWin.autoplay = False
audioWin.load()
audioCoin.autoplay = False
audioCoin.load()
audioCrash.autoplay = False
audioCrash.load()


runGame()
