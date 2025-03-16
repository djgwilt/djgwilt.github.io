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

#to store current position (x,y)
position = [0,0]

#to store movement direction (x,y)
direction = [0,0]

#to store flags left to collect and coins collected
bag = [3,0]

#to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 0







#############################
# Sub-Programs
#############################
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


def getCell ():
    return document.getElementById("R{}C{}".format(position[1], position[0]))


def updatePosition():
    if direction[0] != 0 or 1:
    # Set the cell where the car was to empty
        cell = getCell()
        cell.className = ""
    
        # Update the column position for the car
        position[0] += direction[0]
        position[1] += direction[1]
        # re-draw the car (or report a crash)
        cell = getCell()
        if cell == None:
            handleCrash()
        elif cell.className == "wall":
            handleCrash()
        elif cell.className == "flag":
            handleWin()
        elif cell.className == "coin":
            bag[1] = bag[1] + 1
        
        else:
            cell.className = "car"
        
        



# if the car has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Oops you crashed..."

def handleWin():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "WELL DONE YOU WIN"

# called when the page is loaded to start the timer checks
def runGame():
    global intervalHandle
    print("Running Game")
    document.addEventListener('keydown', checkKey)
    intervalHandle = window.setInterval(updatePosition, 250)



#############################
# Main Program
#############################

runGame()
