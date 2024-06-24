#############################
# Library Imports
#############################
from js import document, window, jQuery
from pyodide.ffi import create_proxy, to_js

#############################
# Global Variables
#############################

# to store current position (x,y)
position = [3, 3]

# to store movement directions (x,y)
direction = [0, 0]

# to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 0

keysDown = []

#############################
# Sub-Programs
#############################

# the function called when a key is pressed - sets direction variable
def keydown(event):
    event.preventDefault()
    if event.key in keysDown:
        pass
    else:
        keysDown.append(event.key)

def keyup(event):
    event.preventDefault()
    keysDown.remove(event.key)


def getCell():
    return document.getElementById("R{}C{}".format(position[1], position[0]))

# the timer check function - runs every 300 milliseconds to update player1's position
def updatePosition():
    
    if "d" in keysDown or "D" in keysDown:
         direction[0] = 2
    elif "a" in keysDown or "A" in keysDown:
         direction[0] = -2
    elif "w" in keysDown or "W" in keysDown:
         direction[1] = -2
    elif "s" in keysDown or "S" in keysDown:
         direction[1] = 2


    print(keysDown)
    if direction[0] != 0 or direction[1] != 0:
        # Set the cell where player1 was to empty
        cell = getCell()
        cell.className = ""
        
        # Update the column position for player1
        position[0] += direction[0]
        position[1] += direction[1]

        # Re-draw player1 (or report a crash)
        cell = getCell()
        if cell.className == "wall":
            position[0] -= direction[0]
            position[1] -= direction[1]
        #cell.className
        
        else:
            cellRect = cell.getBoundingClientRect()
            tableRect = document.getElementById("RacingTrack").getBoundingClientRect()
            jQuery("#player1").animate(to_js({
                "left": f"{cellRect.x-tableRect.x-3}px",
                "top": f"{cellRect.y-tableRect.y-0+25}px",
                }), 300, "linear")            
            if direction[0] == 1 and direction[1] == 0:
                cell.className = "player1-right"
            elif direction[0] == -1 and direction [1] == 0:
                cell.className = "player1-left"
            elif direction[0] == 0 and direction[1] == -1:
                cell.className = "player1-up"
            elif direction [0] == 0 and direction[1] == 1:
                cell.className = "player1-down"
        direction[0] = 0
        direction[1] = 0
# if player1 has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Oops you crashed..."

# called when the page is loaded to start the timer checks
def runGame():
    global intervalHandle
    print("Running Game")
    document.addEventListener('keydown', create_proxy(keydown))
    document.addEventListener('keyup', create_proxy(keyup))
    intervalHandle = window.setInterval(create_proxy(updatePosition), 300)

#############################
# Main Program
#############################

runGame()
