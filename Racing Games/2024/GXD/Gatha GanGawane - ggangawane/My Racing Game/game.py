###################
# Library Imports #
###################
from js import document, window, jQuery
from pyodide.ffi import create_proxy, to_js

####################
# Global Variables #
####################

# to store current position (x,y)
position = [1, 4]

# to store movement directions (x,y)
direction = [0, 0]

# to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 0

################
# Sub-Programs #
################

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
        if direction[0] > 0:
            player1Class = "player_1_right"
        elif direction[0] < 0:
            player1Class = "player_1_left"
        elif direction[1] > 0:
            player1Class = "player_1_down"
        elif direction[1] < 0:
            player1Class = "player_1_up"
        else:
            player1Class = cell.className
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
        elif cell.className == "flag":
            handleWin()
        else:
            #cell.className = player1Class
        
            #cell.className = "player_1_right"
            sprite = document.getElementById("player1")
            sprite.className = player1Class + " sprite"
            cellRect = cell.getBoundingClientRect()
            tableRect = document.getElementById("RacingTrack").getBoundingClientRect()
            jQuery("#player1").animate(to_js({
                "left": f"{cellRect.x-tableRect.x+2}px",
                "top": f"{cellRect.y-tableRect.y+42}px",
            }), 300, "linear")

# if player1 has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "You lose! Refresh to try again?"

def handleWin():
    window.clearInterval(intervalHandle)
    sprite = document.getElementById("player1")
    sprite.className = ""
    document.getElementById("Message").innerText = "You Win!"

# called when the page is loaded to start the timer checks
def runGame():
    global intervalHandle
    print("Running Game")
    document.addEventListener('keydown', create_proxy(checkKey))
    intervalHandle = window.setInterval(create_proxy(updatePosition), 300)

################
# Main Program #
################

runGame()