#############################
# Library Imports
#############################
from js import document, window
from pyodide.ffi import create_proxy

#############################
# Global Variables
#############################

# to store current position (x,y)
position = [2, 4]
pos2 = [0,4]
# to store movement directions (x,y)
direction = [0, 0]
dir2 = [0,0]

bag = [2, 0]
bag2 = [2,0]

# to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 0
intervalHandle2 = 0

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
        direction[1] = 1
        direction[0] = 0
    elif event.key == "ArrowUp":
        direction[1] = -1
        direction[0] = 0
def checkKey2(event):
    event.preventDefault()
    if event.key == "d":
        dir2[0] = 1
        dir2[1] = 0
    elif event.key == "a":
        # left arrow
        dir2[0] = -1
        dir2[1] = 0
    elif event.key == "s":
        dir2[1] = 1
        dir2[0] = 0
    elif event.key == "w":
        dir2[1] = -1
        dir2[0] = 0
    
#def checkShift(event):
#    global intervalsize2
#    event.preventDefault()
#    right_shift_pressed = event.getModifierState("Shift") and event.code == "ShiftRight"
#    if not right_shift_pressed:
#        intervalsize2 = 250
#        
#    else:
#        intervalsize2 = 300
        
#def checkShift2(event):
#    global intervalsize
#    event.preventDefault()
#    right_shift_pressed = event.getModifierState("Shift") and event.code == "ShiftRight"
#    if right_shift_pressed:
#        intervalsize = 250
#        
#    else:
#        intervalsize = 300

def getCell():
    return document.getElementById("R{}C{}".format(position[1], position[0]))
def getCell2():
    return document.getElementById("R{}C{}".format(pos2[1], pos2[0]))

def handleWin():
    window.clearInterval(intervalHandle)
    window.clearInterval(intervalHandle2)
    document.getElementById("Message").innerText = "player 1 Wins and collected {} coins!".format(bag[1])
    
def handleWin2():
    window.clearInterval(intervalHandle)
    window.clearInterval(intervalHandle2)
    document.getElementById("Message").innerText = "Player 2 Wins and collected {} coins!".format(bag[1])
    
# the timer check function - runs every 300 milliseconds to update player1's position
def upPos2():
    if dir2[0] != 0 or dir2[1] != 0:
        cell2 = getCell2()
        
        player2Class = "player2"
        cell2.className = ""
        
        pos2[0] += dir2[0]
        pos2[1] += dir2[1]
        
        cell2 = getCell2()
        
        if cell2 == None:
            handleCrash()
        elif cell2.className == "wall":
            handleCrash()
        elif cell2.className == "player1":
            handleCrash()
        elif cell2.className == "coin":
            cell2.className = player2Class
            bag[1] = bag[1] + 1
        elif cell2.className == "flag":
            if direction[1] == 1 or direction[0] == 1 or direction[0] == -1:
                handleCrash()
            else:
                cell2.className = player2Class
                bag2[0] = bag2[0] - 1
                if bag2[0] == 0:
                    handleWin2()
        
        else:
            cell2.className = player2Class
        
def updatePosition():
    if direction[0] != 0 or direction[1] != 0:
        # Set the cell where player1 was to empty
        cell = getCell()
        
        player1Class = "player1"
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
        elif cell.className == "player2":
            handleCrash()
        elif cell.className == "coin":
            cell.className = player1Class
            bag[1] = bag[1] + 1
        elif cell.className == "flag":
            if direction[1] == 1 or direction[0] == 1 or direction[0] == -1:
                handleCrash()
            else:
                cell.className = player1Class
                bag[0] = bag[0] - 1
                if bag[0] == 0:
                    handleWin()
        else:
            cell.className = player1Class
            
            

# if player1 has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    window.clearInterval(intervalHandle2)
    document.getElementById("Message").innerText = "Oops you crashed..."

# called when the page is loaded to start the timer checks
#def restartIntervals():
 #   global intervalHandle, intervalHandle2
  #  # Clear the existing intervals
    
   # intervalHandle = window.setInterval(create_proxy(updatePosition), intervalsize)
    
    # Set new intervals with the updated interval sizes
    
    #intervalHandle2 = window.setInterval(create_proxy(upPos2), intervalsize2)
    
def runGame():
    global intervalHandle
    global intervalHandle2
    global intervalsize
    global intervalsize2
    #global restartIntervals
    intervalsize = 300
    intervalsize2 = 300
    
    print("Running Game")
    document.addEventListener('keydown', create_proxy(checkKey))
    document.addEventListener('keydown', create_proxy(checkKey2))
    intervalHandle = window.setInterval(create_proxy(updatePosition), intervalsize)
    intervalHandle2 = window.setInterval(create_proxy(upPos2), intervalsize2)
    
    #document.addEventListener('keydown', create_proxy(checkShift))
    #document.addEventListener('keydown', create_proxy(checkShift2))
    

#############################
# Main Program
#############################

runGame()
