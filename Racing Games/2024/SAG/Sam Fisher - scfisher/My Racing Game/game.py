#############################
# Library Imports
#############################
from js import document, window
from pyodide.ffi import create_proxy

#############################
# Global Variables
#############################

# to store current position (x,y)
position = [7, 4]

# to store movement directions (x,y)
direction = [0, 0]

bag = [2, 0]
track = [ 
    
    # ["car", "empty"],
    #      ["empty", "empty"]]


          ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"]     ,  
          ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"] ,
          ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"]  ,
          ["empty", "empty", "empty", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"]  ,
          ["empty", "empty", "wall", "empty", "empty", "flag", "wall", "player1", "empty", "empty", "empty", "empty", "empty", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall",]  ,
          ["empty", "empty", "wall", "empty", "wall", "wall", "wall", "wall", "wall", "wall", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "wall"]  ,
          ["empty", "empty", "wall", "empty",  "wall", "empty", "empty", "empty", "empty",  "wall", "wall","wall","wall","wall","wall","wall","wall","wall","wall","wall","wall","wall","wall","wall","wall","wall","wall","empty","empty","wall",]  ,
          ["empty", "empty", "wall", "empty", "empty", "empty", "wall", "wall", "empty", "empty", "wall", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "wall", "empty", "wall", "wall"]  ,
          ["empty", "empty", "empty", "wall", "wall", "wall", "empty", "empty", "wall", "empty", "empty", "wall", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "wall", "empty", "empty", "wall"]  ,
          ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "wall", "empty", "empty", "wall", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "wall", "empty", "empty", "wall", "empty"]  ,
          ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "wall", "empty", "empty", "wall", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "wall", "empty", "empty", "wall", "empty", "empty"]  ,
          ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "wall", "empty", "empty", "wall", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "wall", "empty", "empty", "wall", "empty", "empty", "empty"]  ,
          ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "wall", "empty", "empty", "wall", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "wall", "empty", "empty", "wall", "empty", "empty", "empty"]  ,
          ["empty", "empty", "wall", "wall", "wall", "wall", "empty", "empty", "empty", "wall", "wall", "empty", "empty", "wall", "empty", "wall", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "wall", "empty", "empty", "wall", "empty", "empty", "empty"]  ,
          ["empty", "wall", "empty", "empty", "empty", "empty", "wall", "empty", "wall", "empty", "empty", "wall", "empty", "wall", "empty", "wall", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "wall", "empty", "empty", "wall", "empty", "empty"]  ,
          ["wall", "empty", "empty", "wall", "wall", "empty", "empty", "wall", "empty", "empty", "empty", "empty", "wall", "empty", "empty", "wall", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "wall", "empty", "empty", "wall", "empty"]  ,
          ["wall", "empty", "wall", "empty", "empty", "wall", "empty", "empty", "empty", "wall", "wall", "empty", "empty", "empty", "empty", "wall", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "wall", "empty", "empty", "wall"]  ,
          ["wall", "empty", "wall", "empty", "empty", "empty", "wall", "wall", "wall", "empty", "empty", "wall", "wall", "wall", "wall", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "wall", "empty", "empty", "wall", "empty"]  ,
          ["wall", "empty", "wall", "empty", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "wall", "empty", "empty", "wall", "empty", "empty"]  ,
          ["wall", "empty", "wall", "wall", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "wall", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "wall", "empty", "empty", "wall", "empty", "empty", "empty"]  ,
          ["wall", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "wall", "empty", "empty", "empty", "empty", "empty", "wall", "empty", "empty", "wall", "empty", "empty", "empty", "empty"]  ,
          ["empty", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "empty", "empty", "wall", "wall", "wall", "wall", "wall", "empty", "empty", "wall", "empty", "empty", "empty", "empty", "empty"]  ,
          ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "wall", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "wall", "empty", "empty", "empty", "empty", "empty", "empty"]  ,
          ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "wall", "wall", "wall", "wall", "wall", "wall", "wall", "empty", "empty", "empty", "empty", "empty", "empty", "empty"]  ,
          ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"]                                    
       ] 
# to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 0

audioFlag = document.getElementById("audioFlag")
audioWin = document.getElementById("audioWin")
audioCoin = document.getElementById("audioCoin")
audioCrash = document.getElementById("audioCrash")

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
    elif event.key == "ArrowDown":
        direction[0] = 0
        direction[1] = 1
    elif event.key == "ArrowUp":
        direction[0] = 0
        direction[1] = -1


def getCell():
    return document.getElementById("R{}C{}".format(position[1], position[0]))

# the timer check function - runs every 300 milliseconds to update player1's position
def updatePosition():
    if direction[0] != 0 or direction[1] != 0 :
        # Set the cell where player1 was to empty
        cell = getCell()
        if cell == None:
            return
        if direction[0] >= 0:
            player1Class = "player1"
        elif direction[0] < 0:
            player1Class = "player1-left"
        else:
            player1Class = cell.className
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
        elif cell.className == "flag":
            handleWin()
        elif cell.className == "coin":
            cell.className = player1Class
        else:
            cell.className = player1Class

# if player1 has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Oops you crashed..."
    audioCrash.play()

# called when the page is loaded to start the timer checks
def runGame():
    global intervalHandle
    print("Running Game")
    document.addEventListener('keydown', create_proxy(checkKey))
    intervalHandle = window.setInterval(create_proxy(updatePosition), 300)

def handleWin():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "You Win the Miami Grand Prix!"
    audioWin.play()

def loadTrack():    
    tableInnerHTML = ""
    for row in range(len(track)):
        tableInnerHTML += "<tr>"
        for col in range(len(track[0])):
            tableInnerHTML += "<td id='R{}C{}' class='{}'></td>".format(row, col, track[row][col])
    tableInnerHTML += "</tr>"
    document. getElementById("RacingTrack"). innerHTML = tableInnerHTML



#############################
# Main Program
#############################


audioFlag.autoplay = False
audioFlag.load()
audioFlag.autoplay = False
audioWin.load()
audioFlag.autoplay = False
audioCoin.load()
audioFlag.autoplay = False
audioCrash.load()

loadTrack()

runGame()
