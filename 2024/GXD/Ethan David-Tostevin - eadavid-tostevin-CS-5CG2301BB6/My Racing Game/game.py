#############################
# Library Imports
#############################
from js import document, window, jQuery
from pyodide.ffi import create_proxy, to_js
import random
#############################
# Global Variables
#############################

# to store current position (x,y)
positions = [[0, 0]]

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
    elif event.key == "ArrowDown":
        direction[1] = 1
        direction[0] = 0
    elif event.key == "ArrowUp":
        direction[1] = -1
        direction[0] = 0

def getCellXY(x, y):
    return document.getElementById("R{}C{}".format(y, x))



def updatePosition():
    if direction[0] != 0 or direction[1] != 0:
        position = list(positions[-1])
        
        # Update the column position for player1
        position[0] = position[0] + direction[0]
        position[1] = position[1] + direction[1]
        positions.append(position)

        # Re-draw player1 (or report a crash)
        cell = getCellXY(int(position[0]), int(position[1]))
        if cell == None:
            handleCrash()
        elif cell.className == "wall":
            handleCrash()
        elif cell.className == "player1":
            handleCrash()
        elif cell.className == "food":
            cell.className = "player1"
            givePoint()
            generateFood()
        else:
            #cell.className = "player1"
            cellRect = cell.getBoundingClientRect()
            tableRect = document.getElementById("RacingTrack").getBoundingClientRect()
            jQuery("#player1").animate(to_js({
                "left": f"{cellRect.x-tableRect.x+2}px",                                                                                                                
                "top": f"{cellRect.y-tableRect.y+2+42}px"}),
                300 - score*2, "linear")
            tail = positions.pop(0)
            cell = getCellXY(tail[0], tail[1])
            cell.className = ""
            for i in range(len(positions)-1):
                p = positions[i]
                cell = getCellXY(p[0], p[1])
                cell.className = "player1"



# if player1 has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = f"GAME OVER Score: {score}"

# called when the page is loaded to start the timer checks
def runGame():
    global intervalHandle
    print("Running Game")
    document.addEventListener('keydown', create_proxy(checkKey))
    intervalHandle = window.setInterval(create_proxy(updatePosition), 300 - score*2)

# Global variable to store the score
score = 0

def givePoint():
    global score
    # Increment the score when the player hits food
    score += 1
    #print(f"Score: {score}")
    document.getElementById("Message").innerText = f"Score: {score}"
    if score >= 100:
        handleWin()
def generateFood():
    # Get a random position for the food cell
    food_x = random.randint(0, 9)
    food_y = random.randint(0, 9)
    
    # Check if the chosen position is already occupied by player1 or a wall
    while getCellXY(food_x, food_y).className != "":
        food_x = random.randint(0, 9)
        food_y = random.randint(0, 9)
    
    # Set the food cell at the chosen position
    #document.getElementById(food_cords)
    getCellXY(food_x, food_y).className = "food"


def handleWin():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = f"You Won! Final score: {score}"
#############################
# Main Program
#############################


runGame()
