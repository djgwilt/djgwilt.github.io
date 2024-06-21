#############################
# Library Imports
#############################
from js import document, window

#############################
# Global Variables
audiocrash = document.getElementById("audiocrash")
audiofein = document.getElementById("audiofein")
money = 0
#############################
def getCell():
    return document.getElementById("R{}C{}".format(direction[0], position[0]))
# to store current position (x,y)
position = [0, 0]

# to store movement directions (x,y)
direction = [0, 0]

# to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 0

#############################
# Sub-Programs
#############################

# the function called when a key is pressed - sets direction variable
def checkKey(event):
    event.preventDefault()  # this will prevent the down arrow from scrolling the page
    if event.key == "ArrowRight":
        direction[0] = 1
        direction[1] = 0
    elif event.key == "ArrowLeft":
        # left arrow
        direction[0] = -1
        direction[1] = 0
    elif event.key == "ArrowUp":
        # up arrow
        direction[0] = 0
        direction[1] = -1
    elif event.key == "ArrowDown":
        # down arrow
        direction[0] = 0
        direction[1] = 1

def getCell():
    return document.getElementById("R{}C{}".format(position[1],position[0]))



# the timer check function - runs every 300 milliseconds to update the car position
def updatePosition():
    global money
    if direction[0] != 0 or direction[1] != 0:
        # Set the cell where player1 was to empty
        cell = getCell()
        cell.className = ""
        
        # Update the column position for player1
        position[0] += direction[0]
        position[1] += direction[1]


        
        # Re-draw player1 (or report a crash)
    
        cell = getCell()
        if cell == None:
            audiocrash.play()
            handleCrash()
        elif cell.className == "wall":
            audiocrash.play()
            handleCrash()
        elif cell.className == "finish":
            cell.className = "car"
            handleWin()
            audiofein.play()
        elif cell.className == "money":
            cell.className = "car"
            money = money + 1

        else:
            cell.className = "car"
            

# if the car has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Done easy nice"
def handleWin():
        global money
        window.clearInterval(intervalHandle)
        document.getElementById("Message").innertext = "Win and scored {} coins!".format(money)
        

# called when the page is loaded to start the timer checks
def runGame():
    global intervalHandle
    print("Running Game")
    document.addEventListener('keydown', checkKey)
    intervalHandle = window.setInterval(updatePosition, 200)

#############################
# Main Program
#############################

audiocrash.autoplay = False
audiocrash.load()
audiofein.autoplay = False
audiofein.load()


runGame()
