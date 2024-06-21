#############################
# Library Imports
#############################
from js import document, window

#############################
# Global Variables
#############################

# to store current position (x,y)
position = [1, 1]
interval=300

# to store movement directions (x,y)
direction = [0, 0]

# to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 0

#############################
# Sub-Programs
#############################
carclass="carRight"
# the function called when a key is pressed - sets direction variable
direct="Right"
def checkKey(event):
    event.preventDefault()
    if event.key == "ArrowRight":
        direction[0]=1
        direction[1]=0
    elif event.key == "ArrowLeft":
        direction[0]=-1
        direction[1]=0
    elif event.key == "ArrowDown":
        direction[0]=0
        direction[1]=1
    elif event.key == "ArrowUp":
        direction[0]=0
        direction[1]=-1

def getCell():
    return document.getElementById(f"R{position[1]}C{position[0]}")

def getdirect():
    if direction==[0,1]:
        direct="Down"
    elif direction==[0,-1]:  
        direct="Up"
    elif direction==[1,0]:
        direct="Right"
    elif direction==[-1,0]:
        direct="Left"
    carclass=f"car{direct}"

# the timer check function - runs every 300 milliseconds to update the car position
def updatePosition():
    global direct, carclass
    getdirect()
    if direction[0] != 0 or direction[1] !=0:
        # Set the cell where the car was to empty
        cell = getCell() #get location
        cell.className = "" #wipe location
        
        # Update the column position for the car
        position[0] += direction[0]
        # Update the row postion for the car
        position[1] += direction[1]
        if position[0]==-1:position[0]=18
        if position[0]==19:position[0]=0

        # Re-draw the car (or report a crash)
        cell = getCell()
        if cell == None: #No cell there
            handleCrash()
        elif cell.className=="wall":
            position[0] -= direction[0]
            position[1] -= direction[1]
            direction[0] *= -1
            direction[1] *= -1
            getdirect()
            interval*=0.95
            cell=getCell()
        cell.className = f"{carclass}"
        

def out(a):
    document.getElementById("Message").innerText = a


# if the car has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Oops you crashed..."

# called when the page is loaded to start the timer checks
def runGame():
    global intervalHandle
    print("Running Game")
    document.addEventListener('keydown', checkKey)
    intervalHandle = window.setInterval(updatePosition, interval)

#############################
# Main Program
#############################

runGame()
