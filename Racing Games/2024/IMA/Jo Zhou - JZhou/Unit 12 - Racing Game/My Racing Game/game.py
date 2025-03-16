#############################
# Library Imports
#############################
from js import document, window

#############################
# Global Variables
#############################

# to store current position (x,y)
position = [0, 0]

# to store movement directions (x,y)
direction = [0, 0]

# to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 0

#############################
# Sub-Programs
#############################

#audio variables
audioWall = document.getElementById("audioWall")
audioFlag = document.getElementById("audioFlag")

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
    if event.key == "ArrowUp":
        direction[1] = -1
        direction[0] = 0
    elif event.key == "ArrowDown":
        direction[1] = 1
        direction[0] = 0

def getCell():
    return document.getElementById("R{}C{}".format(position[1], position[0]))

# the timer check function - runs every 300 milliseconds to update the car position
def updatePosition():
    if direction[0] != 0 or direction[1] != 0:
        # Set the cell where the car was to empty
        cell = getCell()
        if direction[0] > 0:
            player1Class = "car"
        elif direction[0] < 0:
            player1Class = "car-left"
        else:
            player1Class = cell.className
        cell.className = ""

        
        # Update the column position for the car
        position[0] += direction[0]
        position[1] += direction[1]

        # Re-draw the car (or report a crash)
        cell = getCell()
        if cell == None:
            audioWall.play()
            handleCrash()
        elif cell.className == "wall":
            audioWall.play()
            handleCrash()
        elif cell.className == "flag":
            audioFlag.play()
            handleWin()
        else:
           cell.className = player1Class
# if the car has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "HAHA YOU CRASHED WOMP WOMP"

# called when the page is loaded to start the timer checks
def runGame():
    global intervalHandle
    print("Running Game")
    document.addEventListener('keydown', checkKey)
    intervalHandle = window.setInterval(updatePosition, 300)

def handleWin():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "You Win!!!"



import random
import os
import time

# odd number for width and height
WIDTH = 11
HEIGHT = 11
SPEED = 0.2

# build an array of True for walls
maze = [[True for y in range(HEIGHT)] for x in range(WIDTH)]

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

def showMaze():
    os.system('cls' if os.name == 'nt' else 'clear')
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print('#' if maze[x][y] else ' ', end='')
        print()

def printMazeAsHTMLTable():
    print('<table id = "RacingTrack">')
    for y in range(HEIGHT):
        print('<tr>')
        for x in range(WIDTH):
            print('<td id="R{}C{}" class="wall"></td>'.format(y, x) if maze[x][y] else '<td id="R{}C{}"></td>'.format(y, x))
        print('</tr>')
    print('</table>')
       
showMaze()
#start at 1,1 because we want the map to have a border
recursiveMazeBuilder(1, 1)
input("Press Enter to print the maze as an HTML table...")
printMazeAsHTMLTable()


#############################
# Main Program
#############################

audioWall.autoplay = False
audioWall.load()
audioFlag.autoplay = False
audioFlag.load()


runGame()
