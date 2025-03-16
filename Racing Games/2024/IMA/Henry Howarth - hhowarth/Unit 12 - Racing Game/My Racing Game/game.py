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

# to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 0

#############################
# Sub-Programs
#############################

bag = 0

# the function called when a key is pressed - sets direction variable
def checkKey(event):
    event.preventDefault()
    if event.key == "ArrowRight" or event.key == "d":
        direction[1] = 0
        direction[0] = 1
    elif event.key == "ArrowLeft" or event.key == "a":
        # left arrow
        direction[1] = 0
        direction[0] = -1
    elif event.key == "ArrowUp" or event.key == "w":
        direction[0] = 0
        direction[1] = -1
    elif event.key == "ArrowDown" or event.key == "s":
        direction[0] = 0
        direction[1] = 1

def getCell():
    return document.getElementById("R{}C{}".format(position[1], position[0]))

# the timer check function - runs every 300 milliseconds to update the car position
def updatePosition():
    if direction[0] != 0 or direction[1] != 0:
        # Set the cell where the car was to empty
        cell = getCell()
        cell.className = "" # remove player from cell
        
        # Update the column position for the car
        position[0] += direction[0]
        position[1] += direction[1]

        # Re-draw the car (or report a crash)
        cell = getCell() # get new cell
        if cell == None:
            handleCrash()
        elif cell.className == "wall":
            handleCrash()
        elif cell.className == "coin":
            handleCoin()
        elif cell.className == "end":
            handleWin()
        else:
            cell.className = "car"

# if the car has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Antony isn't meant to score..."

# called when the page is loaded to start the timer checks
def runGame():
    global intervalHandle
    print("Running Game")
    document.addEventListener('keydown', checkKey)
    intervalHandle = window.setInterval(updatePosition, 250)

def handleWin():
    cell = getCell()
    cell.className = ""
    cell.className = "spin"
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "You Win, weekly wages gained: {} (£{})".format(bag,bag*150000)

def handleCoin():
    global bag
    bag += 1
    cell = getCell()
    cell.className = ""
    cell.className = "car"
    pass
#############################
# Main Program
#############################

runGame()
