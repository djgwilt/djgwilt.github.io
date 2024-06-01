#############################
# Library Imports
#############################
from js import document, window
#############################
# Global Variables
fpass = False
spass = False
tpass = False
#############################

# to store current position (x,y)
position = [0, 0]

oldposition = [0, 0]

chaseposition = [0, 0]

# to store movement directions (x,y)
direction = [0, 0]

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
    elif event.key == "ArrowUp":
        #up arrow
        direction[0] = 0
        direction[1] = -1
    elif event.key == "ArrowDown":
        #down arrow
        direction[0] = 0
        direction[1] = 1
    
def getCell():
    return document.getElementById("R{}C{}".format(position[1], position[0]))



# the timer check function - runs every 300 milliseconds to update the car position
def updatePosition(): 
    global fpass
    global spass
    global tpass
    if direction[0] != 0 or direction[1] != 0: 
        # Set the cell where the car was to empty 
        cell = getCell() 
        cell.className = "" 
        chaseposition[0]
        chaseposition[1]
        # Update the column position for the car 
        position[0] += direction[0] 
        position[1] += direction[1]

        # Re-draw the car (or report a crash)
        cell = getCell()
        if cell == None:
            handleCrash()
        elif cell.className == "wall": 
            handleCrash()
        elif cell.className == "flag":
            handleWin()
        elif cell.className == "fball":
            handleCoin()
            fpass = True
        elif cell.className == "sball":
            handleCoin()
            spass = True
            tpass = True
        elif cell.className == "fwall":
            if fpass:
                handlePass()
            else:
                handleSRTackle()
        elif cell.className == "swall":
            if spass:
                handlePass()
            else:
                handleSRTackle()
        elif cell.className == "twall":
            if tpass:
                handlePass()
            else:
                handleSRTackle()
        else:
            cell.className = "car"

# if the car has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "You got tackled by a wall"

def handleSRTackle():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "You got tackled by sergio ramos"

def handleWin():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "You Win!"

def handleCoin():
    document.getElementById("Message").innerText = "You have collected a ball"

def handlePass():
    document.getElementById("Message").innerText = "You got through sergio ramos"

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
