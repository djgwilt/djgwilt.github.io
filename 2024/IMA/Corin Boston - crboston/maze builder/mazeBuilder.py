import random
import os
import time

# odd number for width and height
WIDTH = 31
HEIGHT = 11
SPEED = 0.01

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