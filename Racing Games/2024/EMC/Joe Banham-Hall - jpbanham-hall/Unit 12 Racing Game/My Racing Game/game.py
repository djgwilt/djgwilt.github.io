#############################
# Library Imports
#############################
from js import document, window
from pyodide.ffi import create_proxy
import webbrowser
#############################
# Global Variables
#############################

track1 = [
    ["player1", "empty", "empty", "empty", "empty", "empty", "wall", "empty", "empty", "flag"],
    ["empty", "wall", "empty", "wall", "wall", "empty", "wall", "empty", "wall", "wall"],
    ["empty", "wall", "empty", "empty", "wall", "empty", "wall", "empty", "empty", "empty"],
    ["empty", "empty", "wall", "empty", "wall", "empty", "empty", "wall", "wall", "coin"],
    ["wall", "empty", "wall", "empty", "wall", "wall", "empty", "empty", "wall", "empty"],
    ["empty", "coin", "wallfake", "empty", "empty", "empty", "wall", "empty", "empty", "empty"],
    ["empty", "wall", "wall", "wall", "wall", "coin", "wall", "wallfake", "wall", "wall"],
    ["empty", "empty", "empty", "empty", "wall", "empty", "wall", "empty", "empty", "empty"],
    ["wall", "wall", "wall", "empty", "wall", "empty", "wall", "empty", "wall", "empty"],
    ["flag", "empty", "empty", "empty", "wall", "empty", "empty", "empty", "wall", "coin"]
]

track2 = [
   ["empty", "empty", "empty", "empty", "empty", "wall", "empty", "wall", "empty", "empty", "empty", "empty", "empty", "wall", "empty", "empty", "empty", "empty", "empty"],
   ["empty", "empty", "empty", "empty", "empty", "wall", "empty", "wall", "wall", "wall", "wall", "wall", "empty", "wall", "wall", "wall", "wall", "wall", "empty"],
   ["empty", "empty", "empty", "empty", "empty", "wall", "empty", "empty", "empty", "empty", "empty", "wall", "empty", "empty", "empty", "empty", "empty", "empty", "empty"],
   ["empty", "empty", "empty", "empty", "empty", "wall", "wall", "wall", "empty", "wall", "empty", "wall", "wall", "wall", "empty", "wall", "empty", "wall", "empty"],
   ["empty", "empty", "empty", "empty", "empty", "wall", "empty", "empty", "empty", "wall", "empty", "empty", "empty", "empty", "empty", "wall", "empty", "wall", "empty"],
   ["wall", "wall", "wall", "wall", "empty", "wall", "empty", "wall", "empty", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "empty", "wall", "wall"],
   ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "wall", "empty", "wall", "empty", "empty", "empty", "empty", "empty", "wall", "empty", "empty", "empty"],
   ["empty", "wall", "wall", "wall", "wall", "wall", "empty", "wall", "wall", "wall", "empty", "wall", "wall", "wall", "empty", "wall", "wall", "wall", "empty"],
   ["empty", "wall", "empty", "empty", "empty", "wall", "empty", "empty", "empty", "empty", "empty", "wall", "empty", "wall", "empty", "empty", "empty", "wall", "empty"],
   ["empty", "wall", "empty", "wall", "empty", "wall", "wall", "wall", "empty", "wall", "wall", "wall", "empty", "wall", "wall", "wall", "empty", "wall", "empty"],
   ["empty", "empty", "empty", "wall", "empty", "empty", "empty", "wall", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "wall", "empty", "wall", "empty"],
   ["wall", "wall", "empty", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "empty", "wall", "wall", "wall", "wall", "wall", "empty", "wall", "wall"],
   ["empty", "empty", "empty", "wall", "empty", "wall", "empty", "empty", "empty", "empty", "empty", "wall", "empty", "empty", "empty", "empty", "empty", "empty", "empty"],
   ["empty", "wall", "wall", "wall", "empty", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "empty", "wall", "wall", "wall", "wall", "wall", "wall"],
   ["empty", "empty", "empty", "wall", "empty", "empty", "empty", "wall", "empty", "empty", "empty", "wall", "empty", "wall", "empty", "empty", "empty", "empty", "empty"],
   ["wall", "wall", "empty", "wall", "wall", "wall", "empty", "wall", "empty", "wall", "empty", "wall", "empty", "wall", "empty", "wall", "wall", "wall", "empty"],
   ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"],
   ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"],
   ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"]
]

# to store current position (x,y)
position = [0, 0]

# to store movement directions (x,y)
direction = [0, 0]

bag = [2,0]

# to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 0


audioFlag = document.getElementById("audioFlag")
audioCoin = document.getElementById("audioCoin")
audioCrash = document.getElementById("audioCrash")
audioWin = document.getElementById("audioWin")

#############################
# Sub-Programs
#############################

def loadtrack1():
    tableInnerHTML = ""
    for row in range(len(track1)):
        tableInnerHTML += "<tr>"
        for col in range(len(track1[0])):
            tableInnerHTML += "<td id='R{}C{}' class='{}'></td>".format(row, col, track[row][col])
        tableInnerHTML += "</tr>"
    document.getElementById("RacingTrack").innerHTML = tableInnerHTML

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
        # up arrow
        direction[1] = -1
        direction[0] = 0
    elif event.key == "ArrowDown":
        # down arrow
        direction[1] = 1
        direction[0] = 0
        #webbrowser.open_new('https://www.youtube.com/watch?v=5Hhti1JyH70')

def getCell():
    return document.getElementById("R{}C{}".format(position[1], position[0]))

# the timer check function - runs every 300 milliseconds to update player1's position
def updatePosition():
    if direction[0] != 0 or direction[1] != 0:
        # Set the cell where player1 was to empty
        cell = getCell()
        if direction[0] > 0:
            player1Class = "player1"
        elif direction[1] > 0:
            player1Class = "player1"
        elif direction[0] < 0:
            player1Class = "player1"
        elif direction[1] < 0:
            player1Class = "player1"
        else:
            player1Class = cell.className = ""
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
            audioCrash.play()
        elif cell.className == "coin":
            cell.className = player1Class
            bag [1] = bag[1] + 1
            audioCoin.play()
        elif cell.className == "flag":
            audioFlag.play()
            cell.className = player1Class
            bag[0] = bag[0] - 1
            if bag[0] == 0:
                handleWin()
                
        else:
            cell.className = player1Class

# if player1 has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "L bozo yellow larvae on top"

def handleWin():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "You absolutely bum sweated on yellow larvae and won {} donuts!".format(bag[1])
    audioWin.play()

# called when the page is loaded to start the timer checks
def runGame():
    global intervalHandle
    print("Running Game")
    document.addEventListener('keydown', create_proxy(checkKey))
    intervalHandle = window.setInterval(create_proxy(updatePosition), 300)

#############################
# Main Program
#############################

audioFlag.autoplay = False
audioFlag.load()
audioWin.autoplay = False
audioWin.load()
audioCoin.autoplay = False
audioCoin.load()
audioCrash.autoplay = False
audioCrash.load()

loadtrack1()

runGame()
