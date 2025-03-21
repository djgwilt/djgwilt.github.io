#############################
# Library Imports
#############################
from js import document, window

#############################
# Global Variables
#############################

# to store current position (x,y)
position = [0, 0]
position_meteor=[10,1]

# to store movement directions (x,y)
direction = [0, 0]
direction_meteor=[10,1]
# to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 0

#############################
# Sub-Programs
#############################



# the function called when a key is pressed - sets direction variable
def checkKey(event):
    event.preventDefault()
    if event.key == "ArrowRight":
        direction[0] = 1
        direction[1] = 0
        #direction_meteor[0] = 1
        #direction_meteor[1] = 0
    elif event.key == "ArrowLeft":
        # left arrow
        direction[0] = -1
        direction[1]=0
        #direction_meteor[0] = -1
        #direction_meteor[1] = 0
    elif event.key =="ArrowUp":
        direction[0]=0 
        direction[1]=-1
        #direction_meteor[0] = 0
        #direction_meteor[1] = -1
    elif event.key=="ArrowDown":
        direction[0]=0
        direction[1]=1
        #direction_meteor[0] = 0
        #direction_meteor[1] = 1
    

def getCell():
    return document.getElementById("R{}C{}".format(position[1],position[0]))
def getMeteor():
    return document.getElementById("R{}C{}".format(position_meteor[1],position_meteor[0]))


        #have to create sepearte crash for meteor


# the timer check function - runs every 300 milliseconds to update the car position
def updatePosition():
    if direction[0] != 0 or direction[1] !=0 or position_meteor[0] !=0 or direction_meteor[1] !=0:
        # Set the cell where the car was to empty
        cell = getCell()
        currClass=cell.className
        cell2=getCell()
        currClass2=cell2.className
        if direction[0]>0:
            currClass="rocket"
            #currClass="meteor"
        elif direction[0]<0:
            currClass="rocket_flipped"
            #currClass="meteor"
        elif direction[1]<0:
            currClass="rocket_up"
            #currClass2="meteor"
        elif direction[1]>0:
            currClass="rocket_down"
            #currClass2="meteor"
        cell.className=""
        meteor=getMeteor()
        # Update the column position for the car
        position[0] += direction[0]
        position[1] +=direction[1]
        meteor.className=""
        position_meteor[0] += direction[0]
        position_meteor[1] += direction[1]

        # Re-draw the car (or report a crash)
        meteor=getMeteor()
        if meteor==None:
            pass
        elif meteor.className=="wall":
            position_meteor[0]=100000
        else:
            meteor.className="meteor"
        
        cell = getCell()
        if cell == None:
            handleCrash()
        elif cell.className== "wall":
            handleCrash()
        elif cell.className=="planet":
            handleWin()
        elif cell.className=="meteor":
            handleCrash()
        else:
            cell.className = currClass
def handleWin():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText="You win"
# if the car has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Oops you crashed..."



# called when the page is loaded to start the timer checks
def runGame():
    global intervalHandle
    print("Running Game")
    document.addEventListener('keydown', checkKey)
    intervalHandle = window.setInterval(updatePosition, 300)

#############################
# Main Program
#############################

runGame()
