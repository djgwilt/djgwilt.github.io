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

# to store movement directions (x,y)
direction = [0, 0]

# to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 0
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
        direction[0] = 0
        direction[1] = -1
    elif event.key == "ArrowDown":
        direction[0] = 0
        direction[1] = 1
def getCell():
    return document.getElementById("R{}C{}".format(position[1], position[0]))
# the timer check function - runs every 300 milliseconds to update player1's position
def updatePosition():
    if direction[0] != 0 or direction[1] != 0:
        # Set the cell where player1 was to empty
        cell = getCell()
        cell.className = "sea"
        
        # Update the column position for player1
        position[0] += direction[0]
        position[1] += direction[1]
        direction[0] = 0
        direction[1] = 0
        # Re-draw player1 (or report a crash)
        cell = getCell()
        if cell == None:
            handleCrash()
        elif cell.className == "flag":
            cell.className = "player1"
            win()
        elif cell.className == "wall":
            crashwall()
        else:
            cell.className = "player1"

# if player1 has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Oh no your fish swam away..."

def win():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Congratulations! You got your fish back to its home cave!"

def crashwall():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Oh no your fish hit a shipwreck..."
# called when the page is loaded to start the timer checks
def runGame():
    global intervalHandle
    #settings()
    #setboard()
    print("Go!")
    document.addEventListener('keydown', create_proxy(checkKey))
    intervalHandle = window.setInterval(create_proxy(updatePosition), 0)

def settings():
    global playernumber
    global mode
    playernumber = 0
    mode = ""
    while playernumber == 0:
        try:
            playernumber = int(input("Select number of players (1/2/3/4)"))
            if playernumber != 1 and playernumber != 2 and playernumber != 3 and playernumber != 4:
                playernumber = 0
        except:
            pass
    if playernumber == 1:
        while mode == "":
            mode = input("Select mode (Easy/Medium/Hard) or type \"Back\" to reselect number of players")
            if mode.title() != "Easy" and mode.title() != "Medium" and mode.title() != "Hard" and mode.title() != "Back":
                mode = ""
    else:
        while mode == "":
            mode = input("Select mode (1v1/Escape/Race) or type \"Back\" to reselect number of players")
            if mode.lower() != "1v1" and mode.title() != "Escape" and mode.title() != "Race" and mode.title() != "Back":
                mode = ""
    if mode.title() == "Back":
        settings()

def setboard():
    if playernumber == 1:
        if mode.title() == "Easy":
            templist = [player1, ]
            tempposition = [0, 0]
            tempcell = document.getElementById("R{}C{}".format(tempposition[1], tempposition[0]))
            tempcell.className = templist


#############################
# Main Program
#############################
runGame()