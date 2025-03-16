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
 
audioFlag = document.getElementById("audioFlag")
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
        # left arrow
        direction[0] = -1
        direction[1] = 0
    elif event.key == "ArrowUp": 
        direction[0] = -1
        direction[1] = 0
    elif event.key == "ArrowDown": 
        direction[0] = 0
        direction[1] = -1
 
def getCell():
    return document.getElementById("R{}C{}".format(position[1], position[0])) 
  

# the timer check function - runs every 300 milliseconds to update the car position 

def updatePosition(): 

    if direction[0] != 0 or direction[1] != 0: 
        # Set the cell where the car was to empty 
        cell = getCell() 
        cell.className = "" 
        # Update the column position for the car 
        position[0] += direction[0] 
        position[1] += direction[1] 
        # Re-draw the car (or report a crash) 
        cell = getCell() 
        if cell: 
            cell.className = "car" 
        else: 
            handleCrash() 

def getCell(): 
    return document.getElementById("R{}C{}".format(position[1], position[0])) 

    
 
# if the car has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Oops you crashed..."
 
track = [["car", "empty", "empty", "empty", "flag", "wall", "wall", "wall", "wall", "wall"],["wall", "wall", "wall", "wall", "empty", "empty", "empty", "empty", "empty", "flag"],["flag", "empty", "empty", "empty", "empty", "wall", "wall", "wall", "wall", "wall"],["wall", "wall", "wall", "wall", "empty", "empty", "empty", "empty", "empty", "flag"],["flag", "empty", "empty", "empty", "empty", "wall", "wall", "wall", "wall", "wall"],["wall", "wall", "wall", "wall", "empty", "empty", "empty", "empty", "empty", "flag"],["flag", "empty", "empty", "empty", "empty", "wall", "wall", "wall", "wall", "wall"],["wall", "wall", "wall", "wall", "empty", "empty", "empty", "empty", "empty", "flag"],["flag", "empty", "empty", "empty", "empty", "wall", "wall", "wall", "wall", "wall"], ["wall", "wall", "wall", "wall", "empty", "empty", "empty", "empty", "empty", "flag"],]
 
def loadTrack():
    tableInnerHTML = ""
    for row in range(len(track)):
        tableInnerHTML += "<tr>"
        for col in range(len(track[0])):
            tableInnerHTML += "<td id='R{}C{}' class ='{}'></td>".format(row, col, track[row][col])
    tableInnerHTML += "</tr>"
    #print(tableInnerHTML)
    return tableInnerHTML
 
# called when the page is loaded to start the timer checks
def runGame():
    global intervalHandle
    print("Running Game")
    document.getElementById("RacingTrack").innerHTML = loadTrack()
    document.addEventListener('keydown', checkKey)
    intervalHandle = window.setInterval(updatePosition, 300)
 
#############################
# Main Program
#############################
 
audioFlag.autoplay = True
audioFlag.load()
move.autoplay = False
move.load()
dead.autoplay = False
dead.load()
runGame()