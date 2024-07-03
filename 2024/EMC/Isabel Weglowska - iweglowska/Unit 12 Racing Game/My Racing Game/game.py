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

# how many flies eaten
score = 0

#############################
# Sub-Programs
#############################

# the function called when a key is pressed - sets direction variable
def checkKey(event):
    event.preventDefault()  # this will prevent the down arrow from scrolling the page
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


# # the timer check function - runs every 300 milliseconds to update player1's position
# def updatePosition():
#     if direction[0] != 0 or direction[1] != 0:
#         # Set the cell where player1 was to empty
#         cell = getCell()
#         cell.className = ""
        
#         # Update the column position for player1
#         position[0] += direction[0]
#         position[1] += direction[1]

#         # Re-draw player1 (or report a crash)
#         cell = getCell()
#         if cell == None:
#             handleCrash()
#         elif cell.className == "fly":
#             print("Hit Fly")
#         else:
#             cell.className = "player1"
        

def updateFog():
    for row in range(0,11):
        for column in range(0,17):
            cell = getCellFromPos(row,column)
            distance =  ((position[1]-row)**2+abs(position[0]-column)**2)**0.5 

            if distance > 3:
                if cell.className == "wall":
                    cell.className = "FogWall"
                elif cell.className == "fly":
                    cell.className = "FogFly"
                elif cell.className == "":
                    cell.className = "Fog"
            else:
                if cell.className == "FogWall":
                    cell.className = "wall"
                elif cell.className == "FogFly":
                    cell.className = "fly"
                elif cell.className == "Fog":
                    cell.className = ""

def getCell():
    return document.getElementById("R{}C{}".format(position[1], position[0]))

def getCellFromPos(row,column):
    return document.getElementById("R{}C{}".format(row,column))

def updatePosition():
    global score
    if direction[0] != 0 or direction[1] != 0:
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
        elif cell.className == "fly":
            score += 1
            if score == 8:
                handleWin()
            cell.className = "player1"
        else:
            cell.className = "player1"
        updateFog()

# if player1 has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Oops you crashed..."

def handleWin():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "You win!!!!!"

# called when the page is loaded to start the timer checks
def runGame():
    global intervalHandle
    print("Running Game")
    document.addEventListener('keydown', create_proxy(checkKey))
    intervalHandle = window.setInterval(create_proxy(updatePosition), 600)

#############################
# Main Program
#############################

runGame()
