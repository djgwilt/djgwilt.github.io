#############################
# Library Imports
#############################
import os
import time
from js import document, window
from pyodide.ffi import create_proxy
import random
#############################
# Global Variables
audioBackground = document.getElementById("audioBackground")
#############################

# to store current position (x,y)
position = [1, 1]
# to store movement directions (x,y)
direction = [0, 0]
#to store flags left + coins collected
bag = [0, 0]
track = []
pytrack = []
tick = 0
# to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 0
enemyintervalHandle = 0
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
        direction[0] = -1
        direction[1] = 0
    elif event.key == "ArrowUp":
        direction[0] = 0
        direction[1] = -1
    elif event.key == "ArrowDown":
        direction[0] = 0
        direction[1] = 1

def getCell():
    return document.getElementById("R{}C{}".format(position[1], position[0]))

# the timer check function - runs every 300 milliseconds to update player1's position
def updatePosition():
    global tick
    global position
    tick += 1
    if tick == 10:
        hideTrack()
        document.addEventListener('keydown', create_proxy(checkKey))
    if direction[0] != 0 or direction[1] != 0:
        # Set the cell where player1 was to empty
        cell = getCell()
        if direction[0] > 0:
            player1Class = "player1-right"
        elif direction[0] < 0:
            player1Class = "player1-left"
        else:
            player1Class = cell.className
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
        elif cell.className == "flag":
            win()
        elif cell.className == "coin":
            cell.className = player1Class
            bag[1] += 1
        else:
            cell.className = player1Class

# if player1 has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Oops you crashed..."

# called when the page is loaded to start the timer checks
def runGame():
    global intervalHandle
    global tick
    print("Running Game")
    intervalHandle = window.setInterval(create_proxy(updatePosition), 300)

def win():
    global width
    global height
    global maze
    global track
    global pytrack
    track = []
    pytrack = []
    maze = [[True for y in range(height)] for x in range(width)]  
    width += 2
    height += 2
    print(width)
    print(height)
    print("hello")
    return buildNewLevel()
#############################
# Main Program
audioBackground.autoplay = False
audioBackground.load()
audioBackground.play()
#############################
# load the track
def loadTrackUnhidden():
    tableInnerHTML = ""
    track[1][1] = "player1-right"
    track[-2][-2] = "flag"
    for row in range(len(track)):
        tableInnerHTML += "<tr>"
        for col in range(len(track[0])):
            tableInnerHTML += "<td id='R{}C{}' class='{}'></td>".format(row, col, track[row][col])
        tableInnerHTML += "</tr>"
    document.getElementById("RacingTrack").innerHTML = tableInnerHTML

def recursiveMazeBuilder(x, y):
    global width
    global height
    maze[x][y] = False
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    random.shuffle(directions)
    for dx, dy in directions:
        if 0 < x + dx < width-1 and 0 < y + dy < height-1 and maze[x + dx * 2][y + dy * 2]:
            maze[x + dx][y + dy] = False
            time.sleep(SPEED)
            showMaze()
            recursiveMazeBuilder(x + dx * 2, y + dy * 2)

def showMaze():
    global width
    global height
    global pytrack
    os.system('cls' if os.name == 'nt' else 'clear')
    for y in range(height):
        row = []
        for x in range(width):
            row.append("#") if maze[x][y] else row.append(" ")
        pytrack.append(row)

def moveMazeToTable():
    global width
    global height
    for y in range(height):
        row = []
        for x in range(width):
            row.append("wall") if maze[x][y] else row.append("path")
        track.append(row)

def clearMaze():
    os.system('cls')

def waitTime():
    time.sleep(3)
    hideTrack()

def hideTrack():
    elements = document.querySelectorAll(".path")  # selector is a css selector (e.g. "div" or ".myClass" or "#myId")
    for e in elements:
        e.style.backgroundColor = "black"

def buildNewLevel():
    print("Yui")   
    showMaze()
    clearMaze()
    #start at 1,1 because we want the map to have a border
    recursiveMazeBuilder(1, 1)
    moveMazeToTable()
    loadTrackUnhidden()
    runGame()


# odd number for width and height
width = 5
height = 5
SPEED = 0.00000000001

# build an array of True for walls
maze = [[True for y in range(height)] for x in range(width)]      
buildNewLevel()
