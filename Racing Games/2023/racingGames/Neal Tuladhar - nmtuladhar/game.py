#############################
# Library Imports
#############################
from js import document, window

#############################
# Global Variables
#############################

# to store current position (x,y)
position1 = [0, 0]
direction1 = [0, 0]

position2 = [7,6]
direction2 = [0,0]

# to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 0

#to store flages left to collect and coins collected
bag1=[2,0]
bag2=[2,0]

#audio variables
audioCrash = document.getElementById("audioCrash")
audioWin = document.getElementById("audioWin")
audioCoin = document.getElementById("audioCoin")

#############################
# Sub-Programs
#############################

# the function called when a key is pressed - sets direction variable
def checkKey(event):
    event.preventDefault()
    if event.key == "ArrowRight":
        direction1[0] = 1
        direction1[1] = 0
    elif event.key == "ArrowLeft":
        # left arrow
        direction1[0] = -1
        direction1[1] = 0
    elif event.key == "ArrowUp":
        #up arrow
        direction1[0] = 0
        direction1[1] = -1
    elif event.key == "ArrowDown":
        #down arrow
        direction1[0]=0
        direction1[1]=1
    elif event.key == "w":
        #up
        direction2[0] = 0
        direction2[1] = -1
    elif event.key == "a":
        #left
        direction2[0] = -1
        direction2[1] = 0
    elif event.key == "s":
        #down
        direction2[0] = 0
        direction2[1] = 1
    elif event.key == "d":
        direction2[0] = 1
        direction2[1] = 0
   

def getCell1():
    return document.getElementById("R{}C{}".format(position1[1], position1[0]))

def getCell2():
    return document.getElementById("R{}C{}".format(position2[1], position2[0]))

# the timer check function - runs every 300 milliseconds to update the car position
def updatePosition():
    if direction1[0] != 0 or direction1[1] != 0 :
        # Set the cell where the car was to empty
        cell = getCell1()
        curClass=cell.className
        if direction1[0]>0:
            curClass = "player1"
        elif direction1[0]<0:
            curClass = "player1flip"
        cell.className = ""
        
        # Update the column position for the car
        position1[0] += direction1[0]
        position1[1] += direction1[1]

        # Re-draw the car (or report a crash)
        cell = getCell1()
        if cell == None:
            handleCrash()
        elif cell.className == "wall":
            handleCrash()
            audioCrash.play()
        elif cell.className == "powerup":
            cell.className = curClass
            audioCoin.play()
            bag1[1] = bag1[1] + 1
        elif cell.className == "flag": 
            cell.className = curClass
            if bag1[0] == bag1[1]:
                audioWin.play()
                handleWin()
        else:
            cell.className = curClass
            
    if direction2[0] != 0 or direction2[1] != 0 :
        # Set the cell where the car was to empty
        cell = getCell2()
        curClass=cell.className
        if direction2[0]>0:
            curClass = "player2"
        elif direction2[0]<0:
            curClass = "player2flip"
        cell.className = ""
        
        # Update the column position for the car
        position2[0] += direction2[0]
        position2[1] += direction2[1]

        # Re-draw the car (or report a crash)
        cell = getCell2()
        if cell == None:
            handleCrash()
        elif cell.className == "wall":
            handleCrash()
            audioCrash.play()
        elif cell.className == "powerup":
            cell.className = curClass
            audioCoin.play()
            bag2[1] = bag2[1] + 1
        elif cell.className == "flag": 
            cell.className = curClass
            if bag2[0] == bag2[1]:
                audioWin.play()
                handleWin()
        else:
            cell.className = curClass

# if the car has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Oops you crashed..."

def handleWin():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "You Win and scored {} coins!".format(bag[1])

# called when the page is loaded to start the timer checks
def runGame():
    global intervalHandle
    print("Running Game")
    document.addEventListener('keydown', checkKey)
    intervalHandle = window.setInterval(updatePosition, 300)

#############################
# Main Program
#############################

#load in audio files
audioCrash.autoplay = False
audioCrash.load()
audioWin.autoplay = False
audioWin.load()
audioCoin.autoplay = False
audioCoin.load()


runGame()
