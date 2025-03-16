#############################
# Library Imports
#############################
from js import document, window
import time
#############################
# Global Variables
#############################

# to store current position (x,y)
position = [10, 0]

# to store movement directions (x,y)
direction = [0, 0]

# to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 0

bag = [1, 0]

#############################
# Sub-Programs
#############################

# the function called when a key is pressed - sets direction variable
def checkKey(event):
    global direction
    event.preventDefault()  # this will prevent the down arrow from scrolling the page
    if event.key == "ArrowRight" or event.key == "d":
        direction[0] = 1
        direction[1] = 0
    elif event.key == "ArrowLeft" or event.key == "a":
        direction[0] = -1
        direction[1] = 0
    elif event.key == "ArrowUp" or event.key == "w":
        direction[1] = -1
        direction[0] = 0
    elif event.key == "ArrowDown" or event.key == "s":
        direction[1] = 1
        direction[0] = 0
    


def getCell():
    return document.getElementById("R{}C{}".format(position[1], position[0]))

# the timer check function - runs every 300 milliseconds to update the car position
def updatePosition():
    global position
    if direction != [0, 0]:
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
        if cell == None or cell.className == "wall":
            cell.className ="explosion"
            time.sleep(50)
            handleCrash()
        elif cell.className == "flag":
            cell.className = currClass
            bag[0] = bag[0] - 1
            if bag[0] == 0:
                handleWin()
         #elif cell.className == "wall":
            #handleCrash()
        elif cell.className == "coin":
            bag[1] = bag[1] + 1
            cell.className = currClass
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
    intervalHandle = window.setInterval(updatePosition, 300)


def handleWin():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "You Win and scored {} coins!".format(bag[1])


#############################
# Main Program
#############################

runGame()
