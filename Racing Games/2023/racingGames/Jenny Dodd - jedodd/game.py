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

# to store flags left to collect and coins collected
bag = [2,0]

# to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 0



#############################
# Sub-Programs
#############################

# the function called when a key is pressed - sets direction variable
def checkKey(event):
    event.preventDefault()  # this will prevent the down arrow from scrolling the page
    if event.key == "ArrowUp" or event.key == "w":
        direction[0] = -1
        direction[1] = 0
    elif event.key == "ArrowDown" or event.key == "s":
        # left arrow
        direction[0] = 1
        direction[1] = 0
    elif event.key == "ArrowRight" or event.key == "d":
        direction[0] = 0
        direction[1] = 1
    elif event.key == "ArrowLeft" or event.key == "a":
        direction[0] = 0
        direction[1] = -1

def getCell():
    return document.getElementById("R{1}C{0}".format(position[1], position[0]))

def handleWin():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "You Win! You scored {} coins!".format(bag[1])

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
            handleCrash()
        elif cell.className == "coin":
            cell.className = "car"
            bag[1] = bag[1]+1
        elif cell.className == "flag":
            cell.className = "car"
            bag[0] = 1
            if bag[1] == 4:
                handleWin()
        else:
            cell.className = "car"

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

runGame()
