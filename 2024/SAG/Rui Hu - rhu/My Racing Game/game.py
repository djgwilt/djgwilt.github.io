# game.py
#############################
# Library Imports
#############################
from js import document, window
from pyodide.ffi import create_proxy

#############################
# Global Variables
#############################

# to store current position (x,y)
position = [0, 14]  # Start in the bottom

# to store movement directions (x,y)
direction = [0, 0]

# to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 0

# to store if the player has won
won = False

# to store grid dimensions
grid_width = 0
grid_height = 0

# to store the number of tesseracts collected
tesseractCollected = 0

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
    elif event.key == "ArrowDown":
        direction[0] = 0
        direction[1] = 1
    elif event.key == "ArrowUp":
        direction[0] = 0
        direction[1] = -1

def getCell(x, y):
    return document.getElementById("R{}C{}".format(y, x))

# the timer check function - runs every 300 milliseconds to update player1's position
def updatePosition():
    global tesseractCollected
    if direction[0] != 0 or direction[1] != 0:
        # Set the cell where player1 was to empty
        cell = getCell(position[0], position[1])
        cell.className = ""
        
        # Update the column position for player1
        new_x = position[0] + direction[0]
        new_y = position[1] + direction[1]

        # Check boundaries
        if new_x < 0 or new_x >= grid_width or new_y < 0 or new_y >= grid_height:
            handleCrash()
            return

        position[0] = new_x
        position[1] = new_y

        # Re-draw player1 (or report a crash)
        cell = getCell(position[0], position[1])
        if cell is None:
            handleCrash()
        elif cell.className == "wall":
            handleCrash()
        elif cell.className == "tesseract":
            tesseractCollected += 1
            cell.className = ""  # Clear the tesseract cell
        elif cell.className == "wormholeflag" and tesseractCollected == 7:
            handleWin()
        elif cell.className == "wormholeflag" and tesseractCollected != 7:
            handleCrash()
        else:
            cell.className = "player1"

# if player1 has reached the portal, this tidies up including win message
def handleWin():
    global won
    won = True
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "You Win!"

# called when the player crashes into a wall or out of bounds
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Game Over!"

# called when the page is loaded to start the timer checks
def runGame():
    global intervalHandle, grid_width, grid_height
    print("Running Game")
    document.addEventListener('keydown', create_proxy(checkKey))
    intervalHandle = window.setInterval(create_proxy(updatePosition), 500)

    # Assume the grid is defined in the HTML and we can determine its size
    grid_width = len(document.querySelectorAll('[id^="R1C"]'))
    grid_height = len(document.querySelectorAll('[id^="R"]')) // grid_width

    # Set initial position
    initial_cell = getCell(position[0], position[1])
    if initial_cell:
        initial_cell.className = "player1"

#############################
# Main Program
#############################

runGame()