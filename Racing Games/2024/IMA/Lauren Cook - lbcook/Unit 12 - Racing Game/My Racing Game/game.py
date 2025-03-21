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

#to store grasshoppers collected
bag = [0,0]

#############################
# Sub-Programs
#############################

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
 
def getCell():
    return document.getElementById("R{}C{}".format(position[1],position[0]))
 
# the timer check function - runs every 300 milliseconds to update the car position
def updatePosition():
    if direction[0] != 0 or direction[1] != 0:
        # Set the cell where the car was to empty
        cell = getCell()
        original = cell.className
        cell.className = ""
       
        # Update the column position for the car
        position[0] += direction[0]
        position[1] += direction[1]
 
        # Re-draw the car (or report a crash)
        cell = getCell()
        if cell.className == None or cell.className == "wall": # there is no cell with that ID
            handleCrash()
        elif cell.className == "tree":
            handleWin()
        elif cell.className == "grasshopper":
            cell.className = "gecko"
            bag[1] = bag[1] + 1
        else:
            if direction[0] < 0: # left
                cell.className = "gecko" #draw the car in new location
            elif direction[0] > 0: # right
                cell.className = "geckoright" #draw the car in new location
            else:
                cell.className = original # up or down


            
 
# if the car has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Get Better"
 
# called when the page is loaded to start the timer checks
def runGame():
    global intervalHandle
    print("Running Game")
    document.addEventListener('keydown', checkKey)
    intervalHandle = window.setInterval(updatePosition, 300)
 

def handleWin():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "You didn't fail and ate {} grasshoppers!".format(bag[1])
#############################
# Main Program
#############################
 
runGame()
