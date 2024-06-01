#############################
# Library Imports
#############################
from js import document, window

#############################
# Global Variables
#############################

audioCurr = document.getElementById("audioCurr")
yay = document.getElementById("yay")

# to store current position (x,y)
position = [0, 0]

# to store movement directions (x,y)
direction = [0, 0]

positionWall1 = [0, 5]

positionWall2 = [3, 1]

positionWall3 = [4, 5]

positionWall4 = [9, 0]
directionWall4 = [0, 1]

bag = [2, 0]

flag_count = 0

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
        direction[0] = -1
        direction[1] = 0
    elif event.key == "ArrowDown":
        direction[0] = 0
        direction[1] = 1
    elif event.key == "ArrowUp":
        direction[0] = 0
        direction [1] = -1


def getCell(pos):
    return document.getElementById("R{}C{}".format(pos[1], pos[0]))

# the timer check function - runs every 300 milliseconds to update the car position
def updatePosition():
    global flag_count, positionWall1, positionWall2, positionWall3, positionWall4
    if direction[0] != 0 or direction[1] != 0:
        # Set the cell where the car was to empty
        cell = getCell(position)
        currClass = cell.className
        if direction[0] > 0:
            currClass = "mouse"
        elif direction[0] < 0:
            currClass = "mouseflipped"
        cell.className = ""
        
        # Update the column position for the car
        position[0] += direction[0]
        position[1] += direction[1]
        audioCurr.play()
        # Re-draw the car (or report a crash)
        cell = getCell(position)
        if cell == None:
            handleCrash()
        elif cell.className == "wall":
            handleCrash()
        elif cell.className == "cat":
            handleCrash()
        elif cell.className == "flag":
            handleWin()
        elif cell.className == "cheese":
            flag_count = flag_count + 1
            if flag_count >= 10:
                document.getElementById("R1C0").className = "flag"
            cell.className = currClass
        else:
            cell.className = currClass
    oldwall = list(positionWall1)
    if positionWall1 == [0, 5]:
        positionWall1 = [0, 6]
    elif positionWall1 == [0, 6]:
        positionWall1 = [0, 7]
    elif positionWall1 == [0, 7]:
        positionWall1 = [1, 7]
    elif positionWall1 == [1, 7]:
        positionWall1 = [2, 7]
    elif positionWall1 == [2, 7]:
        positionWall1 = [2, 6]
    elif positionWall1 == [2, 6]:
        positionWall1 = [2, 5]
    elif positionWall1 == [2, 5]:
        positionWall1 = [1, 5]
    elif positionWall1 == [1, 5]:
        positionWall1 = [0, 5]
    
    getCell(oldwall).className = getCell(oldwall).className.replace(" cat", "")
    getCell(positionWall1).className = getCell(positionWall1).className + " cat"

    oldwall = list(positionWall2)
    if positionWall2 == [3, 1]:
        positionWall2 = [4, 1]
    elif positionWall2 == [4, 1]:
        positionWall2 = [4, 2]
    elif positionWall2 == [4, 2]:
        positionWall2 = [4, 3]
    elif positionWall2 == [4, 3]:
        positionWall2 = [3, 3]
    elif positionWall2 == [3, 3]:
        positionWall2 = [3, 2]
    elif positionWall2 == [3, 2]:
        positionWall2 = [3, 1]



    getCell(oldwall).className = getCell(oldwall).className.replace(" cat", "")
    getCell(positionWall2).className = getCell(positionWall2).className + " cat"

    oldwall = list(positionWall3)
    if positionWall3 == [4, 5]:
        positionWall3 = [5, 5]
    elif positionWall3 == [5, 5]:
        positionWall3 = [5, 6]
    elif positionWall3 == [5, 6]:
        positionWall3 = [5, 7]
    elif positionWall3 == [5, 7]:
        positionWall3 = [4, 7]
    elif positionWall3 == [4, 7]:
        positionWall3 = [4, 6]
    elif positionWall3 == [4, 6]:
        positionWall3 = [4, 5]
    getCell(oldwall).className = getCell(oldwall).className.replace(" cat", "")
    getCell(positionWall3).className = getCell(positionWall3).className + " cat"
    
    oldwall = list(positionWall4)
    positionWall4[1] = positionWall4[1] + directionWall4[1]
    if positionWall4[1] == 7:
        directionWall4[1] = -1
    elif positionWall4[1] == 0:
        directionWall4[1] = 1
    getCell(oldwall).className = getCell(oldwall).className.replace(" cat", "")
    getCell(positionWall4).className = getCell(positionWall4).className + " cat"
    

# if the car has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Caught!"


def handleWin():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "You evaded the cats and got the cheese!"

# called when the page is loaded to start the timer checks
def runGame():
    global intervalHandle
    print("Running Game")
    document.addEventListener('keydown', checkKey)
    intervalHandle = window.setInterval(updatePosition, 300)

#############################
# Main Program
#############################


runGame()
