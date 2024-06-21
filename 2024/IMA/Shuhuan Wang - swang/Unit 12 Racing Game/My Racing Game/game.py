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
tomPosition = [6,7]

# to store movement directions (x,y)
direction = [0, 0]
tomDirection = [0,0]
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
    elif event.key == "ArrowDown":
        direction[0] = 0
        direction[1] = 1
    elif event.key =="ArrowUp":
        direction[0] = 0
        direction[1] = -1 
def getCell():
    return document.getElementById("R{}C{}".format(position[1], position[0]))

def getTomcell():
    return document.getElementById("R{}C{}".format(tomPosition[1], tomPosition[0]))
# the timer check function - runs every 300 milliseconds to update player1's position
def updatePosition():
    global cheeseCount
    
    #delta = [position[0]-tomPosition[0], position[1]-tomPosition[1]]

    #if abs(delta[0]) > abs(delta[1]): # move Tom in x-axis
        #tomX = delta[0]
        #testCell = [tomX + tomPosition[0],tomPosition[1]]
        #cell = getTomcell()
        #if cell.className != "wall":
         #   tomDirection[0] = 1
          #  tomDirection[1] = 0
#    else:
 #       direction[0] = 0
  #      direction[1] = 1
    
    if direction[0] != 0 or direction[1] != 0: # you are moving!
        # Set the cell where player1 was to empty
        cell = getCell()
        cell.className = "" # remove player1 from the cell
        
        # Update the column position for player1
        position[0] += direction[0]
        position[1] += direction[1]
        # Re-draw player1 (or report a crash)
        cell = getCell() # get the new cell
        if cell == None:
            handleCrash()
        elif cell.className == "wall":
            handleCrash()
        elif cell.className == "Winning":
            cheeseCount = cheeseCount + 1
            cell.className = "player1"
            handleWin()
        elif cell.className == "home":
            if cheeseCount == 7:
                arrived = True
                handleWin()

        else:
            cell.className = "player1" # re-draw player1 in the new cell
# if player1 has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Oops you crashed..."
# called when the page is loaded to start the timer checks
def runGame():
    global arrived
    arrived = False
    global cheeseCount
    cheeseCount = 0
    global intervalHandle
    print("Running Game")
    document.addEventListener('keydown', create_proxy(checkKey))
    intervalHandle = window.setInterval(create_proxy(updatePosition), 300)

def handleWin():
    global cheeseCount
    global arrived
    if cheeseCount == 7:
        if arrived == True:
            window.clearInterval(intervalHandle)
            document.getElementById("Message").innerText = "You Win!"
#############################
# Main Program
#############################
runGame()   
