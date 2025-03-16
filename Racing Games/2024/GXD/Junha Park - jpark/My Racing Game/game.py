#############################
# Library Imports
#############################
from js import document, window
import random

#############################
# Global Variables
#############################

# to store current position (x,y)
position = [1, 1]

# to store movement directions (x,y) and arrow stuffs
direction = [0, 0]
arrow = "R"

arrownames = {"R": "playerRight", 
              "L": "playerLeft",
              "U": "playerUp",
              "D": "playerDown", }

keys = set()

# to store the handle code for the timer interval to cancel it when we crash

intervalHandle = 0

# To store the movement fluidity

Interval = 120

# Variables to store positions and such

width = 5
height = 5

# Variable to store the message when you noclip

Messages = ["First time Noclipping? It may be a shock at first... \nBut you get used to it after a while. \nKeep exploring, see what you find...", 
            "Great job! by this point you can return to base with some samples but... \nWhat's the fun in that right? \nKeep going, you might just find something... \nSpecial", 
            "Oh that's a Lifeform Fellow. And it uhhhh, \nWe don't have a lot of data on it right now. All we know is that... \nIt will kill you...", 
            "You seem to be out of reach of the Lifeform Fellow now. \nYour next Noclip should take you out of the backrooms into our base."]
NoClipTimes = -1

#############################
# Sub-Programs
#############################

def resetTrack(width, height):
    myTrackComplete = [ [9, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
                        [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0],
                        [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0],
                        [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                        [0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0],
                        [0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0],
                        [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0],
                        [1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
                        [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
                        [0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
                        [0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0],
                        [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                        [0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
                        [0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0],
                        [0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0],
                        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
                        [0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
                        [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
                        [0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    myTrack = [myTrackComplete[r][:width] for r in range(height)]
    #Creates one layer padding
    for index in range(len(myTrack)):
        myTrack[index].insert(0,1)
        myTrack[index].append(1)
    myTrack.insert(0, [1 for c in range(width+2)])
    myTrack.append([1 for c in range(width+2)])
    return myTrack

def CreateNoClipPoint():
    global width
    global height
    row = random.randrange(height+1)
    col = random.randrange(width+1)
    while document.getElementById(f"R{row}C{col}").className != "empty": 
        row = random.randrange(height+1)
        col = random.randrange(width+1)
    document.getElementById(f"R{row}C{col}").className = "NoClipPoint"

def convertTrack(myTrack):
    # converts the numbers in the track to the names of the objects they represent
    convert = {0: "empty", 1: "wall", 9: "playerRight"}
    for rowpos, row in enumerate(myTrack): #rowpos in the row position, row is the actual values of the row
        for colpos, val in enumerate(row):
            number = myTrack[rowpos][colpos]
            myTrack[rowpos][colpos] = convert[number]
    return myTrack

def drawTrack():
    global myTrack
    myTrack = convertTrack(myTrack) # so the html code can be edited
    trackHTML = ""
    for rowpos, row in enumerate(myTrack):
        trackHTML += "<tr>"
        for colpos, val in enumerate(row):
            trackHTML += f"<td id='R{rowpos}C{colpos}' class='{myTrack[rowpos][colpos]}'></td>"
        trackHTML += "</tr>"
    document.getElementById("RacingTrack").innerHTML = trackHTML

def resetVariables():
    global position
    global direction
    global myTrack
    global width
    global height
    # To store current position (x,y)
    position = [1, 1]

    # To store movement directions (x,y)
    direction = [0, 0]

    # Create the "track"
    myTrack = resetTrack(width, height)
    drawTrack()

    # Create a Noclip Point
    CreateNoClipPoint()

def ExpandTrack():
    global width
    global height
    height += 5
    width += 5

# the function called when a key is pressed - sets direction variable
def CheckKeyDown(event):
    event.preventDefault()
    keys.add(event.key)


def CheckKeyUp(event):
    event.preventDefault()
    keys.remove(event.key)

def getCell():
    return document.getElementById("R{}C{}".format(position[1], position[0]))

# the timer check function - runs every something milliseconds to update player1's position
def updatePosition():
    global direction
    global NoClipTimes
    global keys
    global Interval

    # Set the direction based off of the keys pressed (variables in the key)

    if "ArrowRight" in keys:
        direction[0] += 1
        arrow = "R"
    if "ArrowLeft" in keys:
        direction[0] -= 1
        arrow = "L"
    if "ArrowDown" in keys:
        direction[1] += 1
        arrow = "D"
    if "ArrowUp" in keys:
        direction[1] -= 1
        arrow = "U"

    if len(keys) > 0:
        Interval = 300
    else:
        Interval = 50

    if direction[0] != 0 or direction[1] != 0:
        # Set the cell where player1 was to empty if it's not a wall
        # Get the next cell based on the direction
        position[1] += direction[1]
        position[0] += direction[0]
        cell = getCell()

        if cell.className == "wall":
            position[1] -= direction[1]
            position[0] -= direction[0]
        else:
            # Update the position for player1
            position[1] -= direction[1]
            position[0] -= direction[0]
            cell = getCell()
            cell.className = "empty"
            position[1] += direction[1]
            position[0] += direction[0]

        # Stop Moving
        direction = [0, 0]

        # Re-draw player1 (or report an event)
        cell = getCell()

        # If the player Noclips
        if cell.className == "NoClipPoint":
            cell.className = arrownames[arrow]
            direction = [0, 0]
            NoClipTimes += 1
            if NoClipTimes == 4:
                # Add a rickroll here
                
                print("")
            else:
                print(Messages[NoClipTimes], "\n")
                ExpandTrack()
                resetVariables()

        else:
            cell.className = arrownames[arrow]

# if player1 has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Massive skill issue dude..."

# called when the page is loaded to start the timer checks
def runGame():
    global intervalHandle
    global Interval
    print("Welcome to your first official mission here at ASYNC. \nThis map will show you where you are, and the arrow represents you. \nYou may not be able to differentiate between wall and ground right now... \nBut wander around the level until you find an area to Noclip into... Best wishes. \n - J Park, Head of Backrooms Exploration\n")
    document.addEventListener('keydown', CheckKeyDown)
    document.addEventListener('keyup', CheckKeyUp)
    intervalHandle = window.setInterval(updatePosition, Interval)
    if len(keys) > 0:
        Interval = 300
    else:
        Interval = 50

#############################
# Main Program
#############################

resetVariables()
runGame()