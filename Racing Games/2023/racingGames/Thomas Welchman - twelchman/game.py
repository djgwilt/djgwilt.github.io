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

bag = [1,0]

audioCoin=document.getElementById("audioCoin")
audioFlag=document.getElementById("audioFlag")
audioWall=document.getElementById("audioWall")
audioKey=document.getElementById("audioKey")
# to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 0

#############################
# Sub-Programs
#############################

# the function called when a key is pressed - sets direction variable
def checkKey(event):
    event.preventDefault()

    if event.key == "ArrowRight" or event.key.lower() == "d":
        direction[0] = 1
        direction[1] = 0
    elif event.key == "ArrowLeft" or event.key.lower() == "a":
        # left arrow
        direction[0] = -1
        direction[1] = 0
    elif event.key == "ArrowDown" or event.key.lower() == "s":
        direction[0] = 0
        direction[1] = 1
    elif event.key == "ArrowUp" or event.key.lower() == "w":
        direction[0] = 0
        direction[1] = -1

def getCell():
    return document.getElementById("R{}C{}".format(position[1],position[0]))

# the timer check function - runs every 300 milliseconds to update the car position
def updatePosition():
    audioKey.play()
    if direction[0] != 0 or direction[1] != 0:
        # Set the cell where the car was to empty
        cell = getCell()
        cell.className = ""
        
        # Update the column position for the car
        position[0] += direction[0]
        position[1] += direction[1]

        # Re-draw the car (or report a crash)
        cell = getCell()
        if cell == None:
          handleCrash()
        elif cell.className == "wall" or cell.className == "coinFake":
          audioWall.play()
          handleCrash()
        elif cell.className == "coin":
           cell.className = "car"
           bag[1] = bag[1] + 1
           audioCoin.play()
        elif cell.className == "flag":
          if bag[0] == bag[1]:
             audioFlag.play()
             handleWin()
        else:
          cell.className = "car"

# if the car has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "You crashed you silly suster"
    audioKey.stop()

# called when the page is loaded to start the timer checks
def runGame():
    global intervalHandle
    print("Running Game")
    document.addEventListener('keydown', checkKey)
    intervalHandle = window.setInterval(updatePosition, 250)

def handleWin():
  window.clearInterval(intervalHandle)
  document.getElementById("Message").innerText =( "You won and got away from the suster!!!!1!!!1!!!")
  audioKey.stop()

#############################
# Main Program
#############################
audioCoin.autoplay = False
audioCoin.load()
audioFlag.autoplay = False
audioFlag.load()
audioWall.autoplay = False
audioWall.load()
audioKey.autoplay = False
audioKey.load()
runGame()
