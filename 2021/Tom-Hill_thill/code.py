#############################
# Library Imports           #
#############################
from js import document, window, jQuery, Object
import random

#############################
# Global Variables          #
#############################
carDirection = "right"
# to store movement direction
xDir = 0
yDir = 0
speed = 300
# to store current column position
column = 0
row = 0
# to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 0
speed = 300
#############################
# Checkpoint Locations
#############################
crow1 = random.randint(0,19)
ccolumn1 = random.randint(0,19)

wallrow1 = random.randint(0,19)
wallcolumn1 = random.randint(0,19)
points = 0
#############################
# Sub-Programs
#############################




# the function called when a key is pressed - sets direction variable
def checkKey(event):
    global xDir
    global yDir
    global carDirection
    global speed
    global intervalHandle
    if event.keyCode == 32:
        #brake
        xDir = 0
        yDir = 0
    elif event.keyCode == 87:
        speed = speed / 1.1
        window.clearInterval(intervalHandle)
        intervalHandle = window.setInterval(updatePosition, speed)
    elif event.keyCode == 39:
        # right arrow
        xDir = 1
        yDir = 0
        carDirection = "right"
    elif event.keyCode == 37:
        # left arrow
        xDir = -1
        yDir = 0
        carDirection = "left"
    elif event.keyCode == 40:
        # up arrow
        xDir = 0
        yDir = 1
        carDirection = "up"
    elif event.keyCode == 38:
        # down arrow
        xDir = 0
        yDir = -1
        carDirection = "down"
    event.preventDefault()
        
def getCell():
    return document.getElementById(f"R{row}C{column}")

def checkpointcell():
    return document.getElementById(f"R{crow}C{ccolumn}")
# the timer check function - runs every 300 milliseconds to update the car position

    
def updatePosition():
    global column
    global row
    global jQuery
    global Object
    global points
    global speed
    global intervalHandle
    if xDir != 0 or yDir != 0:
        
        # Set the cell where the car was to empty
        cell = getCell()
        cell.className = "Empty"
        # Update the column position for the car
        column += xDir
        row += yDir
        # Re-draw the car (or report a crash)
        cell = getCell()
        if not cell:
            handleCrash()
        elif cell.className == "wall":
            handleCrash()
        elif cell.className == "invisible_wall":
            handleCrash()
        elif cell.className == "checkpoint":
            car = document.getElementById("car")
            points = points + (1000 // speed)
            crow1 = random.randint(0,19)
            ccolumn1 = random.randint(0,19)
            nextcheckpoint = document.getElementById(f"R{crow1}C{ccolumn1}")
            nextcheckpoint.className = "checkpoint"
            wallrow1 = random.randint(0,19)
            wallcolumn1 = random.randint(0,19)
            nextwall = document.getElementById(f"R{wallrow1}C{wallcolumn1}")
            nextwall.className = "wall"
            speed = speed / 1.1
            print(f"you have {points}pts")
            window.clearInterval(intervalHandle)
            intervalHandle = window.setInterval(updatePosition, speed)
            jQuery(car).stop()
            jQuery(car).animate(Object(top=f"{row*21*12/11+55}px", left=f"{column*21*12/11+14}px"),speed,"linear")

        elif cell.className == "flag":
            handleWin()
        elif cell:
            car = document.getElementById("car")
            jQuery(car).stop()
            jQuery(car).animate(Object(top=f"{row*21*12/11+55}px", left=f"{column*21*12/11+14}px"),speed,"linear")
            if carDirection == "right":
                car.className = "Car_right car"
            elif carDirection == "left":
                car.className = "Car_left car"
            elif carDirection == "up":
                car.className = "Car_up car"
            elif carDirection == "down":
                car.className = "Car_down car"
#jQuery(car).animate(Object(top=f"{row*21*12/11+55}px"),200)
#jQuery(car).animate(Object(left=f"{column*21*12/11+14}px"),200)           

# if the car has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = f"Oops you crashed... with a total of {points}pts"

# called when the page is loaded to start the timer checks
def runGame():
    global intervalHandle
    print("Running Game")
    document.addEventListener('keydown', checkKey)
    intervalHandle = window.setInterval(updatePosition, speed)
    document.getElementById("car").style.top = "55px"
    document.getElementById("car").style.left = "14px"
    

def handleWin():
        window.clearInterval(intervalHandle)
        document.getElementById("Message").innerText = "Noice you winn"
#############################
# Main Program
#############################

runGame()
