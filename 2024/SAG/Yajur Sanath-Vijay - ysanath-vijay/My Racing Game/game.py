#############################
# Library Imports
#############################
from js import document, window
from pyodide.ffi import create_proxy
import random
#############################
# Global Variables
#############################
# to store current positions (x,y) for players
player1_position = [0, 0]
player2_position = [9, 9]
# to store movement directions (x,y) for players
player1_direction = [0, 0]
player2_direction = [0, 0]
# to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 0
# to store the state of the game (running or not)
game_running = False
# to keep track of who is "it"
it = "player1"
#############################
# Sub-Programs
#############################
# the function called when a key is pressed - sets direction variable for player1
def checkKey(event):
    event.preventDefault()
    if event.key == "ArrowRight":
        player1_direction[0] = 1
        player1_direction[1] = 0
    elif event.key == "ArrowLeft":
        player1_direction[0] = -1
        player1_direction[1] = 0
    elif event.key == "ArrowDown":
        player1_direction[0] = 0
        player1_direction[1] = 1
    elif event.key == "ArrowUp":
        player1_direction[0] = 0
        player1_direction[1] = -1
# the function called when a key is pressed - sets direction variable for player2
def checkKey2(event):
    event.preventDefault()
    if event.key == "d":
        player2_direction[0] = 1
        player2_direction[1] = 0
    elif event.key == "a":
        player2_direction[0] = -1
        player2_direction[1] = 0
    elif event.key == "s":
        player2_direction[0] = 0
        player2_direction[1] = 1
    elif event.key == "w":
        player2_direction[0] = 0
        player2_direction[1] = -1
def getCell(player_position):
    return document.getElementById("R{}C{}".format(player_position[1], player_position[0]))
# the timer check function - runs every 300 milliseconds to update players' positions
def updatePositions():
    global it
    if player1_direction[0] != 0 or player1_direction[1] != 0:
        # Set the cell where player1 was to empty
        cell = getCell(player1_position)
        if cell:
            cell.className = ""
        # Update the position for player1
        player1_position[0] += player1_direction[0]
        player1_position[1] += player1_direction[1]
        # Re-draw player1 (or report a crash)
        cell = getCell(player1_position)
        
        if cell is None or cell.className == "wall":
            handleCrash("player1")
            
        else:
            cell.className = "player1"
    if player2_direction[0] != 0 or player2_direction[1] != 0:
        # Set the cell where player2 was to empty
        cell = getCell(player2_position)
        if cell:
            cell.className = ""
        
        # Update the position for player2
        player2_position[0] += player2_direction[0]
        player2_position[1] += player2_direction[1]
        # Re-draw player2 (or report a crash)
        cell = getCell(player2_position)
        if cell is None or cell.className == "wall":
            handleCrash("player2")
        else:
            cell.className = "player2"
    # Check if players have collided
    if player1_position == player2_position:
        if it == "player1":
            handleTag("player2")
        else:
            handleTag("player1")
def handleCrash(player):
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = f"{player.capitalize()} crashed..."
    game_running = False
def handleTag(tagged_player):
    window.clearInterval(intervalHandle)
    if tagged_player == "player1":
        document.getElementById("Message").innerText = "Player 2 tagged Player 1!"
        it = "player2"
    else:
        document.getElementById("Message").innerText = "Player 1 tagged Player 2!"
        it = "player1"
    game_running = False
def runGame():
    global intervalHandle, game_running
    print("Running Game")
    document.addEventListener('keydown', create_proxy(checkKey))
    document.addEventListener('keydown', create_proxy(checkKey2))
    intervalHandle = window.setInterval(create_proxy(updatePositions), 300)
    game_running = True
def resetGame():
    global player1_position, player2_position, player1_direction, player2_direction, game_running, it
    player1_position = [0, 0]
    player2_position = [9, 9]
    player1_direction = [0, 0]
    player2_direction = [0, 0]
    it = "player1"
    game_running = False
    document.getElementById("Message").innerText = ""
    cell = getCell(player1_position)
    if cell:
        cell.className = "player1"
    cell = getCell(player1_position)
    if cell:
        cell.className = "player2"
    cell = getCell(player2_position)
#############################
# Main Program
#############################
runGame()
