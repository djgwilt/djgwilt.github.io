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
        
        direction[0] = 0
        direction[1] = 1
    elif event.key == "w":
        
        direction[0] = 0
        direction[1] = -1
def getCell():
    return document.getElementById("R{}C{}".format(position[1], position[0]))

# the timer check function - runs every 300 milliseconds to update the car position
def updatePosition():
    if direction[0] != 0 or direction[1] != 0:
        # Set the cell where the car was to empty
        cell = getCell()
        cell.className = ""
        
        # Update the column position for the car
        position[0] += direction[0]
        position[1] += direction[1]
        # Re-draw the car (or report a crash)
        cell = getCell()
        if cell == None:
            handleCrash()
        elif cell.className == "Wall":
            handleCrash()
        elif cell.className == "Bed":
            handleSleep()
        elif cell.className == "Trump":
            handleTrump()
        elif cell.className == "Whitehouse":
            handleWin()
        else:
            cell.className = "biden"
   

# if the car has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Oops you crashed..."
def handleSleep():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Sleepy Joe fell asleep..."
def handleTrump():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Donald Trump finally won the popular vote and the Presidential election with it..."
def handleWin():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "You won the election! Now have a nap."
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