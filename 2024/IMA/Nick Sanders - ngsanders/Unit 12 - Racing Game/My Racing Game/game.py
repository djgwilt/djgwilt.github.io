#############################
# Library Imports
#############################
from js import document, window
from random import randint,shuffle as rand,shuf
#############################
# Global Variables
#############################
score=0
# to store current position (x,y)
position = [1, 1]
Red=[10,8]
Orange=[10,10]
Pink=[11,8]
Blue=[11,10]
GhostSpawn=shuf[10,20,30,40]


# to store movement directions (x,y)
direction = [0, 0]
interval = 300
intervalcount = 0
# to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 0

#############################
# Sub-Programs
#############################
carclass="carRight"
# the function called when a key is pressed - sets direction variable
direct="Right"
def checkKey(event):
    event.preventDefault()
    if event.key == "ArrowRight":
        direction[0]=1
        direction[1]=0
    elif event.key == "ArrowLeft":
        direction[0]=-1
        direction[1]=0
    elif event.key == "ArrowDown":
        direction[0]=0
        direction[1]=1
    elif event.key == "ArrowUp":
        direction[0]=0
        direction[1]=-1

def getCell(a):
    return document.getElementById(f"R{a[1]}C{a[0]}")

def wall(loc):
    if getCell(loc).classname=="wall" or  getCell(loc).classname=="gate":
        return True
    else:
        return False

def updateRed(a):
    rcell=getCell(Red)
    rcell.className=""
    if interval==a:
        if "car" in getCell([9,8]).cellName:
            Red=[9,9]
        else:
            Red=[9,8]
    elif interval > a:
        xdif=position[1]-Red[1]
        ydif=position[0]-Red[0]
        Right=getCell([Red[0]+1],Red[1])
        Left=getCell([Red[0]-1],Red[1])
        Down=getCell([Red[0]],Red[1]+1)
        Up=getCell([Red[0]],Red[1]-1)
        next=False
        if abs(xdif)>=abs(ydif):
            rightleft(xdif,ydif,Up,Down,Left,Right,False,False,False,False)
        else:
            updown(xdif,ydif,Up,Down,Left,Right,False,False,False,False)
            
def updown(xdif,ydif,Up,Down,Left,Right,alright,alup,alleft,aldown):
    if ydif<0 and alup==True or aldown==True:
        if wall(Up):
            alup=True
            rightleft(xdif,ydif,Up,Down,Left,Right,alright,alup,alleft,aldown)
        else:
            getCell(Up).className=getCell(Up).className and "red"
    else:
        if wall(Down):
            aldown=True
            rightleft(xdif,ydif,Up,Down,Left,Right,alright,alup,alleft,aldown)
        else:
            getCell(Down).className=getCell(Down).className and "red"

def rightleft(xdif,ydif,Up,Down,Left,Right,alright,alup,alleft,aldown):
    if xdif<0 and alright==False or alleft==True:
        if wall(Right):
            alright=True
            updown(xdif,ydif,Up,Down,Left,Right,alright,alup,alleft,aldown)
        else:
            getCell(Right).className=getCell(Right).className and "red"
    else:
        if wall(Left):
            alleft=True
            updown(xdif,ydif,Up,Down,Left,Right,alright,alup,alleft,aldown)
        else:
            getCell(Left).className=getCell(Left).className and "red"


# the timer check function - runs every 300 milliseconds to update the car position
def updatePosition():
    global intervalcount
    global GhostSpawn
    if intervalcount<=GhostSpawn[0]:
        updateRed(GhostSpawn[0])
    global score
    global direct
    if direction==[0,1]:
        direct="Down"
    elif direction==[0,-1]:  
        direct="Up"
    elif direction==[1,0]:
        direct="Right"
    elif direction==[-1,0]:
        direct="Left"
    carclass=f"car{direct}"
    if direction[0] != 0 or direction[1] !=0:
        # Set the cell where the car was to empty
        cell = getCell(position) #get location
        cell.className = "" #wipe location
        
        # Update the column position for the car
        position[0] += direction[0]
        # Update the row postion for the car
        position[1] += direction[1]
        if position[0]==-1:position[0]=18
        if position[0]==19:position[0]=0

        # Re-draw the car (or report a crash)
        cell = getCell(position)
        if cell == None: #No cell there
            handleCrash()
        elif cell.className=="dot":
            score+=1
            out(score)
        elif cell.className=="gate":
            handleCrash()
        elif cell.className=="wall":
            position[0] -= direction[0]
            position[1] -= direction[1]
            direction[0] *= -1
            direction[1] *= -1
            cell=getCell(position)
        cell.className = f"{carclass}"
        

def out(a):
    document.getElementById("Message").innerText = a


# if the car has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Oops you crashed..."

# called when the page is loaded to start the timer checks
def runGame():
    global intervalHandle, interval
    print("Running Game")
    document.addEventListener('keydown', checkKey)
    intervalHandle = window.setInterval(updatePosition, interval)

#############################
# Main Program
#############################

runGame()
