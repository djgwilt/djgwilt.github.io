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
coin = 0
# to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 0

#############################
# Sub-Programs
#############################

# the function called when a key is pressed - sets direction variable
def checkKey(event):
    event.preventDefault()
    if event.key == "d":
        direction[0] = 1
        direction[1] = 0
    elif event.key == "a":
        direction[0] = -1
        direction[1] = 0
    elif event.key == "w":
        direction[1] = -1
        direction[0] = 0
    elif event.key == "s":
        direction[1] = 1
        direction[0] = 0


def getCell():
    return document.getElementById("R{}C{}".format(position[1],position[0]))

# the timer check function - runs every 300 milliseconds to update the car position
def updatePosition():
    if direction[0] != 0 or direction[1] != 0:
        # Set the cell where the car was to empty
        cell = getCell()
        if direction[0] > 0:
            player1Class = "car" 
        elif direction[0] < 0:
            player1Class = "carFlipped"
        else:
            player1Class = cell.className
        cell.className = ""
            
            
    
        # Update the column position for the car
        position[0] += direction[0]
        position[1] += direction[1]

        # Re-draw player1 (or report a crash)
        cell = getCell()
        if cell == None:
            handleCrash()
        elif cell.className == "wall":
            handleCrash()
        elif cell.className == "coin":
            handleCoin()
        elif cell.className =="diamond":
            handleWin()
        else:
            cell.className = player1Class   

       

# if the car has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Oops you crashed..."

def handleCoin():
    global coin
    coin += 1
    cell = getCell()
    cell.className = ""
    cell.className = "car"

def runGame():
    global intervalHandle
    print("Running Game")
    document.addEventListener('keydown', checkKey)
    intervalHandle = window.setInterval(updatePosition, 300)

def handleWin():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "You Win!! and scored {} diamond(s)!".format(coin)

#############################
# Main Program
#############################

runGame()
