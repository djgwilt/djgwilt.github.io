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

#store coins
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
def getFlagCell():
    return document.getElementById("R16C16")

# the timer check function - runs every 300 milliseconds to update player1's position
def updatePosition():
    if direction[0] != 0 or direction[1] != 0:
        # Set the cell where player1 was to empty
        cell = getCell()
        if direction [0] < 0:
            player1class = "player1left"
           # print("left")
            #print(bag[1])
        elif direction [0] > 0:
           player1class = "player1right"
           #print("right")
           #print(bag[1])
        elif direction[1] > 0:
            player1class = "player1down"
           # print("down")
            #print(bag[1])
        else:
            player1class = "player1up"
            #print("up")
           # print(bag[1])
            
     #   else:
      #      player1class = cell.className
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
            bag[1] = bag[1] + 1
            print(bag[1])
            if bag[1] == 25:
                print("display flag")
                flagCell = getFlagCell()
                flagCell.className = "flag"
            
        
        elif cell.className =="flag":
            cell.className = player1class
            bag[0] = bag[0] - 1
            if bag[0] == 0:
                handleWin()
        else:
            cell.className = player1class



# if player1 has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Oops you crashed..."

# if the player reaches the flag the user has won
def handleWin():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Yay! You win! :> and you got {} food!".format(bag[1])






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
