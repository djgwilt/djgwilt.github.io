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


bag = [3,0]
# to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 0

#############################
# Sub-Programs
#############################

# the function called when a key is pressed - sets direction variable
def checkKey(event):
    event.preventDefault()  # this will prevent the down arrow from scrolling the page
    if event.key == "ArrowRight":
        direction[0]= 1
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
    if direction[0] != 0 or 1:
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
            if bag[1] == 3:
                handleWin()
            else:
                handleCrash()
        elif cell.className == "FakeWall":
                if bag[1] < 1:
                    handleCrash()
                else:
                    cell.className == "Federer"
                handleCrash()
        elif cell.className == "djokovic":
            handleCrash()
        elif cell.className == "alcaraz":
            handleCrash()
        elif cell.className == "WALL":
            handleCrash()
        elif cell.className == "trophy":
            bag[1] = bag[1] + 1
            
        elif cell.className == "Trophy":
            bag[1] = bag[1] + 1
        elif cell.className == "TROPHY":
            bag[1] = bag[1] + 1
        
        else:
            cell.className = "car"
def handleWin():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "You won all the major tornaments"
      

# if the car has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Oops you lost, try not to face the tough opponents"

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
