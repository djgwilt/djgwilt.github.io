#############################
# Library Imports
#############################
from js import document, window
from pyodide.ffi import create_proxy

#############################
# Global Variables
#############################

# to store current position (column, row)
position = [0, 0]
position2 = [12, 0]

# to store movement directions (left-right, up-down)
direction = [0, 0]
direction2 = [0, 0]

# to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 0
bag = 0

win = 0
win2 = 0

x = 300

#############################
# Sub-Programs
#############################

# the function called when a key is pressed - sets direction variable
def checkKey(event):
    event.preventDefault()
    if event.key == "ArrowRight":
        direction2[0] = 1
        direction2[1] = 0
    elif event.key == "ArrowLeft":
        direction2[0] = -1
        direction2[1] = 0
    elif event.key == "ArrowUp":
        direction2[0] = 0
        direction2[1] = -1
    elif event.key == "ArrowDown":
        direction2[0] = 0
        direction2[1] = 1
    
    elif event.key == "d":
        direction[0] = 1
        direction[1] = 0
    elif event.key == "a":
        direction[0] = -1
        direction[1] = 0
    elif event.key == "w":
        direction[0] = 0
        direction[1] = -1
    elif event.key == "s":
        direction[0] = 0
        direction[1] = 1
        

def getCell():
    return document.getElementById("R{}C{}".format(position[1], position[0]))

def getCell2():
    return document.getElementById("R{}C{}".format(position2[1], position2[0]))

# the timer check function - runs every 300 milliseconds to update player1's position
def updatePosition():
    global bag
    if (direction[0] != 0 or direction[1] != 0) and win != 1:
        # Set the cell where player1 was to empty
        cell = getCell()
        cell.className = ""
        
        # Update the column position for player1
        position[0] += direction[0]
        position[1] += direction[1]

        # Re-draw player1 (or report a crash)
        cell = getCell()
        if cell == None:
            handleCrash()
        elif cell.className == "wall":
            handleCrash()
        elif cell.className == "coin":
            cell.className = "player1"
            bag = bag + 1
        elif cell.className == "flag1":
            handleWin()
        elif cell.className == "flag2":
            handleWrongflag()
        #elif cell.className == "speedup":
            #speedup()
            #cell.className = "player1"
        else:
            cell.className = "player1"

    if (direction2[0] != 0 or direction2[1] != 0) and win2 != 1:
        cell = getCell2()
        cell.className = ""

        position2[0] += direction2[0]
        position2[1] += direction2[1]

        cell = getCell2()
        if cell == None:
            handleCrash()
        elif cell.className == "wall":
            handleCrash2()
        elif cell.className == "coin":
            cell.className = "player2"
            bag = bag + 1
        elif cell.className == "flag1":
            handleWrongflag()
        elif cell.className == "flag2":
            handleWin2()
        #elif cell.className == "speedup":
            #speedup()
            #cell.className = "player2"
        else:
            cell.className = "player2"

# if player1 has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    if win != 1:
        if bag == 0:
            document.getElementById("Message").innerText = "Oops you crashed... you didn't even collect any candy."
        elif bag < 4:
            document.getElementById("Message").innerText = "Oops you crashed... you only collected {} candy.".format(bag)
        else:
            document.getElementById("Message").innerText = "Oops you crashed... you collected {} candy, though.".format(bag)
        

def handleCrash2():
    if win2 != 1:
        window.clearInterval(intervalHandle)
        if bag == 0:
            document.getElementById("Message").innerText = "Oops you crashed... you didn't even collect any candy."
        elif bag < 4:
            document.getElementById("Message").innerText = "Oops you crashed... you only collected {} candy.".format(bag)
        else:
            document.getElementById("Message").innerText = "Oops you crashed... you collected {} candy, though.".format(bag)

        

def handleWrongflag():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "That's not the right flag for you... you collected {} candy, though.".format(bag)

def handleWin():
    global win 
    global win2
    win = win + 1
    if win == 1 and win2 == 1:
        window.clearInterval(intervalHandle)
        document.getElementById("Message").innerText = "You win and collected {} candy!".format(bag) 
    else:
        document.getElementById("Message").innerText = "Only one more left! {} candy so far!".format(bag)

def handleWin2():
    global win
    global win2
    win2 = win2 + 1
    if win2 == 1 and win == 1:
        window.clearInterval(intervalHandle)
        document.getElementById("Message").innerText = "You win and collected {} candy!".format(bag)
    else:
        document.getElementById("Message").innerText = "Only one more left! {} candy so far!".format(bag) 

# def speedup():


# called when the page is loaded to start the timer checks
def runGame():
    global intervalHandle
    print("Running Game")
    document.addEventListener('keydown', create_proxy(checkKey))
    intervalHandle = window.setInterval(create_proxy(updatePosition), 300)

#############################
# Main Program
#############################

runGame()
