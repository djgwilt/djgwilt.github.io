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

key = 2
coin = 0
#audio variables
audiocoin = document.getElementById("audiocoin")
audiocrash = document.getElementById("audiocrash")
audiokeys = document.getElementById("audiokeys")
audiochest = document.getElementById("audiochest")
#############################
# Sub-Programs
#############################

# the function called when a key is pressed - sets direction variable
def checkKey(event):
    global intervalHandle
    global w
    global a
    global s
    global d
    global input_type
    event.preventDefault()  # this will prevent the down arrow from scrolling the page
    if input_type == "arrows":
        if event.key == "ArrowRight":
            direction[0] = 1
            direction[1] = 0
        elif event.key == "ArrowLeft":
            # left arrow
            direction[0] = -1
            direction[1] = 0
        elif event.key == "ArrowUp":
            direction[0] = 0
            direction[1] = -1
        elif event.key == "ArrowDown":
            direction[0] = 0
            direction[1] = 1
    elif input_type == "wasd":
        if event.key == "d":
            direction[0] = 1
            direction[1] = 0
        elif event.key == "a":
            # left arrow
            direction[0] = -1
            direction[1] = 0
        elif event.key == "w":
            direction[0] = 0
            direction[1] = -1
        elif event.key == "s":
            direction[0] = 0
            direction[1] = 1
    elif input_type == "custom":
        if event.key == (d):
            direction[0] = 1
            direction[1] = 0
        elif event.key == (a):
            # left arrow
            direction[0] = -1
            direction[1] = 0
        elif event.key == (w):
            direction[0] = 0
            direction[1] = -1
        elif event.key == (s):
            direction[0] = 0
            direction[1] = 1

def getCell():
    return document.getElementById("R{}C{}".format(position[1],position[0]))

# the timer check function - runs every 300 milliseconds to update the car position
def updatePosition():
    global intervalHandle
    global key
    global coin
    if direction[0] != 0 or direction[1] != 0:
        # Set the cell where the car was to empty
        cell = getCell()
        if direction[0] > 0:
            player1class = "car"
        elif direction[0] < 0:
            player1class = "carleft"
        else:
            player1class = cell.className
        cell.className = ""
        
        # Update the column position for the car
        position[0] += direction[0]
        position[1] += direction[1]

        # Re-draw the car (or report a crash)
        cell = getCell()
        if cell == None:
            audiocrash.play()
            handleCrash()
        elif cell.className == "wall":
            audiocrash.play()
            handleCrash()
        elif cell.className == "closed":
            if key == 0:
                handleWin()
        elif cell.className == "key":
            audiokeys.play()
            cell.className = player1class
            key = key - 1
        elif cell.className == "coin":
            audiocoin.play()
            coin = coin + 1
            if coin == 1:
                print ("You have collected {} coin so far!".format(coin))
            else:
                print ("You have collected {} coins so far!".format(coin))
            cell.className = player1class
        else:
            cell.className = player1class

# if the car has gone off the table, this tidies up including crash message
def handleCrash():
        window.clearInterval(intervalHandle)
        document.getElementById("Message").innerText = "Oops you crashed..."
    

# called when the page is loaded to start the timer checks
def runGame():
    global intervalHandle
    global w
    global a
    global s
    global d
    global input_type
    global speed
    print("Running Game")
    
    input_type = input("What type of input do you want to use to move?\nType 'arrows' for arrow keys, 'wasd' for WASD or 'custom' for custom input:")
    if input_type == "custom":
        w = input("What button do you want to use to go up")
        a = input("What button do you want to use to go left")
        s = input("What button do you want to use to go down")
        d = input("What button do you want to use to go right")
    speed = input ("How fast do you want to go (difficulty)?\nType 1 for level 1 difficulty:\nType 2 for level 2 difficulty:\nType 3 for level 3 difficulty:\nType 4 for level 4 difficulty:\nType 5 for *Impossible mode*:")
    if speed == "1":
        document.addEventListener('keydown', checkKey)
        intervalHandle = window.setInterval(updatePosition, 1000)
    elif speed == "2":
        document.addEventListener('keydown', checkKey)
        intervalHandle = window.setInterval(updatePosition, 700)
    elif speed == "3":
        document.addEventListener('keydown', checkKey)
        intervalHandle = window.setInterval(updatePosition, 450)
    elif speed == "4":
        document.addEventListener('keydown', checkKey)
        intervalHandle = window.setInterval(updatePosition, 300)
    elif speed == "5":
        document.addEventListener('keydown', checkKey)
        intervalHandle = window.setInterval(updatePosition, 200)




def handleWin():
    audiochest.play()
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "You win and collected {} coins!".format(coin)
    cell = getCell()
    cell.className = "open"
#############################
# Main Program
#############################
#load in audio files ready for use
audiocoin.autoplay = False
audiocoin.load()
audiocrash.autoplay = False
audiocrash.load()
audiochest.autoplay = False
audiochest.load()
runGame()
