#############################
# Library Imports
#############################
from js import document, window

#############################
# Global Variables
#############################

# to store current position (x,y)
position = [0, 0]
position2 = [7, 7]
position3 = [0, 5]
position4 = [7, 3]
# to store movement directions (x,y)
direction = [0, 0]
direction2 = [0, 0]
direction3 = [1, 0]
direction4 = [-1, 0]
# to store the handle code for the timer interval to cancel it when we crash
intervalHandle= 0
intervalHandle2 = 0
intervalHandle3 = 0
intervalHandle4  = 0
# to store number of coins
coins = 0
coins2 = 0

import time

audioPirate = document.getElementById("audioPirate")
audioFail = document.getElementById("audioFail")

count = 0
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
    elif event.key == "w":
        direction[0] = 0
        direction[1] = -1
    elif event.key == "s":
        direction[0] = 0
        direction[1] = 1
    if event.key == "ArrowRight":
        direction2[0] = 1
        direction2[1] = 0
    elif event.key == "ArrowLeft":
        # left arrow
        direction2[0] = -1
        direction2[1] = 0
    elif event.key == "ArrowUp":
        direction2[0] = 0
        direction2[1] = -1
    elif event.key == "ArrowDown":
        direction2[0] = 0
        direction2[1] = 1
def getCell():
    return document.getElementById("R{}C{}".format(position[1], position[0]))

def getCell2():
    return document.getElementById("R{}C{}".format(position2[1], position2[0]))

def getCell3():
    return document.getElementById("R{}C{}".format(position3[1], position3[0]))

def getCell4():
    return document.getElementById("R{}C{}".format(position4[1], position4[0]))

# the timer check function - runs every 300 milliseconds to update the car position
def updatePosition():
    global coins
    if direction[0] != 0 or direction[1] != 0:
        # Set the cell where the car was to empty
        cell = getCell()
        oldCell = getCell()
        cell.className = ""
        
        # Update the column position for the car
        position[0] += direction[0]
        position[1] += direction[1]
        # Re-draw the car (or report a crash)
        cell = getCell()
        if cell == None:
            handleCrash()
            oldCell.className = "peppacrash"
        elif cell.className == "sand": 
            handleCrash()
            oldCell.className = "peppacrash"
        elif cell.className == "duck": 
            handleCrash()
            oldCell.className = "peppacrash"
        elif cell.className == "duck2": 
            handleCrash()
            oldCell.className = "dannycrash"
            cell.className = "duck"
        elif cell.className == "coin":
            cell.className = "peppa"
            coins = coins + 1
        else:
            cell.className = "peppa"

def updatePosition2():
    global coins2
    if direction2[0] != 0 or direction2[1] != 0:
        # Set the cell where the car was to empty
        cell2 = getCell2()
        oldCell2 = getCell2()
        cell2.className = ""
        
        # Update the column position for the car
        position2[0] += direction2[0]
        position2[1] += direction2[1]
        # Re-draw the car (or report a crash)
        cell2 = getCell2()
        if cell2 == None:
            handleCrash()
            oldCell2.className = "dannycrash"
        elif cell2.className == "sand": 
            handleCrash()
            oldCell2.className = "dannycrash"
            cell2.className = "sand"
        elif cell2.className == "duck": 
            handleCrash()
            oldCell2.className = "dannycrash"
            cell2.className = "duck"
        elif cell2.className == "duck2": 
            handleCrash()
            oldCell2.className = "dannycrash"
            cell2.className = "duck"
        elif cell2.className == "coin":
            cell2.className = "danny"
            coins2 = coins2 + 1
        else:
            cell2.className = "danny"
  
def duckmove():
    cell3 = getCell3()
    oldCell3 = getCell3()
    cell3.className = ""
    position3[0] += direction3[0]
    cell3 = getCell3()
    cell3.className = "duck"
    oldCell3.className = ""
    if position3[0] == 7:
        direction3[0] = -1
    elif position3[0] == 0:
        direction3[0] = 1

def duckmove2():
    cell4 = getCell4()
    oldCell4 = getCell4()
    cell4.className = ""
    position4[0] += direction4[0]
    cell4 = getCell4()
    cell4.className = "duck2"
    oldCell4.className = ""
    if position4[0] == 7:
        direction4[0] = -1
    elif position4[0] == 0:
        direction4[0] = 1

# if the car has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    window.clearInterval(intervalHandle2)
    window.clearInterval(intervalHandle3)
    window.clearInterval(intervalHandle4)
    audioFail.play()
    print("Player 1 finished with {} coins and Player 2 finished with {} coins".format(coins, coins2))

# called when the page is loaded to start the timer checks
def runGame():
    global intervalHandle
    global intervalHandle2
    global intervalHandle3
    global intervalHandle4
    print("Running Game")
    document.addEventListener('keydown', checkKey)
    intervalHandle = window.setInterval(updatePosition, 300)
    intervalHandle2 = window.setInterval(updatePosition2, 300)
    intervalHandle3 = window.setInterval(duckmove, 300)
    intervalHandle4 = window.setInterval(duckmove2, 300)
    audioPirate.play()
    audioPirate.addEventListener("ended", on_Pirate_ended)

def on_Pirate_ended(*args):
    audioPirate.play()
    
#############################
# Main Program
#############################

runGame()
