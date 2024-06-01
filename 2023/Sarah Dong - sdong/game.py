#############################
# Library Imports
#############################
from js import document, window

#audio variables
audioopen = document.getElementById("audioopen")

#############################
# Global Variables?
#############################

# to store current position (x,y)
position = [1, 1]
moster_pos = [2,5]
# to store movement directions (x,y)
direction = [0, 0]
monster_direction = [1,1]

# to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 0

#to store flags left to collect and coins collected
bag = [1,0,0]

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
    elif event.key == "ArrowUp":
        direction[0] = 0
        direction[1] = -1
    elif event.key == "ArrowDown":
        direction[0] = 0
        direction[1] = 1
        
#def monstercell():
#    return document.getElementById("R{}C{}".format(moster_pos[1],moster_pos[0]))

#def monstermove():    
#    if direction[0] != 0 or direction[1] != 0:
        # Set the cell where the car was to empty
#        monstercell = monstercell()
        # Update the column position for the car
#        moster_pos[0] += monster_direction[0]
#        moster_pos[1] += monster_direction[1]
        
        #3 coins, 3 flags
        # Re-draw the car (or report a crash)
#        if monstercell.className == "wall":
#            moster_pos[0] -= monster_direction[0]
#            moster_pos[1] -= monster_direction[1]
#        else:
#            moster_pos[0] += monster_direction[0]
#            moster_pos[1] += monster_direction[1]

def getCell():
    return document.getElementById("R{}C{}".format(position[1],position[0]))

# the timer check function - runs every 300 milliseconds to update the car position
def updatePosition():
    if direction[0] != 0 or direction[1] != 0:
        # Set the cell where the car was to empty
        cell = getCell()
        currClass = cell.className
        if direction[0]>0:
            currClass = "flappy"
        elif direction[0]<0:
            currClass = "flip"
        cell.className = ""
        
        # Update the column position for the car
        position[0] += direction[0]
        position[1] += direction[1]

        #3 coins, 3 flags
        # Re-draw the car (or report a crash)
        cell = getCell()
        if cell == None:
            handleCrash()
        elif cell.className == "wall":
            handleCrash()
        elif cell.className == "monster":
            handlemonster()
        elif cell.className == "coin":
            cell.className == currClass
            bag[1]=bag[1]+1
            if bag[1] == 5:
                print("the code is 3192")
            document.getElementById("Message").innerText = f"Coins: {bag[1]}"
        elif cell.className == "key":
            bag[2]=1
        elif cell.className == "door":
            if bag[2]==1:
                bag[0] = bag[0]-1
                if bag[0] == 0:
                    code = int(input("enter the code"))
                    if code == 3192:
                        handleWin()
                    else:
                        codewrong()
            else:
                lockeddoor()
        else:
            cell.className = currClass

# if the car has gone off the table, this tidies up including crash message

def codewrong():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Wrong code"
    
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Oops you crashed...\n Try again?"

# called when the page is loaded to start the timer checks
def runGame():
    global intervalHandle
    print("Running Game")
    print("get the key and code to unlock the door")
    print("Collect 5 coins to get the code")
    print("Don't touch the mblue monsters")
    print("when you collect 5 or more coins, the code will show up here")
    document.addEventListener('keydown', checkKey)
    intervalHandle = window.setInterval(updatePosition, 300)
#############################
# Main Program
#############################

def handleWin():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = f"WINNER, you collected {bag[1]} coins!\nNext level?"
    
def lockeddoor():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "The door was locked..., you need the key \n tryagain?"
    
def handlemonster():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "You got eaten\n try again?"
    
runGame()
