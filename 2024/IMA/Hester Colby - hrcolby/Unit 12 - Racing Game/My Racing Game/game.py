#############################
# Library Imports
#############################
from js import document, window

#############################
# Global Variables
#############################

# to store current position (x,y)
positionplayer1 = [0, 0]
positionplayer2 = [0, 0]
# to store movement directions (x,y)
directionplayer1 = [0, 0]
directionplayer2 = [0, 0]
# to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 0

#to show when player 1 has enough food to rest


#############################
# Sub-Programs
#############################

# the function called when a key is pressed - sets direction variable
def checkKey(event):
    event.preventDefault()
    # player 1
    cell = getCell()
    if event.key == "ArrowRight":
        directionplayer1[0] = 1
    elif event.key == "ArrowLeft":
        # left arrow
        directionplayer1[0] = -1
    if event.key == "ArrowUp":
        if "pole" in cell.className:
            directionplayer1[1] = -1
    elif event.key == "ArrowDown":
        if "pole" in cell.className:
            directionplayer1[1] = 1
    # player 2
    elif event.key == "KeyD":
        directionplayer2[0] = 1
    elif event.key == "KeyA":
        directionplayer2[0] = -1
    elif event.key == "KeyW":
        if "pole" in cell.classname:
            directionplayer2[1] = -1
    elif event.key == "KeyS":
        if "pole" in cell.classname:
            directionplayer2[1] = 1
    

            
def checkKeyUp(event):
    event.preventDefault()
    directionplayer1[1] = 0
    directionplayer1[0] = 0
    directionplayer2[1] = 0
    directionplayer2[0] = 0


def getCell():
    return document.getElementById("R{}C{}".format(positionplayer1[1],positionplayer1[0]))

foodcount = 0
# the timer check function - runs every 300 milliseconds to update the car position
def updatePosition():
    # player 1
    global foodcount
    if directionplayer1[0] != 0 or directionplayer1[1] != 0:
        # Set the cell where the car was to empty
        cell = getCell()
        if cell.className.endswith("slugcat"):
            cell.className = cell.className[:-len(" slugcat")]
        if cell.className == ("food"):
            cell.className = cell.className[:-len("food")]
        # Update the column position for the car
        positionplayer1[0] += directionplayer1[0]
        positionplayer1[1] += directionplayer1[1]

        
        # Re-draw the car (or report a crash)
        cell = getCell()
        if cell == None:
            handleCrash()
        elif cell == "wall":
            handleCrash()
        elif cell.className == "flag":
            if foodcount >= 5: #checking for enough food to trigger win
                handleWin()
        elif cell.className == "food": #add to food whenever player gets food
            foodcount = foodcount + 1
        elif cell.className == "PassageDark1":
            positionplayer1[0] = 3
            positionplayer1[1] = 8
        else:
            cell.className += " slugcat" 
        
    #player 2
    if directionplayer2[0] != 0 or directionplayer2[1] != 0:
        # Set the cell where the car was to empty
        cell = getCell()
        if cell.className.endswith("lizard"):
            cell.className = cell.className[:-len(" lizard")]
        
        # Update the column position for the car
        positionplayer2[0] += directionplayer2[0]
        positionplayer2[1] += directionplayer2[1]

        #redraw car, report crash or trigger win
        cell = getCell()
        if cell == None:
            handleCrash()
        elif cell == "wall":
            handleCrash()
        elif cell.className == "slugcat":
                handleWin()
        elif cell.className == "PassageDark1":
            positionplayer2[0] = 3
            positionplayer2[1] = 8
        else:
            cell.className += " lizard" 

# if the car has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Oops, you hit a wall..."

# called when the page is loaded to start the timer checks
def runGame():
    global intervalHandle
    print("Running Game")
    document.addEventListener('keydown', checkKey)
    document.addEventListener('keyup', checkKeyUp)
    intervalHandle = window.setInterval(updatePosition, 300)

def handleWin():
     window.clearInterval(intervalHandle)
     document.getElementbyId("message").innerText = "Player 1 Wins!"



#############################
# Main Program
#############################

runGame()
