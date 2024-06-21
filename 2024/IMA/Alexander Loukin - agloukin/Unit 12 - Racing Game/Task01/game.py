#############################
# Library Imports
#############################
from js import document, window, console
import random

#############################
# Global Variables
#############################

chosen_x = 0
chosen_y = 0

# to store current position (x,y)
position = [0, 0]
enemy_position = [11, 5]

# to store movement directions (x,y)
direction = [0, 0]
enemy_direction = [0, 0]

# to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 0

#############################
# Sub-Programs
#############################

# the function called when a key is pressed - sets direction variable
def checkKey(event): 
    event.preventDefault()  # this will prevent the down arrow from scrolling the page 
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

def enemyMove():
    cell = getEnemyCell()
    cell.className = ""
    enemy_direction = [0,0]
    x_distance = enemy_position[0] - position[0]
    y_distance = enemy_position[1] - position[1]


    if abs(x_distance) > abs(y_distance):
        if x_distance > 0:
            enemy_direction[0] = -1
        else:
            enemy_direction[0] = 1
    else:
        if y_distance > 0:
            enemy_direction[1] = -1
        else:
            enemy_direction[1] = 1
    


    enemy_position[0] += enemy_direction[0] 
    enemy_position[1] += enemy_direction[1]












    




def getCell(): 
    return document.getElementById("R{}C{}".format(position[1], position[0])) 

def getChosenCell(): 
    return document.getElementById("R{}C{}".format(chosen_y, chosen_x)) 

def getEnemyCell():
    return document.getElementById("R{}C{}".format(enemy_position[1], enemy_position[0])) 
# the timer check function - runs every 300 milliseconds to update the car position
# the timer check function - runs every 300 milliseconds to update the car position 

def updatePosition(): 




    if direction[0] != 0 or direction[1] != 0: 
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
        elif cell.className == "wall" or cell.className == "enemy":
            cell.className = "hybrid"
            handleCrash()
        else:
            cell.className = "car" 

    enemyMove()
    cell = getEnemyCell()
    if cell == None: 
        handleCrash() 
    elif cell.className == "car":
        cell.className = ""
        handleCrash()
    elif cell.className == "wall":
        enemy_position[0] -= enemy_direction[0]
        enemy_position[1] -= enemy_direction[1]
        cell = getEnemyCell()
    else:
        cell.className = "enemy" 
    cell.className = "enemy"


# if the car has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "blud crashed"


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
