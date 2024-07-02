#############################
# Library Imports
#############################
from js import document, window
from pyodide.ffi import create_proxy
import random
import os
import time


#############################
# Global Variables
#############################

audioWin = document.getElementById("audioWin")
audioCrash = document.getElementById("audioCrash")
audioBackground = document.getElementById("audioBackground")
# to store current position (x,y)
position = [0, 0]

# odd number for width and height
WIDTH = 11
HEIGHT = 11
SPEED = 0.2

# build an array of True for walls
maze = [[True for y in range(HEIGHT)] for x in range(WIDTH)]

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
    if event.key == "d":
        direction[0] = 1
        direction[1] = 0
    elif event.key == "a":
        # left arrow
        direction[0] = -1
        direction[1] = 0
    elif event.key == "s":
        direction[0] = 0
        direction[1] = 1
    elif event.key == "w":
        direction[0] = 0
        direction[1] = -1
    
def recursiveMazeBuilder(x, y):
    maze[x][y] = False
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    random.shuffle(directions)
    for dx, dy in directions:
        if 0 < x + dx < WIDTH-1 and 0 < y + dy < HEIGHT-1 and maze[x + dx * 2][y + dy * 2]:
            maze[x + dx][y + dy] = False
            time.sleep(SPEED)
            showMaze()
            recursiveMazeBuilder(x + dx * 2, y + dy * 2)

def printMazeAsHTMLTable():
    print('<table id = "RacingTrack">')
    for y in range(HEIGHT):
        print('<tr>')
        for x in range(WIDTH):
            print('<td id="R{}C{}" class="wall"></td>'.format(y, x) if maze[x][y] else '<td id="R{}C{}"></td>'.format(y, x))
        print('</tr>')
    print('</table>')
       

def getCell():
    audioBackground.play()
    return document.getElementById("R{}C{}".format(position[1], position[0]))
    
# the timer check function - runs every 300 milliseconds to update player1's position
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
            audioBackground.pause()
            audioCrash.play()
        elif cell.className ==  "wall":
            handleCrash()
            audioBackground.pause()
            audioCrash.play()
        elif cell.className == "flag":
            handleWin()
            audioBackground.pause()
            audioWin.play()
        else:
            cell.className = "player1"

def handleWin():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "You win"
# if player1 has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Oops you crashed..."

# called when the page is loaded to start the timer checks
def runGame():
    global intervalHandle
    print("Running Game")
    document.addEventListener('keydown', create_proxy(checkKey))
    intervalHandle = window.setInterval(create_proxy(updatePosition), 300)

#############################
# Main Program
#############################

audioBackground.autoplay = False
audioBackground.load()
audioWin.autoplay = False
audioWin.load()
audioCrash.autoplay = False
audioCrash.load()
#start at 1,1 because we want the map to have a border
recursiveMazeBuilder(1, 1)
printMazeAsHTMLTable()

runGame()




