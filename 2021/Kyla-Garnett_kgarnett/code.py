#############################
# Library Imports
#############################
from js import document, window

#############################
# Global Variables
#############################

# to store movement direction
xDir = 0
yDir = 0

# to store current column position & last cell contents
column = 0
row = 0
prev = "Empty"

# to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 0

coinsMax = 3
coinsCollected = 0

level = 0
speed = 300

# backup of table HTML for level restore
tableHTML = '''<tr>
            <td id="R0C0" class="Car"></td>
            <td id="R0C1"></td>
            <td id="R0C2"></td>
            <td id="R0C3"></td>
            <td id="R0C4" class="Coin"></td>
            <td id="R0C5" class="Wall"></td>
            <td id="R0C6"></td>
            <td id="R0C7"></td>
        </tr>
        <tr>
            <td id="R1C0"></td>
            <td id="R1C1" class="Wall"></td>
            <td id="R1C2"></td>
            <td id="R1C3"></td>
            <td id="R1C4"></td>
            <td id="R1C5"></td>
            <td id="R1C6" class="Wall"></td>
            <td id="R1C7"></td>
        </tr>
        <tr>
            <td id="R2C0"></td>
            <td id="R2C1"></td>
            <td id="R2C2"></td>
            <td id="R2C3"></td>
            <td id="R2C4" class="Wall"></td>
            <td id="R2C5"></td>
            <td id="R2C6"></td>
            <td id="R2C7" class="Wall"></td>
        </tr>
        <tr>
            <td id="R3C0" class="Wall"></td>
            <td id="R3C1"></td>
            <td id="R3C2"></td>
            <td id="R3C3" class="Wall"></td>
            <td id="R3C4"></td>
            <td id="R3C5" class="Wall"></td>
            <td id="R3C6"></td>
            <td id="R3C7" class="Wall"></td>
        </tr>
        <tr>
            <td id="R4C0"></td>
            <td id="R4C1"></td>
            <td id="R4C2" class="Coin"></td>
            <td id="R4C3"></td>
            <td id="R4C4" class="Wall"></td>
            <td id="R4C5"></td>
            <td id="R4C6"></td>
            <td id="R4C7"></td>
        </tr>
        <tr>
            <td id="R5C0"></td>
            <td id="R5C1" class="Wall"></td>
            <td id="R5C2"></td>
            <td id="R5C3"></td>
            <td id="R5C4"></td>
            <td id="R5C5"></td>
            <td id="R5C6" class="Flag"></td>
            <td id="R5C7"></td>
        </tr>
        <tr>
            <td id="R6C0" class="Coin"></td>
            <td id="R6C1"></td>
            <td id="R6C2"></td>
            <td id="R6C3"></td>
            <td id="R6C4" class="Wall"></td>
            <td id="R6C5" class="Wall"></td>
            <td id="R6C6"></td>
            <td id="R6C7"></td>
        </tr>'''

#############################
# Sub-Programs
#############################

# the function called when a key is pressed - sets direction variable
def checkKey(event):
    
    event.preventDefault()
    
    global xDir, yDir
    if event.keyCode == 39:
        # right arrow
        xDir = 1
        yDir = 0
    elif event.keyCode == 37:
        # left arrow
        xDir = -1
        yDir = 0
    elif event.keyCode == 38:
        #up arrow
        xDir = 0
        yDir = -1
    elif event.keyCode == 40:
        #down arrow
        xDir = 0
        yDir = 1

def getCell():
    return document.getElementById(f"R{row}C{column}")

# the timer check function - runs every 300 milliseconds to update the car position
def updatePosition():
    global column, row, prev
    if xDir != 0 or yDir != 0:
        # Set the cell where the car was to empty
        cell = getCell()
        cell.className = prev
        
        # Update the column position for the car
        column += xDir
        row += yDir
        
        # Re-draw the car (or report a crash)
        cell = getCell()
        prev = cell.className
        
        if cell.className == "Flag":
            handleWin()
        elif cell.className == "Coin":
            handleCoin()
        
        if cell and cell.className != "Wall":
            cell.className = "Car"
        else:
            handleCrash()

def resetBoard():
    global level, speed, xDir, yDir, column, row, prev, intervalHandle, coinsCollected
    level += 1
    speed = 300 - (level*50)
    xDir = 0
    yDir = 0
    column = 0
    row = 0
    coinsCollected = 0
    prev = "Empty"        
    document.getElementById("RacingTrack").innerHTML = tableHTML
    intervalHandle = window.setInterval(updatePosition, speed)
            
# if the car has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Oops you crashed..."
    resetBoard()
    
    
def handleCoin():
    global coinsCollected, prev
    coinsCollected += 1
    prev = "Empty"
    if coinsCollected == coinsMax:
        document.getElementById("Message").innerText = "You can now go to the mud puddle"
    else:
        document.getElementById("Message").innerText = "Cabbage collected"

def handleWin():
    global level, speed, xDir, yDir, column, row, prev, intervalHandle, coinsCollected
    if coinsCollected == coinsMax:
        window.clearInterval(intervalHandle)
        document.getElementById("Message").innerText = "WELL DONE! :), now try with a faster speed"
        resetBoard()
    else:
        document.getElementById("Message").innerText = "You need to collect all the cabbages first"

# called when the page is loaded to start the timer checks
def runGame():
    global intervalHandle
    print("Running Game")
    document.addEventListener('keydown', checkKey)
    intervalHandle = window.setInterval(updatePosition, speed)

#############################
# Main Program
#############################

runGame()
