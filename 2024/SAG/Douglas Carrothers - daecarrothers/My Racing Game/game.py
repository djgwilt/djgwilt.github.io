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

m1position = [2, 2]
m2position = [4, 0]
m3position = [0, 4]
m4position = [6, 2]

# to store movement directions (x,y)
direction = [0, 0]

# to store coins collected
bag = [1, 0]

# to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 0

FLAGS = 0
COINS = 1

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

def getCell():
    return document.getElementById("R{}C{}".format(position[1], position[0]))

def getM1Cell():
    return document.getElementById("R{}C{}".format(m1position[1], m1position[0]))



def getExitCell():
    return document.getElementById("R{}C{}".format(8, 5))

# the timer check function - runs every 300 milliseconds to update player1's position
def updatePosition():
    cell = getM1Cell()
    cell.className = ""
    
    


    if m1position[1] == 2 and  m1position[0] == 2:
        m1position[1] = m1position[1] - 1
    else:
        m1position[1] = m1position[1] + 1
    cell = getM1Cell()
    cell.className = "wall3"




    if direction[0] != 0 or direction[1] != 0:
        # Set the cell where player1 was to empty
        cell = getCell()
        cell.className = ""
        
        # Update the column position for player1
        position[0] += direction[0]
        position[1] = position[1] + direction[1]
        # Re-draw player1 (or report a crash)
        cell = getCell()
        if cell == None:
            handleCrash()
        elif cell.className == "wall":
            handleCrash()
        elif cell.className == "wall2":
            handleCrash()  
        elif cell.className == "Winning" :
            handleWinMore()
        elif cell.className == "coin1":
            cell.className = "player1"
            bag [COINS] = bag [COINS] + 1
            print("You have coin", bag[COINS],"out of 3")
            if bag[COINS] == 3:
                handleWin()
        else:
            cell.className = "player1"

# if player1 has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "You died... Restart!"

def handleWin():
    cell = getExitCell()
    cell.className = "openExit"
 #   window.clearInterval(intervalHandle)
 #   document.getElementById("Message").innerText = "Level 1 Completed... Well done!"
  #  updatePosition()

def handleWinMore():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Congratulations... Level 1 complete!"




def handleCollect1():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "You got coin 1/3!"


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



# Notes for Mr Gray next lesson...
# How do I create moving enemies (Got the jpgs sorted)
# Removing wall at R8, C5
