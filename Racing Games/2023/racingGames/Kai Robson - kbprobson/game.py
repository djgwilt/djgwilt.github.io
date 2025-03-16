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

bag = [0]

#############################
# Sub-Programs
#############################

# the function called when a key is pressed - sets direction variable
def checkKey(event):
    event.preventDefault()
    if event.key == "d":
        direction[1] = 0
        direction[0] = 1
    elif event.key == "a":
        direction[1] = 0
        direction[0] = -1
    elif event.key == "w":
        direction[0] = 0
        direction[1] = -1
    elif event.key == "s":
        direction[0] = 0
        direction[1] = +1

def getCell():
    return document.getElementById("R{}C{}".format(position[1], position[0]))

# the timer check function - runs every 300 milliseconds to update the car position

# if the car has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Uh ohh Biggie Cheese got caught by the opps"



def handleWin():
    window.clearInterval(intervalHandle)
    document.getElementById("message").innerText = "You escaped the wrong and and survived congrats!"

def updatePosition():
    if direction[0] != 0 or direction[1] != 0:
        cell = getCell()
        cell.className = ""
        position[0] += direction[0]
        position[1] += direction[1]
        cell = getCell()
        if cell == None:
            handleCrash()
        elif cell.className == "wall":
            handleCrash()
        elif cell.className == "coin":
            cell.className = "car"
            bag[0] = bag[0] + 1
        elif cell.className == "flag":
            cell.className = "car"
            if bag[0] == 5:
                handleWin()
            
        else:
            cell.className = "car"


# called when the page is loaded to start the timer checks
def runGame():
    global intervalHandle
    print("Running Game")
    document.addEventListener('keydown', checkKey)
    intervalHandle = window.setInterval(updatePosition, 300)
    gamesound = "Bombastic.mp3"

#############################
# Main Program
#############################

runGame()
