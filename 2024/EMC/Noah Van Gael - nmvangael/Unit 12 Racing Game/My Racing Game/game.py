#############################
# Library Imports
#############################
from js import document, window
from pyodide.ffi import create_proxy
import random
from copy import deepcopy

#############################
# Global Variables
#############################

global shields, shield

shields = [3]
shield = [False, 0]

# to store current position (x,y)
position = [0, 0]

# to store movement directions (x,y)
direction = [0, 0]

# to store the handle code for the 

coins = [0]
wall_chance = 30
coin_chance = 25

#iterations = 0

#############################
# Sub-Programs
#############################

def build_track_random():
    track_size = [random.randint(5, 10), random.randint(5, 10)]
    track = []
    for i in range(track_size[0]):
        track.append(['wall' if random.randint(0, 100) < wall_chance else ['coin' if random.randint(0, 100) < coin_chance else ''][0] for _ in range(track_size[1])])
    track[track_size[0]-1][track_size[1]-1] = 'finish'
    build_track(track)

def generate_track():
    width, height = random.randint(5, 10), random.randint(5, 10)
    track = [['' for _ in range(width)] for _ in range(height)]

    wall_count = int(width * height * 0.3)
    for _ in range(wall_count):
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        if track[y][x] == '':
            track[y][x] = 'wall'

    track[height - 1][width - 1] = 'Player1'

    accessible_spots = []
    for y in range(height):
        for x in range(width):
            if track[y][x] == '' and self_check(track, x, y):
                accessible_spots.append((x, y))

    if accessible_spots:
        finish_x, finish_y = random.choice(accessible_spots)
        track[finish_y][finish_x] = 'finish'
    
    for i in range(round(width * height * 0.25)):
        random.choice(accessible_spots)

    track[0][0] = 'player1'

    build_track(track)

def self_check(track, x, y):
    if x > 0 and track[y][x-1] == 'wall':
        return False
    if x < len(track[0]) - 1 and track[y][x+1] == 'wall':
        return False
    if y > 0 and track[y-1][x] == 'wall':
        return False
    if y < len(track) - 1 and track[y+1][x] == 'wall':
        return False
    return True

def random_object():
    prob = random.randint(0, 100)

    if prob < 50:
        return 'wall'
    elif prob < 70:
        return 'coin'
    else:
        return ''

def check_range(row, col, track):
    if row > 0 and row < (len(track)-1) and col > 0 and col < (len(track[0])-1):
        return True
    return False

def neighbours(row, col, track):
    neighbours = 0
    if check_range(row, col+1, track):
        if track[row][col+1] == 'wall':
            neighbours += 1
    if check_range(row+1, col+1, track):
        if track[row+1][col+1] == 'wall':
            neighbours += 1
    if check_range(row-1, col+1, track):
        if track[row-1][col+1] == 'wall':
            neighbours += 1

    if check_range(row-1, col-1, track):
        if track[row-1][col-1] == 'wall':
            neighbours += 1
    if check_range(row, col-1, track):
        if track[row][col-1] == 'wall':
            neighbours += 1
    if check_range(row+1, col-1, track):
        if track[row+1][col-1] == 'wall':
            neighbours += 1

    if check_range(row-1, col, track):
        if track[row-1][col] == 'wall':
            neighbours += 1
    if check_range(row+1, col, track):
        if track[row+1][col] == 'wall':
            neighbours += 1
    
    return neighbours

def build_track(track):
    print(track)
    TableTextHTML = ''
    for row in range(len(track)):
        TableTextHTML += '<tr>'
        for col in range(len(track[row])):
            TableTextHTML += f'<td id="R{row}C{col}" class="{track[row][col]}"></td>'
        TableTextHTML += '</tr>'
    document.getElementById('racing_track').innerHTML = TableTextHTML

height = random.randint(10, 20)
width = random.randint(10, 20)
track = [[random_object() for _ in range(width)] for _ in range(height)]

def game_of_life(track):
#    iterations += 1
#    try:
#        window.clearInterval(interval)
#    except Exception as e:
#        print('First iteration')
    for i in range(1):
        new_track = deepcopy(track)
        for i in range(len(track)):
            for j in range(len(track[i])):
                if track[i][j] == 'wall':
                    if neighbours(i, j, track) < 2 or neighbours(i, j, track) > 3:
                        new_track[i][j] = ''
                else:
                    if neighbours(i, j, track) == 3:
                        new_track[i][j] = 'wall'
        track = new_track
        track[0][0] = 'player1'
        track[len(track)-1][len(track[0])-1] = 'finish'
    build_track(track)
#    if iterations < 3:
#        interval = window.setInterval(create_proxy(run_game), 500)
#    else:
#        return
#    return track

game_of_life(track)

#generate_track()
#def run_game():
#    track = game_of_life(track)

# the function called when a key is pressed - sets direction variable
def checkKey(event):
    global shield, shields
    event.preventDefault()
    if event.key == "ArrowRight":
        direction[0] = 1
        direction[1] = 0
    elif event.key == "ArrowLeft":
        # left arrow
        direction[0] = -1
        direction[1] = 0
    elif event.key == 'ArrowUp':
        direction[0] = 0
        direction[1] = -1
    elif event.key == 'ArrowDown':
        direction[0] = 0
        direction[1] = 1
    elif event.key == ' ':
        if shields[0] > 0:
            if shields == 3:
                shield = document.getElementById("shield1")
                shield.classNamde = "hide_shield"
            elif shields == 2:
                shield = document.getElementById("shield2")
                shield.className = "hide_shield"
            elif shields == 1:
                shield = document.getElementById("shield3")
                shield.className = "hide_shield"
            shields[0] -= 1
            shield = [True, 1]
            print(shield)

def getCell():
    return document.getElementById("R{}C{}".format(position[1], position[0]))

# the timer check function - runs every 300 milliseconds to update player1's position
def updatePosition():
    global shield, shields
    if direction[0] != 0 or direction[1] != 0:
        if shield[0]:
            shield[1] -= .5
            if shield[1] < 0:
                shield = [False, 0]
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
        elif cell.className == 'wall':
            if not shield[0]:
                handleCrash()
            else:
                shield = [False, 0]
                cell.className = "player1" if direction[0] == -1 else "player_flipped"
                print('saved')
        elif cell.className == 'finish':
            handleWin()
        elif cell.className == 'coin':
            coins[0] += 1
            if shield[0]:
                cell.className = "player_shield" if direction[0] == -1 else "player_shield_flipped"
            else:
                cell.className = "player1" if direction[0] == -1 else "player_flipped"
        else:
            if shield[0]:
                cell.className = "player_shield" if direction[0] == -1 else "player_shield_flipped"
            else:
                cell.className = "player1" if direction[0] == -1 else "player_flipped"

# if player1 has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Oops you crashed..."

def handleWin():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = f"You Win with {coins[0]} coins collected"

# called when the page is loaded to start the timer checks
def runGame():
    global intervalHandle
    print("Running Game")
    document.addEventListener('keydown', create_proxy(checkKey))
    intervalHandle = window.setInterval(create_proxy(updatePosition), 500)

#############################
# Main Program
#############################

runGame()