#############################
# Library Imports
#############################

global human_liking
human_liking = 0

from js import document, window
from pyodide.ffi import create_proxy

#############################
# Global Variables
#############################

# to store current position (x,y)
position = [0, 0]

# to store movement directions (x,y)
direction = [0, 0]

# to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 0

bag = [1,0]



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
        direction[1] = 0
        # left arrow
        direction[0] = -1
    elif event.key == "ArrowUp":
        direction[0] = 0
        direction[1] = -1
    elif event.key == "ArrowDown":
        direction[0] = 0
        direction[1] = 1

def getCell():
    return document.getElementById("R{}C{}".format(position[1], position[0]))

def getFlagCell():
    return document.getElementById("R{}C{}".format(0,15))


def handleWin():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "You win! You have successfully managed to reach the food and save yourself from starvation - after all, the last time you ate was a whole hour ago!!! You have also managed to get {} treats. The amount your human likes you is {}.".format(bag[1],human_liking)

# the timer check function - runs every 300 milliseconds to update player1's position
def updatePosition():
    if direction[0] != 0 or direction[1] != 0:
        # Set the cell where player1 was to empty
        cell = getFlagCell()
        cell.className = "flag"
        cell = getCell()
        #cell = getFlagCell()
        cell.className = ""
        global human_liking
        # Update the column position for player1
        position[0] += direction[0]
        position[1] += direction[1]
        # Re-draw player1 (or report a crash)
        cell = getCell()

def prev():
        if cell == None:
            handleCrash()
        elif cell.className == "wall":
            handleCrash()
        elif cell.className == "flag":
            if human_liking > 0:
                handleWin()
            else:
                print("Uh-oh, your human doesn't like you enough to get up and feed you (again). Go be a good cat and come back!")
            #    cell.className = "flag"
        elif cell.className == "treat":
            cell.className = "player1"
            bag[1] += 1
        elif cell.className == "scratch":
            cell.className = "player1"
            
            human_liking = human_liking - 1
        elif cell.className == "goodcat":
            cell.className = "player1"
            human_liking += 1
          #Bug here
        else:
            if direction[0] == 1:
                cell.className = "player1-left"
            elif direction[0] == -1:
                cell.className = "player1"
            else:
                cell.className = "player1"
                #need to add stuff for up and down!


# if player1 has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Oops you crashed..."

# called when the page is loaded to start the timer checks
def runGame():
    global intervalHandle
    print("Running Game")
    document.addEventListener('keydown', create_proxy(checkKey))
    intervalHandle = window.setInterval(create_proxy(updatePosition), 300)

#############################
# Main Program
#############################

runGame()
