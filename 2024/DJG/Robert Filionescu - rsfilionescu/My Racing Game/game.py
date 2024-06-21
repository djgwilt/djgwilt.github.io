#############################
# Library Imports
#############################
from js import document, window
from pyodide.ffi import create_proxy

#############################
# Global Variables
#############################

# to store current position (column, row)
position = [0, 0]

# to store movement directions (x,y)
direction = [0, 0]

# to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 0

# coin counter
coin_counter = 0

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
        # left arrow
        direction[0] = -1
        direction[1] = 0
    elif event.key == "ArrowUp":
        # up arrow
        direction[1] = -1
        direction[0] = 0
    elif event.key == "ArrowDown":
        direction[1] = 1
        direction[0] = 0

def getCell():
    return document.getElementById("R{}C{}".format(position[1], position[0]))

count = 11

# the timer check function - runs every 300 milliseconds to update player1's position
def updatePosition():
    global count
    if count <= 10:
        count -=1
        if count == 0:
            slowAgain()
    global coin_counter
    if direction[0] != 0 or direction[1] != 0: # If I am moving left or right
        # Set the cell where player1 was to empty
        cell = getCell()
        cell.className = ""
        
        # Update the column position for player1
        position[0] += direction[0]
        position[1] += direction[1]

        # Re-draw player1 (or report a crash)
        cell = getCell()
        if cell.className == "flag":
            finishGame()
        elif cell == None:
            handleCrash()
        elif cell.className == "wall":
            handleCrash()
        elif cell.className == "coin":
            coin_counter += 1
            print(f"Coin counter {coin_counter}")
            cell.className = "player1"
        elif cell.className == "cloud":
            fast()
            count = 10
            cell.className = "player1"
        else:
            cell.className = "player1"

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

def fast():
    global intervalHandle
    window.clearInterval(intervalHandle)
    intervalHandle = window.setInterval(create_proxy(updatePosition), 200)

def slowAgain():
    global intervalHandle
    window.clearInterval(intervalHandle)
    intervalHandle = window.setInterval(create_proxy(updatePosition), 300)
    

def finishGame():
    window.clearInterval(intervalHandle)
  
    print("Well done you completed the game!")
    print(f"You collected {coin_counter} coins")

#############################
# Main Program
#############################

runGame()
