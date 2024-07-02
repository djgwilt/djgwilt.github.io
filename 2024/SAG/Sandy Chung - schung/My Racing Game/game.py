#############################
# Library Imports
#############################
from js import document, window
from pyodide.ffi import create_proxy 

#############################
# Global Variables
#############################

# to store current position (x,y)
position = [0, 0]

# to store movement directions (x,y)
direction = [0, 0]

# to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 0

life = 10

slowdown = False

skipframe = False 

 #import pygame, sys

import time
# define the countdown func. 
def countdown(t): 
    
    while t: 
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        t -= 1
    
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Oops you crashed..."
    life = life -1
    document.getElementById("Message").innerText = 'life - 1 ' + life + ' life remaining... '
    # called when the page is loaded to start the timer checks
def runGame():
    global intervalHandle
    print("Running Game")
    document.addEventListener('keydown', create_proxy(checkKey))
    intervalHandle = window.setInterval(create_proxy(updatePosition), 300)

def handleWin():
    window.clearInterval (intervalHandle)
    document.getElementById ("Message").innerText ="You win!"
def handleEnd():
    document.getElementById ("Message").innerText ="GAME OVER!"

def handleSlowdown():
    global slowdown
    slowdown = True
          
  
# input time in seconds 
#t = 90
  
# function call 
#countdown(int(t)) 
#############################
# Sub-Programs
#############################

# the function called when a key is pressed - sets direction variable

# def checkKey(event):
#     global life  # Ensure global life is declared
#     key = event.key
#     player_position = getPlayerPosition()

#     if key == "ArrowLeft":
#         movePlayer(player_position, -1)
#     elif key == "ArrowRight":
#         movePlayer(player_position, 1)
#     elif key == " ":
#         checkIfPlayerCrashed()
    
#     updateDisplay()

#def getPlayerPosition():
    # Retrieve player position logic
 #   pass

#def movePlayer(position, delta):
    # Move player logic
    #pass

def checkIfPlayerCrashed():
    # Crash checking logic
    global life
    life -= 1
    if life <= 0:
        handleCrash()

def handleCrash():
    # Crash handling logic
    global life
    life = 10  # Reset life for example
    print("Crash! Life reset to 10.")

#def updateDisplay():
    # Update display logic
 #   pass

def checkKey(event):
    event.preventDefault()
    if event.key == "ArrowRight":
        direction[0] = 1
        direction[1]=0
    elif event.key == "ArrowLeft":
        # left arrow
        direction[0] = -1
        direction[1]=0
    elif event.key == "ArrowUp":
        # left arrow
        direction[0] = 0
        direction[1]=-1
    elif event.key == "ArrowDown":
        # left arrow
        direction[0] =0
        direction[1]=1


def getCell():
    return document.getElementById("R{}C{}".format(position[1], position[0]))

# the timer check function - runs every 300 milliseconds to update player1's position
def updatePosition():
    global skipframe
    if slowdown== True and skipframe == False:
        if direction[0] != 0 or direction[1] != 0 :
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
            elif cell.className == "wall":
                handleCrash()
            elif cell.className == "igloo":
                handleWin()
            elif cell.className == "fakewall":
                handleSlowdown()
            else:
                cell.className = "player1"
            skipframe= not skipframe 

# if player1 has gone off the table, this tidies up including crash message

    # Main Program
    #############################

runGame()