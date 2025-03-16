#############################
# Library Imports
#############################
import random
import time
from js import document, window

#############################
# Global Variables
#############################

# to store current position (x,y)
position = [2, 2]

# to store movement directions (x,y)
direction = [0, 0]

enemy = []
enemy_move = 0 # only move the enemy every other move

ORIG_MOVE_TIME = 400
TIME_DECREASE = 10 # how much the time decreases when you collect a coin
# to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 0

width = 5
height = 5

lives = 5
collided = 0
coins = 0
move_time = 400 # smaller -> greater speed

#############################
# Sub-Programs
#############################

def resetTrack(width, height):
    myTrackComplete = [[9, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0],
                        [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
                        [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0],
                        [0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
                        [0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0],
                        [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0],
                        [1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1],
                        [0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
                        [0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1],
                        [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
                        [0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1],
                        [0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1],
                        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1],
                        [0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                        [0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0],
                        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0]]
    myTrack = [myTrackComplete[r][:width] for r in range(height)]
    for _ in range(2): # 2 squares padding
        for index in range(len(myTrack)):
            myTrack[index].insert(0,1)
            myTrack[index].append(1)
    for _ in range(2):
        myTrack.insert(0, [1 for c in range(width+4)])
        myTrack.append([1 for c in range(width+4)])
    
    return myTrack

def resetVariables(_coins=0, _lives=5):
    global position, direction, coins, move_time, myTrack, lives, width, height, enemy, enemy_move
    #time.sleep(1)
    # to store current position (x,y)
    position = [2, 2]

    # to store movement directions (x,y)
    direction = [0, 0]
    coins = _coins
    move_time = ORIG_MOVE_TIME-TIME_DECREASE*coins
    if lives == 0:
        width = 5
        height = 5
        move_time = ORIG_MOVE_TIME
        enemy = []
        enemy_move = 0
    lives = _lives
     # smaller -> greater speed
    myTrack = resetTrack(width, height)
    drawTrack()
    # if enemy:
    #     addEnemy()
    addCoin()
    displayCoinsAndLives()


# the function called when a key is pressed - sets direction variable
def checkKey(event):
    global direction
    event.preventDefault()
    if event.key == "ArrowRight":
        direction = [1, 0]
    elif event.key == "ArrowLeft":
        # left arrow
        direction = [-1, 0]
    elif event.key == "ArrowDown":
        direction = [0, 1]
    elif event.key == "ArrowUp":
        direction = [0, -1]

def addEnemy():
    global enemy
    row = random.randrange(height)
    col = random.randrange(width)
    
    while not (document.getElementById(f"R{row}C{col}").className == "empty" and row > 5 and col > 5): 
        row = random.randrange(height)
        col = random.randrange(width)
    #print(row, col)
    document.getElementById(f"R{row}C{col}").className = "enemy"
    enemy = [col, row]

def addCoin():
    #print(width, height)
    row = random.randrange(height)
    col = random.randrange(width)
    #print(row, col)
    while document.getElementById(f"R{row}C{col}").className != "empty": 
        row = random.randrange(height)
        col = random.randrange(width)
    document.getElementById(f"R{row}C{col}").className = "coin"

def displayCoinsAndLives():
    document.getElementById("Message").innerText = f"coins: {coins} #||# lives: {lives}"

def getCell():
    return document.getElementById("R{}C{}".format(position[1], position[0]))

def extendTrack():
    global move_time
    resetTrack(width, height)
    resetVariables(coins, lives)
    move_time = max(100, ORIG_MOVE_TIME-TIME_DECREASE*coins)

def extendMap(coins):
    global width, height, intervalHandle
    #print(coins)
    extend = False
    if coins == 1:
        width = 10
        height = 10
        extend = True
    elif coins == 2:
        width = 15
        height = 15
        extendTrack()
        addEnemy()
        window.clearInterval(intervalHandle)
        intervalHandle = window.setInterval(updateGame, move_time)
        return
    elif coins == 15:
        width = 20
        height = 20
        extendTrack()
        addEnemy()
        window.clearInterval(intervalHandle)
        intervalHandle = window.setInterval(updateGame, move_time)
        extend = True
    
    if extend:
        extendTrack()

def enemy_search(dy, dx):
    return document.getElementById(f"R{enemy[1]+dy}C{enemy[0]+dx}").className

def moveEnemy():
    global enemy
    moved = False
    document.getElementById(f"R{enemy[1]}C{enemy[0]}").className = "empty"
    priority = []
    x_diff = enemy[0] - position[0]
    y_diff = enemy[1] - position[1]
    if x_diff > 0: # enemy to the right of the player
        priority.insert(0,"left")
        priority.append("right") # right goes at the end of the priority list
    elif x_diff < 0: # enemy to the left of the player
        priority.insert(0,"right")
        priority.append("left")
    else:
        priority.append("left")
        priority.append("right")
    if y_diff > 0: # enemy below the player
        priority.insert(0,"up")
        priority.append("down")
    elif y_diff < 0: # enemy above the player
        priority.insert(0,"down")
        priority.append("up")
    else:
        priority.append("up")
        priority.append("down")
    i = 0
    while not moved:
        if priority[i] == "right":
            # possible teleportation through walls
            if enemy_search(0,1) == "empty":
                enemy[0] += 1
                moved = True
            elif (enemy_search(0,1) == "wall" and enemy_search(0,2) == "empty"):
                enemy[0] += 2
                moved = True
        elif priority[i] == "left":
            if enemy_search(0,-1) == "empty":
                enemy[0] -= 1
                moved = True
            elif (enemy_search(0,-1) == "wall" and enemy_search(0,-2) == "empty"):
                enemy[0] -= 2
                moved = True
        elif priority[i] == "down":
            if enemy_search(1,0) == "empty":
                enemy[1] += 1
                moved = True
            elif (enemy_search(1,0) == "wall" and enemy_search(2,0) == "empty"):
                enemy[1] += 2
                moved = True
        elif priority[i] == "up":
            if enemy_search(-1,0) == "empty":
                enemy[1] -= 1
                moved = True      
            elif (enemy_search(-1,0) == "wall" and enemy_search(-2,0) == "empty"):
                enemy[1] -= 2 
                moved = True
        i += 1

    document.getElementById(f"R{enemy[1]}C{enemy[0]}").className = "enemy"

# the timer check function - runs every 300 milliseconds to update the car position
def updateGame():
    global position, coins, direction, move_time, intervalHandle, enemy_move
    global collided
    if collided == 1:
        move_time = 1000
        collided = 2
        if lives == 0:
            move_time = 5000 # wait longer when game over
            document.getElementById("Message").innerText = f"GAME OVER... Your score was {coins}"
        return
    elif collided == 2:
        collided = 0
        handleCrash()
        return
    #print("H")

    if direction != [0, 0]:
        # Set the cell where the car was to empty
        cell = getCell()
        cell.className = "empty"
        
        # Update the column position for the car
        position[0] += direction[0]
        # Update the row position for the car
        position[1] += direction[1]

        # Re-draw the car (or report a crash)
        cell = getCell()
        if cell == None:
            handleCrash()
        # elif cell.className == "wall":
        #     position[0] -= direction[0] # go back
        #     position[1] -= direction[1]
        #     getCell().className = "player"
        #     direction = [0, 0] # become stationary
        elif cell.className in ["wall", "enemy"]:
            cell.className = "explosion"
            collided = 1
            window.clearInterval(intervalHandle)
            intervalHandle = window.setInterval(updateGame, move_time)
            #handleCrash()
            return
        elif cell.className == "coin":
            coins += 1
            move_time = max(100, move_time-TIME_DECREASE)
            displayCoinsAndLives()
            cell.className = "player"
            addCoin()
            extendMap(coins)
        else:
            cell.className = "player"
        
    if enemy and enemy_move == 0:
        enemy_move = 1
        moveEnemy()
    elif enemy_move == 1:
        enemy_move = 0

    window.clearInterval(intervalHandle)
    intervalHandle = window.setInterval(updateGame, move_time)

# if the car has gone off the table, this tidies up including crash message
def handleCrash():
    global intervalHandle, lives, move_time

    window.clearInterval(intervalHandle)
    if lives == 1:
        lives = 0
        #document.getElementById("Message").innerText = f"Oops you crashed... Your score was {coins}"
        resetVariables()
        intervalHandle = window.setInterval(updateGame, move_time)
    else:
        lives -= 1
        displayCoinsAndLives()
        resetVariables(coins, lives)
        move_time = max(100, ORIG_MOVE_TIME-TIME_DECREASE*coins)
        intervalHandle = window.setInterval(updateGame, move_time) # when you lose a life but not game over, the speed stays the same

# called when the page is loaded to start the timer checks

def convertTrack(myTrack):
    '''converts the numbers in the track to the names of the objects they represent'''
    convert = {0: "empty", 1: "wall", 2: "coin", 9: "player"}
    for rowx, row in enumerate(myTrack): #rowx in the row number, row is the actual values of the row
        for colx, col in enumerate(row):
            val = myTrack[rowx][colx]
            myTrack[rowx][colx] = convert[val]
    return myTrack
            

def drawTrack():
    global myTrack
    myTrack = convertTrack(myTrack) # so the html code can be edited
    trackHTML = ""
    for rowx, row in enumerate(myTrack):
        trackHTML += "<tr>"
        for colx, col in enumerate(row):
            trackHTML += f"<td id='R{rowx}C{colx}' class='{myTrack[rowx][colx]}'></td>"
        trackHTML += "</tr>"
    document.getElementById("RacingTrack").innerHTML = trackHTML


def runGame():
    global intervalHandle, move_time
    print("Running Game")
    document.addEventListener('keydown', checkKey)
    intervalHandle = window.setInterval(updateGame, move_time)

#############################
# Main Program
#############################


resetVariables()
runGame()
