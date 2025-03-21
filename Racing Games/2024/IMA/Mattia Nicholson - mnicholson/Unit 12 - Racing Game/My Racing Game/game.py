#############################
# Library Imports
#############################
from js import document, window # type: ignore

#############################
# Global Variables
#############################

# to store current position (x,y)
position = [0, 0]

# to store movement directions (x,y)
direction = [0, 0]

coin = 0

secretdiddymist = document.getElementById("secretdiddymist")
adlib = document.getElementById("adlib")
ken = document.getElementById("ken")


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
        direction[0] = 0  # Set meaningful value for moving up
        direction[1] = -1  # Set meaningful value for moving up
    elif event.key == "ArrowDown":
        direction[0] = 0  # Set meaningful value for moving down
        direction[1] = 1  # Set meaningful value for moving down

def getCell():
    return document.getElementById("R{}C{}".format(position[1], position[0]))

# the timer check function - runs every 300 milliseconds to update the car position
def updatePosition():
    global coin
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
            handleCrash()
        elif cell.className == "wall":
            handleCrash()
        elif cell.className == "coin":
            cell.className = "car"
            coin = coin + 1
            if coin == 1:
                print("You have collected {} chip".format(coin))
            else:
                print("You have collected {} chips".format(coin))
            adlib.play()
        elif cell.className == "flag":
            cell.className = "car"
            handleWin()
        else:
            cell.className = "car"

# if the car has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Gng done crashed🙏🏻🙏🏻👶🏿"
    ken.play()

# called when the page is loaded to start the timer checks
def runGame():
    global intervalHandle
    print("Running Game")
    document.addEventListener('keydown', checkKey)
    intervalHandle = window.setInterval(updatePosition, 300)

def handleWin():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Gng done won🙌🏻🙌🏻 and you got {} fries".format(coin)  # type: ignore
    secretdiddymist.play()

#############################
# Main Program
#############################

secretdiddymist.autoplay = False
secretdiddymist.load()
adlib.autoplay = False
adlib.load()
ken.autoplay = False
ken.load()

runGame()
