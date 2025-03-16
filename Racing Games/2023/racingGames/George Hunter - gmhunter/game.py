#############################
# Library Imports
#############################
from js import document, window

#############################
# Global Variables
#############################

# to store current position (x,y)
position = [0, 7]

# to store movement directions (x,y)
direction = [0, 0]


bag = [4,0]

audiocoin = document.getElementById("audiocoin")
audioFlag = document.getElementById("audioflag")
# to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 0

# round 1 track
track = [
    ["empty", "empty", "empty", "empty", "wallfake", "empty", "empty", "flag"],
    ["korokseed", "wall", "empty", "empty", "wall", "empty", "empty", "empty"],
    ["wall", "empty", "empty", "wall", "wall", "empty", "empty", "wall"],
    ["wall", "empty", "korokseed", "empty", "empty", "wallfake", "empty", "wall"],
    ["empty", "wall", "empty", "wall", "empty", "empty", "wall", "wall"],
    ["empty", "wall", "empty", "empty", "empty", "wall", "empty", "wall"],
    ["empty", "empty", "empty", "korokseed", "empty", "empty", "wallfake", "empty"],
    ["car", "empty", "empty", "empty", "empty", "wall", "korokseed", "empty"]
]
#############################
# Sub-Programs
#############################

def loadtrack():
    tableInnerHTML = ""
    for row in range(len(track)):
        tableInnerHTML += "<tr>"
        for col in range(len(track[0])):
            tableInnerHTML += "<td id= 'R{}C{}' class='{}'></td>".format(row, col, track[row][col])
        tableInnerHTML += "</tr>"
    document.getElementById("RacingTrack").innerHTML = tableInnerHTML


# the function called when a key is pressed - sets direction variable
def checkKey(event):
    event.preventDefault()
    if event.key == "D" or event.key == "d":
        direction[0] = 1
        direction[1] = 0
    elif event.key == "A" or event.key == "a":
        direction[0] = -1
        direction[1] = 0
    elif event.key == "W" or event.key == "w":
        direction[0] = 0
        direction[1] = -1
    elif event.key == "S" or event.key == "s":
        direction[0] = 0
        direction[1] = 1
    elif event.key == "R" or event.key == "r":
        postition[0] = 0
        position[1] = 7
        intervalHandle = 0
        direction[0] = 0
        direction[1] = 0
        loadtrack()
        runGame()

def getCell():
    return document.getElementById("R{}C{}".format(position[1],position[0]))


# the timer check function - runs every 300 milliseconds to update the car position
def updatePosition():
    if direction[0] != 0 or direction[1] != 0:
        # Set the cell where the car was to empty
        cell = getCell()
        cell.className = ""
        currClass = cell.className
        if direction[0] > 0:
            currClass = "car"
            currfakeClass = "carcopy"
        elif direction[0] < 0:
            currClass = "carflipethed"
            currfakeClass = "carflipethedcopy"
        elif direction[0] == 0:
            currClass = "car"
            currfakeClass = "carcopy"
        cell.className = ""     

        # Update the column position for the car
        position[0] += direction[0]
        position[1] += direction[1]

        # Re-draw the car (or report a crash)
        cell = getCell()
        if cell == None:
            handleCrash()
        elif cell.className == "wall":
            handleCrash()
        elif cell.className == "flag":
            cell.className = currClass
            bag[0] = bag[0] - bag[1]
            if bag[0] == 0:
                handlewin()
        elif cell.className == "korokseed":
            cell.className = currClass
            handlecoin()
            audiocoin.play()
        #elif cell.className == "wallfake":
         #   handlefaked()
        else:
            cell.className = currClass
            #direction[0] = 0
            #direction[1] = 0
    
# if the car has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Oops you crashed..."

def handlecoin():
    bag[1] = bag[1] + 1

def handlefaked():
    cell.className = currfakeClass

def handlewin():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "You Win"
# called when the page is loaded to start the timer checks
def runGame():
    loadtrack()
    global intervalHandle
    print("Running Game")
    document.addEventListener('keydown', checkKey)
    intervalHandle = window.setInterval(updatePosition, 300)

#############################
# Main Program
#############################

audiocoin.autoplay = False
audiocoin.load()
audioFlag.autoplay = False 
audioFlag.load()

loadtrack()

runGame()
