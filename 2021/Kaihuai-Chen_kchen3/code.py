#############################
# Library Imports
#############################
from js import document, window

#############################
# Global Variables
COINSMAX = 3
coins_collected= 0
score = 0 

#############################

# to store movement direction
xDir = 0
yDir = 0 
# to store current column position
column = 0
row = 0 
# to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 0
#carflip 
carFlipped = False 

#############################
# Sub-Programs
#############################

# the function called when a key is pressed - sets direction variable
def checkKey(event):
    global xDir , yDir , carFlipped 
    if event.keyCode == 39:
        # right arrow
        xDir = 1
        yDir = 0 
        carFlipped = False 
    elif event.keyCode == 37:
        # left arrow
        xDir = -1
        yDir = 0 
        CarFlipped = True  
    elif event.keyCode == 38 : 
        yDir = -1 
        xDir = 0 
    elif event.keyCode == 40 : 
        yDir = 1
        xDir = 0 
def getCell():
    return document.getElementById(f"R{row}C{column}")

# the timer check function - runs every 300 milliseconds to update the car position
def getCoin() : 
    global coins_collected , score 
    coins_collected += 1
    score += 1 
def updatePosition():
    global column , row 
    if xDir != 0 or yDir != 0 : 
        # Set the cell where the car was to empty
        cell = getCell()
        cell.className = "Empty"
        
        # Update the column position for the car
        column += xDir
        row += yDir
        # Re-draw the car (or report a crash)
        cell = getCell()
        if not cell : 
            handleCrash()
        elif cell.className  == "Wall":
            handleCrash()
        elif cell.className == "flag" : 
            if coins_collected == COINSMAX : 
                handleWin()
        
        elif cell.className =="coin" : 
            getCoin()
        else  :     
            cell.className == "Car"
        
        
        if cell and cell.className != "Wall" : 
            cell.className = "Car"
        else:
            handleCrash()

# if the car has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Oops you crashed..."

# called when the page is loaded to start the timer checks
def runGame():
    global intervalHandle
    print("Running Game")
    print(score)
    
    document.addEventListener('keydown', checkKey)
    intervalHandle = window.setInterval(updatePosition, 300)
#
def handleWin():  
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "WELL DONE , YOU'VE WON  "

#############################
# Main Program
#############################

runGame()
