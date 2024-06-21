#############################
# Library Imports
#############################
from js import document, window
from pyodide.ffi import create_proxy

#############################
# Global Variables
#############################

# to store current position (x,y)
position = [0, 0]
#column is position[0]
#row is position[1]

# to store movement directions (left/right, up/down)
direction = [0, 0]
# to store flags left to collect and coins collected
bag = [2, 0]

# to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 0
count = 0

#############################
# Sub-Programs
#############################

# the function called when a key is pressed - sets direction variable
def checkKey(event):
    event.preventDefault()
    if event.key == "ArrowRight":
        # right arrow
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

        

def getCell():
    return document.getElementById("R{}C{}".format(position[1] , position[0]))

# the timer check function - runs every 300 milliseconds to update player1's position
def updatePosition():
    if direction[0] != 0 or direction[1] != 0: #if i am moving left or right
        # Set the cell where player1 was to empty
        cell = getCell()
        cell.className = ""
        
        # Update the column position for player1
        position[0] += direction[0]
        position[1] += direction[1]

        # Re-draw player1 (or report a crash)
        cell = getCell()
        if cell == None:
            handleCrash()
        elif cell.className == "wall":
            handleCrash()
        elif cell.className == "coin":
            cell.className = "player1"
            treatcount()
        elif cell.className == "flag":
            cell.className = "player1"
            win()
        else:
            cell.className = "player1"

# if player1 has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)

    document.getElementById("Message").innerText = "Oops you crashed...! you have eaten {} treats but now you are covered with poo.".format(count)

def win():
    window.clearInterval(intervalHandle)
    if count <= 5:
        print("you are going to die of starvation, unlucky there.")
    elif count <= 13:
        print("you are a happy little sausage!")
    else:
        print("you are fat now.lol.")
    document.getElementById("Message").innerText = "Well done, you found your owner! you have eaten {} treats.".format(count)
    

def treatcount():
    global count
    count = count + 1
    document.getElementById("Message").innerText = "you have collected {}".format(count)

# called when the page is loaded to start the timer checks
def runGame():
    global intervalHandle
    print("Running Game")
    document.addEventListener('keydown', create_proxy(checkKey))
    intervalHandle = window.setInterval(create_proxy(updatePosition), 175)

#############################
# Main Program
#############################

runGame()
