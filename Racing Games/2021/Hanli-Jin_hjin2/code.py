#############################
# Library Imports
#############################

from js import document, window
import random
import time
import math
#############################
# Global Variables
#############################
gameOver = False
score = 0
# to store movement direction
xDir = 0
# to store current column position
playerX = 3
playerY = 11
lives = 10
newId = ''
projectiles = []
projSpeed = 800
projSpawn = 1500
lastSpeed = 0
lastSpawn = 0
speedLimit = 0
speedMultiplier = 1
spawnMultiplier = 1
toRemove = []
#############################
# DIFFICULTY 
easy = True
medium = False
hard = False
hardcore = False
incspeed = False
# HIGHSCORES
higheasy = 0
highmed = 0
highhard = 0
highcore = 0
#############################
# Sub-Programs
#############################
    
def init_player():
    cell = getCell(playerX, playerY)
    cell.className = 'player'

def send_projectile():
    global projectiles
    projX = random.randint(0, 5)
    projY = 0
    projectiles.append([projX, projY])
    cell = getCell(projX, projY)
    cell.className = "Projectile"

def move_projectiles():
    global projectiles
    global toRemove
    global lives
    toRemove = []
    for i in projectiles:
        cell = getCell(i[0], i[1])
        cell.className = 'Empty'
        i[1] += 1
        if i[1] == 11:
            if (i[0], i[1]) == (playerX, playerY):
                handle_catch(i[0], i[1])
                continue
            #handle_miss()
            lives -= 1
            global newId
            
            if lives == 3:
                newId = "ThreeLives"
            elif lives == 2:
                newId = "TwoLives"
            elif lives == 1:
                newId = "OneLife"
            document.getElementById("Lives").className = newId
            toRemove.append([i[0], i[1]])
            cell = getCell(i[0], i[1])
            cell.className = 'Empty'
            continue
            
        cell = getCell(i[0], i[1])
        cell.className = 'Projectile'
        
        update_lives()
    for i in toRemove:
        projectiles.remove(i)
    
def handle_catch(projX, projY):
    global projectiles
    global score
    global projSpeed
    global projSpawn
    global intervalHandle3
    global intervalHandle4
    global toRemove
    global lastSpawn
    global lastSpeed
    toRemove.append([projX, projY])
    score += 1
    
    if projSpeed > speedLimit:
        projSpeed *= speedMultiplier
        window.clearInterval(intervalHandle4)
        intervalHandle4 = window.setInterval(move_projectiles, projSpeed)
    if projSpawn > 500:
        projSpawn *= spawnMultiplier
        window.clearInterval(intervalHandle3)
        intervalHandle3 = window.setInterval(send_projectile, projSpawn)
    else:
        projSpawn = 500
        
    if speedMultiplier != 1:
        lastSpeed = projSpeed
        lastSpawn = projSpawn
        document.getElementById("projspeed").innerHTML = f"Speed: {projSpeed:.0f}"
        document.getElementById("projspawn").innerHTML = f"Spawn: {projSpawn:.0f}"
    update_score()
    
def checkKeyDown(event):
    global xDir
    if event.keyCode == 68:
        # right 
        xDir = 1
    elif event.keyCode == 65:
        # left 
        xDir = -1
    if event.keyCode == 37:
        xDir = -1
    elif event.keyCode == 39:
        xDir = 1

def checkKeyUp(event):
    global xDir
    if event.keyCode == 68 or event.keyCode == 65 or event.keyCode == 37 or event.keyCode == 39:
        xDir = 0
    
def getCell(x, y):
    return document.getElementById(f"R{y}C{x}")
    
def update_score():
    document.getElementById("Score").innerHTML = f"Score: {score}"

def update_highscore():
    if easy:
        document.getElementById("Higheasy").innerHTML = f"Easy: {higheasy}"
    elif medium:
        document.getElementById("Highmed").innerHTML = f"Medium: {highmed}"
    elif hard:
        document.getElementById("Highhard").innerHTML = f"Hard: {highhard}"
    elif hardcore:
        document.getElementById("Highcore").innerHTML = f"Hardcore: {highcore}"

def update_lives():
    document.getElementById("Lives").innerHTML = f"Lives: {lives}"

# the timer check function - runs every 300 milliseconds to update the player position
def update_position():
    global playerX
    
    if xDir != 0:
        # Set the cell where the player was to empty
        cell = getCell(playerX, playerY)
        cell.className = "Empty"
        
        # Update the position for the player
        playerX += xDir
        # redraw player
        if playerX > 5:
            playerX = 5
        if playerX < 0:
            playerX = 0
        cell = getCell(playerX, playerY)
        cell.className = "player"

def make_easy(event):
    
    global easy
    global medium
    global hard
    global hardcore
    easy = True
    medium = False
    hard = False
    hardcore = False
    restart(event)
def make_medium(event):
    global easy
    global medium
    global hard
    global hardcore
    medium = True
    easy = False
    hard = False
    hardcore = False
    restart(event)
def make_hard(event):
    
    global easy
    global medium
    global hard
    global hardcore
    hard = True
    easy = False
    medium = False
    hardcore = False
    restart(event)
def make_hardcore(event):
    
    global easy
    global medium
    global hard
    global hardcore
    global lives
    lives = 1
    hardcore = True
    easy = False
    medium = False
    hard = False
    update_lives()
    restart(event)
    
def toggle_incspeed(event):
    
    global incspeed
    incspeed = not incspeed
    if incspeed:
        document.getElementById("speed").className = "increasing"
        document.getElementById("speed").innerHTML = "Increasing"
    else:
        document.getElementById("speed").className = "constant"
        document.getElementById("speed").innerHTML = "Constant"
    restart(event)

def runGame():
    global gameOver
    global score
    global xDir
    global playerX
    global playerY
    global lives
    global projectiles
    global projSpeed
    global projSpawn
    global toRemove
    global speedMultiplier
    global spawnMultiplier
    global incspeed
    global lastSpawn
    global lastSpeed
    lastSpawn = 0
    lastSpeed = 0
    gameOver = False
    score = 0
    update_score()
    xDir = 0
    playerX = 3
    playerY = 11
    lives = 10
    projectiles = []
    
    if easy:
        projSpeed = 800
        projSpawn = 1500
        if incspeed:
            speedMultiplier = 0.99
            spawnMultiplier = 0.97
        document.getElementById("Mode").className = "easy"
        document.getElementById("Mode").innerHTML = "Easy"
        speedLimit = 400
    elif medium:
        projSpeed = 400
        projSpawn = 1200
        if incspeed:
            speedMultiplier = 0.98
            spawnMultiplier = 0.96
        document.getElementById("Mode").className = "med"
        document.getElementById("Mode").innerHTML = "Medium"
        speedLimit = 200
    elif hard:
        projSpeed = 200
        projSpawn = 1000
        if incspeed:
            speedMultiplier = 0.96
            spawnMultiplier = 0.9
        document.getElementById("Mode").className = "hard"
        document.getElementById("Mode").innerHTML = "Hard"
        speedLimit = 100
    elif hardcore:
        lives = 1
        projSpeed = 90
        projSpawn = 800
        if incspeed:
            speedMultiplier = 0.99
            spawnMultiplier = 0.97
        document.getElementById("Mode").className = "hardcore"
        document.getElementById("Mode").innerHTML = "Hardcore"
        speedLimit = 90
    document.getElementById("projspeed").innerHTML = f"Speed: {projSpeed}"
    document.getElementById("projspawn").innerHTML = f"Spawn: {projSpawn}"
    
    if not incspeed: 
        speedMultiplier = 1
        spawnMultiplier = 1
    toRemove = []
    if not hardcore:
        document.getElementById("Lives").className = "default"
        global newId
        newId = "default"
    else:
        document.getElementById("Lives").className = "OneLife"
    global intervalHandle
    global intervalHandle2
    global intervalHandle3
    global intervalHandle4
    print("Running Game")
    init_player()
    document.addEventListener('keydown', checkKeyDown)
    document.addEventListener('keyup', checkKeyUp)      
    intervalHandle = window.setInterval(update_position, 100)
    intervalHandle2 = window.setInterval(check_over, 100)
    intervalHandle3 = window.setInterval(send_projectile, projSpawn)
    intervalHandle4 = window.setInterval(move_projectiles, projSpeed)
    
    
def check_over():
    if lives < 1:
        game_over(0)
        
def restart(event):
    game_over(1)
    for i in projectiles:
        cell = getCell(i[0], i[1])
        cell.className = 'Empty'
    cell = getCell(playerX, playerY)
    cell.className = 'Empty'
    update_lives()
    document.getElementById("blank").id = "Grid"
    runGame()
    
def game_over(n):
    if n == 0:
        if easy:
            global higheasy
            if score > higheasy:
                higheasy = score
                update_highscore()
        elif medium:
            global highmed
            if score > highmed:
                highmed = score
                update_highscore()
        elif hard:
            global highhard
            if score > highhard:
                highhard = score
                update_highscore()
        elif hardcore:
            global highcore
            if score > highcore:
                highcore = score
                update_highscore()
    window.clearInterval(intervalHandle)
    window.clearInterval(intervalHandle2)
    window.clearInterval(intervalHandle3)
    window.clearInterval(intervalHandle4)
    try:
        document.getElementById("Grid").id = "blank"
    except:
        pass
    
document.getElementById("restart").addEventListener('click', restart)
document.getElementById("Easy").addEventListener('click', make_easy)
document.getElementById("Medium").addEventListener('click', make_medium)
document.getElementById("Hard").addEventListener('click', make_hard)
document.getElementById("Hardcore").addEventListener('click', make_hardcore)
document.getElementById("incspeed").addEventListener('click', toggle_incspeed)
runGame()