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

# to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 0
counter = 0
tacklecounter = 0

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
        direction[1] = -1
        direction[0] = 0



def getCell():
    return document.getElementById("R{}C{}".format(position[1], position[0]))

# the timer check function - runs every 300 milliseconds to update the Messi position
def updatePosition():
    global counter
    global tacklecounter
    if direction[0] != 0 or direction[1] != 0:
        # Set the cell where the Messi was to empty
        cell = getCell()
        currClass = cell.className
        if direction[0] > 0:
            currClass = "Messi"
        elif direction[0] < 0:
            currClass = "MessiInverted"
        else:
            pass
        cell.className = ""
        
        # Update the column position for the Messi
        position[0] += direction[0]
        position[1] += direction[1]

        # Re-draw the Messi (or report a crash)
        cell = getCell()
        if cell == None:
            handleCrash()

        elif cell.className == "Ramos":
            cell.className = "MessiTackled"
            counter = counter - 1
            tacklecounter = tacklecounter + 1
            if tacklecounter == 2:
                handleCrash()
        elif cell.className == "Wall":
            handleCrash()
        elif cell.className == "Goal":
            counter = counter +1
            cell.className = currClass
            if counter > 3:
                document.getElementById("R7C7").className = "BallonDor"
        elif cell.className == "BallonDor" and counter == 4:
            handleWin()
        else:
            cell.className = currClass

#if counter > 3:
    #cell.className == BallonDorClosed:


# if the Messi has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Oops you crashed..."

# called when the page is loaded to start the timer checks
def runGame():
    global intervalHandle
    print("Running Game")
    document.addEventListener('keydown', checkKey)
    intervalHandle = window.setInterval(updatePosition, 300)

def handleWin():
    window.clearINterval(intervalHandle)
    document.getElementById("message").innerText = "You Win!"

#############################
# Main Program
#############################

runGame()
