#############################
# Library Imports
#############################
from js import document, window

#############################
# Global Variables
#############################

# to store current position (x,y)
position = [0, 7]
position2 = [8,0]

# to store movement directions (x,y)
direction = [0, 0]
direction2 = [0,0]

directionA = direction
directionB = direction2

# to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 0
hunting = 1

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
        direction[1] = -1
        direction[0] = 0
    elif event.key == "ArrowDown":
        direction[1] = 1
        direction[0] = 0
    elif event.key == "d":
        direction2[0] = 1
        direction2[1] = 0
    elif event.key == "a":
        # left arrow
        direction2[0] = -1
        direction2[1] = 0
    elif event.key == "w":
        direction2[1] = -1
        direction2[0] = 0
    elif event.key == "s":
        direction2[1] = 1
        direction2[0] = 0

def getCell():
    return document.getElementById("R{}C{}".format(position[1],position[0]))

def getCell2():
    return document.getElementById("R{}C{}".format(position2[1],position2[0]))

# the timer check function - runs every 300 milliseconds to update the car position
def updatePosition():
    global hunting
    if sum(direction) != 0:
        # Set the cell where the car was to empty
        if hunting == 2:
            player1Class = "GOOSE2"
        else:
            player1Class = "car"

        cell = getCell()
        cell.className = ""
        
        # Update the column position for the car
        position[0] += direction[0]
        position[1] += direction[1]
        # Re-draw the car (or report a crash)
        cell = getCell()
        if cell == None or cell.className == "wall":
            position[0] -= direction[0]
            position[1] -= direction[1]
        elif cell.className == "car2" and hunting == 1:
            handleWin("hunter")
        elif cell.className == "car2" and hunting == 2:
            handleWin("goose")
        cell = getCell()
        if cell.className == "powerup":
            hunting = 2
        cell.className = player1Class

    if sum(direction2) != 0:
        # Set the cell where the car was to empty
        cell = getCell2()
        cell.className = ""
        
        # Update the column position for the car
        position2[0] += direction2[0]
        position2[1] += direction2[1]
        # Re-draw the car (or report a crash)
        cell = getCell2()
        if cell == None or cell.className == "wall":
            position2[0] -= direction2[0]
            position2[1] -= direction2[1]
            
        elif cell.className == "car" and hunting == 1:
            handleWin("hunter")
        elif cell.className == "car" and hunting == 2:
            handleWin("goose")
        cell = getCell2()
        cell.className = "car2"

# if the car has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Oops..."

def handleWin(winner):
    print(f"{winner} wins")
    window.clearInterval(intervalHandle)

# called when the page is loaded to start the timer checks
def runGame():
    global intervalHandle
    print("Running Game")
    document.addEventListener('keydown', checkKey)
    intervalHandle = window.setInterval(updatePosition, 200)


#############################
# Main Program
#############################

runGame()