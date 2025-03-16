#############################
# Library Imports
#############################
from js import document, window

#############################
# Global Variables
#############################

# audio variables
quasarAudio = document.getElementById('quasarAudio')
shinyRockAudio = document.getElementById('shinyRockAudio')

# to store current position (x,y)
position = [0, 0]

# to store movement directions (x,y)
direction = [0, 0]

bag = [3, 0]

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
    elif event.key == "ArrowDown":
        direction[0] = 0
        direction[1] = 1
    elif event.key == "ArrowUp":
        direction[0] = 0
        direction[1] = -1


def getCell():
    return document.getElementById("R{}C{}".format(position[1], position[0]))

# the timer check function - runs every 300 milliseconds to update the car position
def updatePosition():
    if direction[0] != 0 or direction[1] != 0:
        # Set the cell where the car was to empty
        cell = getCell()
        currClass = cell.className
        if direction[0] > 0:
            currClass = 'spaceship'
        elif direction[0] < 0:
            currClass = 'spaceshipFlipped'
        if cell != None:
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
        elif cell.className == 'earth':
            handleWin()
        elif cell.className == 'quasar':
            cell.className = currClass
            bag[0] = bag[0] - 1
            if bag[0] != 3:
                audioQuasar.play()
            if bag[0] == 0:
                handleWin()
        elif cell.className == 'shinyRock':
            cell.className = currClass
            bag[1] = bag[1] + 1
            if bag[1] != 0:
                audioShinyRock.play()
        else:
            cell.className = currClass

# if the car has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Oops you crashed..."

def handleWin():
    window.clearInterval(intervalHandle)
    document.getElementById('Message').innerText = 'You win and scored {} coins!'.format(bag[1])

# called when the page is loaded to start the timer checks
def runGame():
    global intervalHandle
    print("Running Game")
    document.addEventListener('keydown', checkKey)
    intervalHandle = window.setInterval(updatePosition, 300)

#############################
# Main Program
#############################

quasarAudio.autoplay = False
quasarAudio.load()
shinyRockAudio.autoplay = False
shinyRockAudio.load()

runGame()
