#############################
# Library Imports
#############################
from js import document, window

#############################
# Global Variables
#############################

winaudio = document.getElementById("winaudio")
# to store current position (x,y)
position = [0, 0]

# to store movement directions (x,y)
direction = [0, 0]

# to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 0

bag = [0,0]
#############################
# Sub-Programs
#############################

# the function called when a key is pressed - sets direction variable
def checkKey(event):
    event.preventDefault()
    if event.key == "ArrowLeft":
        direction[0] = 0
        direction[1] = -1
    elif event.key == "ArrowRight":
        # left arrow
        direction[0] = 0
        direction[1] = 1
    elif event.key == "ArrowUp":
        direction[0] = -1
        direction[1] = 0
    elif event.key == "ArrowDown":
        direction[0] = 1
        direction[1] = 0


def getCell():
    return document.getElementById("R{}C{}".format(position[0] , position[1]))


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
        elif cell.className == "flag":
            winaudio.play()
            handleWin() 
        elif cell.className == "coins":
            bag[0] = bag[0] + 1
            cell.className = "car"
        else:
            cell.className = "car"
def handleWin():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "You win and found {} coin(s)!".format(bag[0]) 
#############################
# Main Program
#############################

winaudio.autoplay = False 
winaudio.load()

runGame()
