class Unbuffered(object):
    def __init__(self, stream):
        self.stream = stream
    def write(self, data):
        self.stream.write(data)
        self.stream.flush()
    def writelines(self, datas):
        self.stream.writelines(datas)
        self.stream.flush()
    def __getattr__(self, attr):
        return getattr(self.stream, attr)

import sys
sys.stdout = Unbuffered(sys.stdout)

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
maze = []
shownMaze = []
vision = 1
canSee = []
# to store movement direction
xDir = 0
yDir = 0
# to store current column position
playerX = 0
playerY = 0
# to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 0
intervalHandle2 = 0

#############################
# Sub-Programs
#############################
# the function called when a key is pressed - sets direction variable
def countdown(t):
    t = int(t)
    while t > 0:
        time.sleep(1)
        print(t)
        t -= 1
    #game_over() enable when figured out how to use time
    
def init_player():
    global playerX
    global playerY
    cell1 = maze[0][1]
    cell2 = maze[0][2]
    if cell1 == 'c':
        playerX = 1
        playerY = 0
    elif cell2 == 'c':
        playerX = 2
        playerY = 0
        
# DIFFICULTY VARIABLES:
v1 = True
v2 = True
# if both true: easy
# if both false: hard
# if one true one false: medium
def toggle_difficulty():
    if v1 and v2:
        v1 = not v1
    elif not v1:
        v2 = not v2
    elif not v1 and not v2:
        v1 = True
        v2 = True
def check_difficulty():
    pass

        
def checkKeyDown(event):
    global xDir
    global yDir
    if event.keyCode == 68:
        # right 
        xDir = 1
    elif event.keyCode == 65:
        # left 
        xDir = -1
    elif event.keyCode == 87:
        # up
        yDir = -1
    elif event.keyCode == 83:
        # down
        yDir = +1

def checkKeyUp(event):
    global xDir
    global yDir
    if event.keyCode == 68 or event.keyCode == 65:
        xDir = 0
    elif event.keyCode == 87 or event.keyCode == 83:
        yDir = 0
    
def getCell(x, y):
    return document.getElementById(f"R{y}C{x}")

#[][][]
#[]XY[]
#[][][]
def update_vision():
    
    global canSee
    global shownMaze
    shownMaze = []
    seeUp = -1
    seeDown = 1
    seeLeft = -1
    seeRight = 1
    while maze[playerY+seeUp][playerX] == 'c':
        canSee.append([playerX, playerY+seeUp])
        seeUp -= 1

    canSee.append([playerX, playerY+seeUp])
    while maze[playerY+seeDown][playerX] == 'c':
        canSee.append([playerX, playerY+seeDown])
        seeDown += 1
        if playerY + seeDown >= 20:
            break
    canSee.append([playerX, playerY+seeDown])
    while maze[playerY][playerX+seeLeft] == 'c':
        canSee.append([playerX+seeLeft, playerY])
        seeLeft -= 1
    canSee.append([playerX+seeLeft, playerY])
    while maze[playerY][playerX+seeRight] == 'c':
        canSee.append([playerX+seeRight, playerY])
        seeRight += 1
    canSee.append([playerX+seeRight, playerY])

    x = [[playerX-vision, playerY], [playerX+vision, playerY], [playerX, playerY-vision], [playerX, playerY+vision], [playerX-vision, playerY-vision], [playerX-vision, playerY+vision], [playerX+vision, playerY-vision], [playerX+vision, playerY+vision]]
    for i in x:
        canSee.append(i)
    for row in range(len(maze)):
        x = []
        for col in range(len(maze[row])):
            hide = True
            for coords in canSee:
                if coords == [col, row]:
                    x.append(maze[row][col])
                    hide = False
                    break
            if hide:
                x.append('h')
        shownMaze.append(x)
    update_maze()

    
# the timer check function - runs every 300 milliseconds to update the player position
def update_position():
    global playerX
    global playerY
    if xDir != 0 or yDir != 0:
        # Set the cell where the player was to empty
        cell = getCell(playerX, playerY)
        cell.className = "Empty"
        
        # Update the position for the player
        playerX += xDir
        playerY += yDir
        # Re-draw the player (or report a crash)
        cell = getCell(playerX, playerY)
        
        if cell.className == 'Wall':
            playerX -= xDir
            playerY -= yDir
        cell = getCell(playerX, playerY)
        cell.className = "player"
        
        update_vision()
# called when the page is loaded to start the timer checks
def runGame():
    make_maze()
    countdown(3)
    global intervalHandle
    global intervalHandle2
    print("Running Game")
    document.addEventListener('keydown', checkKeyDown)
    document.addEventListener('keyup', checkKeyUp)      
    intervalHandle = window.setInterval(update_position, 300)
    intervalHandle2 = window.setInterval(check_over, 200)

def restart():
    pass
    
def check_over():
    global gameOver
    if gameOver:
        game_over()
def game_over():
    window.clearInterval(intervalHandle)
    window.clearInterval(intervalHandle2)
    document.getElementById(f"R{playerY}C{playerX}").className = "Empty"
    document.getElementById("Grid").id = "blank"
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            document.getElementById(f"R{row}C{col}").className = "Empty"
    
    for i in range(21):
        document.getElementById(f"R{2}C{i}").className = "Fill"
    for i in range(1, 4):
        document.getElementById(f"R{4}C{i}").className = "Fill"
    for i in range(5,8):
        document.getElementById(f"R{4}C{i}").className = "Fill"
    document.getElementById(f"R{4}C{9}").className = "Fill"
    document.getElementById(f"R{4}C{13}").className = "Fill"
    for i in range(15, 19):
        document.getElementById(f"R{4}C{i}").className = "Fill"
    document.getElementById(f"R{5}C{0}").className = "Fill"
    document.getElementById(f"R{5}C{5}").className = "Fill"
    document.getElementById(f"R{5}C{7}").className = "Fill"
    document.getElementById(f"R{5}C{9}").className = "Fill"
    document.getElementById(f"R{5}C{10}").className = "Fill"
    document.getElementById(f"R{5}C{12}").className = "Fill"
    document.getElementById(f"R{5}C{13}").className = "Fill"
    document.getElementById(f"R{5}C{15}").className = "Fill"
    document.getElementById(f"R{6}C{0}").className = "Fill"
    document.getElementById(f"R{6}C{2}").className = "Fill"
    document.getElementById(f"R{6}C{3}").className = "Fill"
    document.getElementById(f"R{6}C{5}").className = "Fill"
    document.getElementById(f"R{6}C{6}").className = "Fill"
    document.getElementById(f"R{6}C{7}").className = "Fill"
    document.getElementById(f"R{6}C{9}").className = "Fill"
    document.getElementById(f"R{6}C{11}").className = "Fill"
    document.getElementById(f"R{6}C{13}").className = "Fill"
    document.getElementById(f"R{6}C{15}").className = "Fill"
    document.getElementById(f"R{6}C{16}").className = "Fill"
    document.getElementById(f"R{6}C{17}").className = "Fill"
    document.getElementById(f"R{7}C{0}").className = "Fill"
    document.getElementById(f"R{7}C{3}").className = "Fill"
    document.getElementById(f"R{7}C{5}").className = "Fill"
    document.getElementById(f"R{7}C{7}").className = "Fill"
    document.getElementById(f"R{7}C{9}").className = "Fill"
    document.getElementById(f"R{7}C{13}").className = "Fill"
    document.getElementById(f"R{7}C{15}").className = "Fill"
    document.getElementById(f"R{8}C{1}").className = "Fill"
    document.getElementById(f"R{8}C{2}").className = "Fill"
    document.getElementById(f"R{8}C{3}").className = "Fill"
    document.getElementById(f"R{8}C{5}").className = "Fill"
    document.getElementById(f"R{8}C{7}").className = "Fill"
    document.getElementById(f"R{8}C{9}").className = "Fill"
    document.getElementById(f"R{8}C{13}").className = "Fill"
    document.getElementById(f"R{8}C{15}").className = "Fill"
    document.getElementById(f"R{8}C{16}").className = "Fill"
    document.getElementById(f"R{8}C{17}").className = "Fill"
    document.getElementById(f"R{8}C{18}").className = "Fill"
    #start
    document.getElementById(f"R{10}C{3}").className = "Fill"
    document.getElementById(f"R{10}C{4}").className = "Fill"
    document.getElementById(f"R{10}C{7}").className = "Fill"
    document.getElementById(f"R{10}C{9}").className = "Fill"
    document.getElementById(f"R{10}C{11}").className = "Fill"
    document.getElementById(f"R{10}C{12}").className = "Fill"
    document.getElementById(f"R{10}C{13}").className = "Fill"
    document.getElementById(f"R{10}C{14}").className = "Fill"
    document.getElementById(f"R{10}C{16}").className = "Fill"
    document.getElementById(f"R{10}C{17}").className = "Fill"
    document.getElementById(f"R{10}C{18}").className = "Fill"
    document.getElementById(f"R{11}C{2}").className = "Fill"
    document.getElementById(f"R{11}C{5}").className = "Fill"
    document.getElementById(f"R{11}C{7}").className = "Fill"
    document.getElementById(f"R{11}C{9}").className = "Fill"
    document.getElementById(f"R{11}C{11}").className = "Fill"
    document.getElementById(f"R{11}C{16}").className = "Fill"
    document.getElementById(f"R{11}C{19}").className = "Fill"
    document.getElementById(f"R{12}C{2}").className = "Fill"
    document.getElementById(f"R{12}C{5}").className = "Fill"
    document.getElementById(f"R{12}C{7}").className = "Fill"
    document.getElementById(f"R{12}C{9}").className = "Fill"
    document.getElementById(f"R{12}C{11}").className = "Fill"
    document.getElementById(f"R{12}C{12}").className = "Fill"
    document.getElementById(f"R{12}C{13}").className = "Fill"
    document.getElementById(f"R{12}C{16}").className = "Fill"
    document.getElementById(f"R{12}C{17}").className = "Fill"
    document.getElementById(f"R{12}C{18}").className = "Fill"
    document.getElementById(f"R{13}C{2}").className = "Fill"
    document.getElementById(f"R{13}C{5}").className = "Fill"
    document.getElementById(f"R{13}C{7}").className = "Fill"
    document.getElementById(f"R{13}C{9}").className = "Fill"
    document.getElementById(f"R{13}C{11}").className = "Fill"
    document.getElementById(f"R{13}C{16}").className = "Fill"
    document.getElementById(f"R{13}C{18}").className = "Fill"
    document.getElementById(f"R{14}C{3}").className = "Fill"
    document.getElementById(f"R{14}C{4}").className = "Fill"
    document.getElementById(f"R{14}C{8}").className = "Fill"
    document.getElementById(f"R{14}C{11}").className = "Fill"
    document.getElementById(f"R{14}C{12}").className = "Fill"
    document.getElementById(f"R{14}C{13}").className = "Fill"
    document.getElementById(f"R{14}C{14}").className = "Fill"
    document.getElementById(f"R{14}C{16}").className = "Fill"
    document.getElementById(f"R{14}C{19}").className = "Fill"
    for i in range(21):
        document.getElementById(f"R{16}C{i}").className = "Fill"
    print("end")
    

# Maze generator -- Randomized Prim Algorithm
def runMaze():
    ## Imports
    import random
    import time
    ## Functions

    ## Main code
    # Init variables
    wall = 'w'
    cell = 'c'
    unvisited = 'u'
    height = 20
    width = 20
    global maze
    maze = []

    # Find number of surrounding cells
    def surroundingCells(rand_wall):
        s_cells = 0
        if (maze[rand_wall[0]-1][rand_wall[1]] == 'c'):
            s_cells += 1
        if (maze[rand_wall[0]+1][rand_wall[1]] == 'c'):
            s_cells += 1
        if (maze[rand_wall[0]][rand_wall[1]-1] == 'c'):
            s_cells +=1
        if (maze[rand_wall[0]][rand_wall[1]+1] == 'c'):
            s_cells += 1

        return s_cells
    # Denote all cells as unvisited
    for i in range(0, height):
        line = []
        for j in range(0, width):
            line.append(unvisited)
        maze.append(line)

    # Randomize starting point and set it a cell
    starting_height = int(random.random()*height)
    starting_width = int(random.random()*width)
    if (starting_height == 0):
        starting_height += 1
    if (starting_height == height-1):
        starting_height -= 1
    if (starting_width == 0):
        starting_width += 1
    if (starting_width == width-1):
        starting_width -= 1

    # Mark it as cell and add surrounding walls to the list
    maze[starting_height][starting_width] = cell
    walls = []
    walls.append([starting_height - 1, starting_width])
    walls.append([starting_height, starting_width - 1])
    walls.append([starting_height, starting_width + 1])
    walls.append([starting_height + 1, starting_width])

    # Denote walls in maze
    maze[starting_height-1][starting_width] = 'w'
    maze[starting_height][starting_width - 1] = 'w'
    maze[starting_height][starting_width + 1] = 'w'
    maze[starting_height + 1][starting_width] = 'w'

    while (walls):
        # Pick a random wall
        rand_wall = walls[int(random.random()*len(walls))-1]

        # Check if it is a left wall
        if (rand_wall[1] != 0):
            if (maze[rand_wall[0]][rand_wall[1]-1] == 'u' and maze[rand_wall[0]][rand_wall[1]+1] == 'c'):
                # Find the number of surrounding cells
                s_cells = surroundingCells(rand_wall)

                if (s_cells < 2):
                    # Denote the new path
                    maze[rand_wall[0]][rand_wall[1]] = 'c'

                    # Mark the new walls
                    # Upper cell
                    if (rand_wall[0] != 0):
                        if (maze[rand_wall[0]-1][rand_wall[1]] != 'c'):
                            maze[rand_wall[0]-1][rand_wall[1]] = 'w'
                        if ([rand_wall[0]-1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0]-1, rand_wall[1]])


                    # Bottom cell
                    if (rand_wall[0] != height-1):
                        if (maze[rand_wall[0]+1][rand_wall[1]] != 'c'):
                            maze[rand_wall[0]+1][rand_wall[1]] = 'w'
                        if ([rand_wall[0]+1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0]+1, rand_wall[1]])

                    # Leftmost cell
                    if (rand_wall[1] != 0):	
                        if (maze[rand_wall[0]][rand_wall[1]-1] != 'c'):
                            maze[rand_wall[0]][rand_wall[1]-1] = 'w'
                        if ([rand_wall[0], rand_wall[1]-1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1]-1])


                # Delete wall
                for wall in walls:
                    if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                        walls.remove(wall)

                continue

        # Check if it is an upper wall
        if (rand_wall[0] != 0):
            if (maze[rand_wall[0]-1][rand_wall[1]] == 'u' and maze[rand_wall[0]+1][rand_wall[1]] == 'c'):

                s_cells = surroundingCells(rand_wall)
                if (s_cells < 2):
                    # Denote the new path
                    maze[rand_wall[0]][rand_wall[1]] = 'c'

                    # Mark the new walls
                    # Upper cell
                    if (rand_wall[0] != 0):
                        if (maze[rand_wall[0]-1][rand_wall[1]] != 'c'):
                            maze[rand_wall[0]-1][rand_wall[1]] = 'w'
                        if ([rand_wall[0]-1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0]-1, rand_wall[1]])

                    # Leftmost cell
                    if (rand_wall[1] != 0):
                        if (maze[rand_wall[0]][rand_wall[1]-1] != 'c'):
                            maze[rand_wall[0]][rand_wall[1]-1] = 'w'
                        if ([rand_wall[0], rand_wall[1]-1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1]-1])

                    # Rightmost cell
                    if (rand_wall[1] != width-1):
                        if (maze[rand_wall[0]][rand_wall[1]+1] != 'c'):
                            maze[rand_wall[0]][rand_wall[1]+1] = 'w'
                        if ([rand_wall[0], rand_wall[1]+1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1]+1])

                # Delete wall
                for wall in walls:
                    if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                        walls.remove(wall)

                continue

        # Check the bottom wall
        if (rand_wall[0] != height-1):
            if (maze[rand_wall[0]+1][rand_wall[1]] == 'u' and maze[rand_wall[0]-1][rand_wall[1]] == 'c'):

                s_cells = surroundingCells(rand_wall)
                if (s_cells < 2):
                    # Denote the new path
                    maze[rand_wall[0]][rand_wall[1]] = 'c'

                    # Mark the new walls
                    if (rand_wall[0] != height-1):
                        if (maze[rand_wall[0]+1][rand_wall[1]] != 'c'):
                            maze[rand_wall[0]+1][rand_wall[1]] = 'w'
                        if ([rand_wall[0]+1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0]+1, rand_wall[1]])
                    if (rand_wall[1] != 0):
                        if (maze[rand_wall[0]][rand_wall[1]-1] != 'c'):
                            maze[rand_wall[0]][rand_wall[1]-1] = 'w'
                        if ([rand_wall[0], rand_wall[1]-1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1]-1])
                    if (rand_wall[1] != width-1):
                        if (maze[rand_wall[0]][rand_wall[1]+1] != 'c'):
                            maze[rand_wall[0]][rand_wall[1]+1] = 'w'
                        if ([rand_wall[0], rand_wall[1]+1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1]+1])

                # Delete wall
                for wall in walls:
                    if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                        walls.remove(wall)


                continue

        # Check the right wall
        if (rand_wall[1] != width-1):
            if (maze[rand_wall[0]][rand_wall[1]+1] == 'u' and maze[rand_wall[0]][rand_wall[1]-1] == 'c'):

                s_cells = surroundingCells(rand_wall)
                if (s_cells < 2):
                    # Denote the new path
                    maze[rand_wall[0]][rand_wall[1]] = 'c'

                    # Mark the new walls
                    if (rand_wall[1] != width-1):
                        if (maze[rand_wall[0]][rand_wall[1]+1] != 'c'):
                            maze[rand_wall[0]][rand_wall[1]+1] = 'w'
                        if ([rand_wall[0], rand_wall[1]+1] not in walls):
                            walls.append([rand_wall[0], rand_wall[1]+1])
                    if (rand_wall[0] != height-1):
                        if (maze[rand_wall[0]+1][rand_wall[1]] != 'c'):
                            maze[rand_wall[0]+1][rand_wall[1]] = 'w'
                        if ([rand_wall[0]+1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0]+1, rand_wall[1]])
                    if (rand_wall[0] != 0):	
                        if (maze[rand_wall[0]-1][rand_wall[1]] != 'c'):
                            maze[rand_wall[0]-1][rand_wall[1]] = 'w'
                        if ([rand_wall[0]-1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0]-1, rand_wall[1]])

                # Delete wall
                for wall in walls:
                    if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                        walls.remove(wall)

                continue

        # Delete the wall from the list anyway
        for wall in walls:
            if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                walls.remove(wall)



    # Mark the remaining unvisited cells as walls
    for i in range(0, height):
        for j in range(0, width):
            if (maze[i][j] == 'u'):
                maze[i][j] = 'w'

    # Set entrance and exit
    for i in range(0, width):
        if (maze[1][i] == 'c'):
            maze[0][i] = 'c'
            break

    for i in range(width-1, 0, -1):
        if (maze[height-2][i] == 'c'):
            maze[height-1][i] = 'c'
            break
    return maze

def make_maze():
    maze = runMaze()
    init_player()
    update_vision()
    shownMaze[playerY][playerX] = 'p'
    for row in range(len(shownMaze)):
        for col in range(len(shownMaze[row])):
            cell = getCell(col, row)
            if shownMaze[row][col] == 'w':
                cell.className = 'Wall'
            elif shownMaze[row][col] == 'c':
                cell.className = 'Empty'
            elif shownMaze[row][col] == 'h':
                cell.className = 'hide'
        cell = getCell(playerX, playerY)
        cell.className = 'player'

def update_maze():
    for row in range(len(shownMaze)):
        for col in range(len(shownMaze[row])):
            cell = getCell(col, row)
            if shownMaze[row][col] == 'w':
                cell.className = 'Wall'
            elif shownMaze[row][col] == 'c':
                cell.className = 'Empty'
            elif shownMaze[row][col] == 'h':
                cell.className = 'hide'
        cell = getCell(playerX, playerY)
        cell.className = 'player'
    
runGame()
