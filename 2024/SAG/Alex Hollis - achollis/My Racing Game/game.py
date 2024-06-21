#############################
# Library Imports
#############################
from js import document, window
from pyodide.ffi import create_proxy

#############################
# Global Variables
#############################
stomach = [2,0]

# to store current position (x,y)
position = [0, 0]
positionb = [0, 0]
positiond = [4, 6]
positionh = [9, 9]

# to store movement directions (x,y)
direction = [0, 0]
directiond = [0, 0]
directionh = [0, 0]
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
        # left arrow
        direction[0] = -1
        direction[1] = 0
    elif event.key == "s":
        direction[1] = 1
        direction[0] = 0
    elif event.key == "w":
        direction[0] = 0
        direction[1] = -1
    elif event.key == "q":
        direction[0] = 0
        direction[1] = 0
    elif event.key == "e":
        directiond[0] = 0
        directiond[1] = 0
    if event.key == "j":
        directiond[0] = 1
        directiond[1] = 0
    elif event.key == "g":
        # left arrow
        directiond[0] = -1
        directiond[1] = 0
    elif event.key == "h":
        directiond[1] = 1
        directiond[0] = 0
    elif event.key == "y":
        directiond[0] = 0
        directiond[1] = -1
    elif event.key == "ArrowRight":
        directionh[0] = 1
        directionh[1] = 0
    elif event.key == "ArrowLeft":
        # left arrow
        directionh[0] = -1
        directionh[1] = 0
    elif event.key == "ArrowDown":
        directionh[1] = 1
        directionh[0] = 0
    elif event.key == "ArrowUp":
        directionh[0] = 0
        directionh[1] = -1



def getCell():
    return document.getElementById("R{}C{}".format(position[1], position[0]))

def getcelld():
    return document.getElementById("R{}C{}".format(positiond[1],positiond[0]))

def getcellh():
    return document.getElementById("R{}C{}".format(positionh[1],positionh[0]))
# the timer check function - runs every 300 milliseconds to update player1's position
def updatePosition():
    if directiond[0] != 0 or directiond[1] != 0:
        # Set the cell where player1 was to empty
        cell = getcelld()
        cell.className = ""
        

        # Update the column position for player1
        positiond[0] += directiond[0]
        positiond[1] += directiond[1]

        

        # Re-draw dhar mann (or report a crash)
        cell = getcelld()
        if cell == None:
            handleoffcourse()
        elif cell.className == "wall":
            handleoffcourse()
        elif cell.className =="fakewall":
            handleoffcourse()
        elif cell.className =="burger":
            stomach[1] = stomach[1] + 1
            if stomach[1]>2:
                handledharmannWin()
        else:
            cell.className = "flag"
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
        elif cell.className == "flag":
            handleWin()
        elif cell.className == "wall":
            handleCrash()
        elif cell.className == "dharwall":
            handleCrash()
        else:
            cell.className = "player1"
 

# if player1 has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "You could not force Dhar Mann to pay you the agreed upon wage. He went on to mistreat workers for the rest of his career."

def handleoffcourse():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "dhar mann bonked his head into a wall and went unconscious. Mr Feast kidnaps him and hold him ransom for the agreed upon wage"

def handleWin():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "You succesfully forced Dhar Mann to pay you the agreed upon wage. Dhar Mann is forced to pay a $10,000 fine for attempting to mistreat workers and is put on probation for 5 years (Based on a true story)."
 

def handledharmannWin():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "You let Dhar Mann run away! Not only did he steal Mr Feast and his family's dinner for the next two weeks, but he also returned to his exploitative ways unpunished and refused to pay his employees for the rest of his career! His life ended with stolen riches built off the sacrifices of actors like Colin and Other Colin."

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
