#############################
# Library Imports
#############################
from js import document, window
from pyodide.ffi import create_proxy

#############################
# Global Variables
#############################

# to store current position (x,y)
position = [0, 0]

# to store movement directions (x,y)
direction = [0, 0]
timer = 0
bob = 1
coincount = 0
# to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 0
def getCellByXY(x, y):
    return document.getElementById("R{}C{}".format(y,x))

player = getCellByXY(0,0)


sure = "n"
chosenskin = 1
while sure == "n":
    chosenskin = input("Choose your skin, 1-9")
    sure = input("Are you sure (y/n)")
if chosenskin == "1":
    player1skin = "player1"
elif chosenskin == "2":
    player1skin = "player2"
elif chosenskin == "3":
    player1skin = "player3"
elif chosenskin == "4":
    player1skin = "player4"
elif chosenskin == "5":
    player1skin = "player5"
elif chosenskin == "6":
    player1skin = "player6"
elif chosenskin == "7":
    player1skin = "player7"
elif chosenskin == "8":
    player1skin = "player8"
elif chosenskin == "9":
    player1skin = "player9"
elif chosenskin == "!":
    player1skin = "player10"
elif chosenskin == ".":
    player1skin = "player11"
player.className = player


def handleMOVE():
    global timer
    global bob
    global player1skin
    cell1 = getCellByXY(4,1)
    cell2 = getCellByXY(4,2)
    if bob == 1:
        if timer == 3:
            if cell1.className == "wall3":
                if cell2.className == player1skin:
                    handleCrash()
                    cell1.className = ""
                    cell2.className = "wall3"
                else:
                    cell1.className = ""
                    cell2.className = "wall3"
            elif cell2.className == "wall3":
                if cell2.className == player1skin:
                    handleCrash()
                    cell2.className = ""
                    cell1.className = "wall3"
                else:
                    cell2.className = ""
                    cell1.className = "wall3"
            timer = 0
        else:
            timer = timer + 1

#############################
# Sub-Programs
#############################

# the function called when a key is pressed - sets direction variable
def handleWin():
    window.clearInterval(intervalHandle)
    if coincount==2:
        if chosenskin == ".":
            document.getElementById("Message").innerText = "You win, but why did u choose that skin!?!?!??!?!?"
        else:   
            document.getElementById("Message").innerText = "You win with all coins!"   
    else:
        document.getElementById("Message").innerText = "You win! Next time try and get all the coins"
def checkKey(event):
    event.preventDefault()
    if event.key == "ArrowRight":
        direction[0] = 1
        direction[1] = 0
    elif event.key == "ArrowLeft":
        # left arrow
        direction[0] = -1
        direction[1] = 0
    elif event.key == "ArrowUp" :
        direction[0] = 0
        direction[1] = -1
    elif event.key == "ArrowDown" :

       direction[0] = 0
       direction[1] = 1

def updatePosition(): 
    global coincount
    global timer
    handleMOVE()
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

        elif cell.className == "wall" or cell.className == "wall2" or cell.className == "wall3":

            handleCrash() 

        elif cell.className == "flag":
            handleWin()
        elif cell.className == "coin":
            cell.className = player1skin
            coincount = coincount + 1
        else:
            cell.className = player1skin 
            
def getCell():
    return document.getElementById("R{}C{}".format(position[1], position[0]))



# the timer check function - runs every 300 milliseconds to update player1's position

# if player1 has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "You dissapointed me, you dissapointed your family, and most of all you dissapointed darwin. Speaking of Darwin, play his game with the link https://www.bing.com/search?q=short&gs_lcrp=EgZjaHJvbWUqBggAEEUYOzIGCAAQRRg7MgYIARBFGDwyBwgCEOkHGEAyBwgDEOkHGEAyBwgEEOkHGEAyBwgFEOkHGEAyCAgGEOkHGPxV0gEHNjU1ajBqMagCALACAA&FORM=ANAB01&DAF0=1&PC=U531&adlt=strict"

# called when the page is loaded to start the timer checks
def runGame():
    global intervalHandle
    print("Running Game")
    document.addEventListener('keydown', create_proxy(checkKey))
    intervalHandle = window.setInterval(create_proxy(updatePosition), 300)

#############################
# Main Program
#############################

runGame()
