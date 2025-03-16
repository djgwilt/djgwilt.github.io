#############################
# Library Imports
#############################
from js import document, window

#############################
# Global Variables
#############################
difficulty= int(input('Speed of scrat (in blocks per second):'))
timelapse = 1000/difficulty
# to store movement direction
xDir = 0
yDir = 0
# to store current column position
column = 0
row = 0
# to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 0
carFlipped = False
acorns = 0
fakewall=0
won=False
#############################
# Sub-Programs
#############################

# the function called when a key is pressed - sets direction variable
def checkKey(event):
    event.preventDefault()
    global xDir, yDir, carFlipped
    if event.keyCode == 39:
        # right arrow
        xDir,yDir,carFlipped = 1,0,False
    elif event.keyCode == 37:
        # left arrow
        xDir,yDir,carFlipped = -1,0, True
    elif event.keyCode == 38:
        # left arrow
        xDir,yDir = 0,-1
    elif event.keyCode == 40:
        # left arrow
        xDir,yDir = 0,1

def getCell():
    return document.getElementById(f"R{row}C{column}")

# the timer check function - runs every 300 milliseconds to update the car position
def updatePosition():
    global column,row,acorns,carFlipped, difficulty,fakewall,won
    if xDir != 0 or yDir !=0:
        # Set the cell where the car was to empty
        cell = getCell()
        cell.className = "Empty"
        
        # Update the column position for the car
        column += xDir
        row += yDir
        # Re-draw the car (or report a crash)
        cell = getCell()
        if not cell or cell.className == "wall":
            handleCrash()
        elif cell.className == "flag":
            handleWin()
        elif cell.className == "rudy":
            handleDeath()
        elif cell.className == "acorn":
            document.getElementById("acorn").volume = 1.0
            document.getElementById("acorn").play()
            cell.className = ("CarFlipped" if carFlipped else "Car")
            acorns += 1
        elif cell.className == "fakewall":
            cell.className = ("CarFlipped" if carFlipped else "Car")
            fakewall += 1
        elif cell.className == "scratte":
            document.getElementById("scratte").volume = 1.0
            document.getElementById("scratte").play()
            cell.className = ("CarFlipped" if carFlipped else "Car")
        else:
            cell.className = ("CarFlipped" if carFlipped else "Car")

# if the car has gone off the table, this tidies up including crash message
def handleCrash():
    document.getElementById("crash").volume = 1.0
    document.getElementById("crash").play()
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = f"Oops you crashed... but you got {acorns} acorns"
    
def handleDeath():
    document.getElementById("rudy").volume = 1.0
    document.getElementById("rudy").play()
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Oops you dead bro!"
    
def handleWin():
    global difficulty
    document.getElementById("win").volume = 1.0
    document.getElementById("win").play()
    window.clearInterval(intervalHandle)
    allthe = (str(acorns)if acorns<7 else 'all of the')
    allthe1 = (str(fakewall)if fakewall<=2 else 'all of the')
    allthe2=str((acorns+8*fakewall)*difficulty)
    document.getElementById("Message").innerText = f"Whoa Nelly! You won! You also gained {allthe} acorns! You also spotted {allthe1} fake walls. Points scored: {allthe2}"

# called when the page is loaded to start the timer checks
def runGame():
    document.getElementById("back").volume = 0.25
    document.getElementById("back").play()
    global intervalHandle, timelapse
    print("Running Game")
    document.addEventListener('keydown', checkKey)
    intervalHandle = window.setInterval(updatePosition, timelapse)

#############################
# Main Program
#############################
runGame()
