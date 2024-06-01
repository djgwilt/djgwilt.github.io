#############################
# Library Imports
#############################
from js import document, window, storageChange, checkStorage

#############################
# Global Variables
#############################

# to store movement direction
xDir = 0
yDir = 0

# to store current column position
column = 0
row = 0
upDown = 0
leftRight = 0

# to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 0

#############################
# Sub-Programs
#############################

# the function called when a key is pressed - sets direction variable
def checkKey(event):
    event.preventDefault()
    global xDir, yDir, leftRight, upDown
    if event.keyCode == 39:
        # right arrow
        xDir = 1
        yDir = 0
        leftRight = 0
        upDown = 2
    elif event.keyCode == 37:
        # left arrow
        xDir = -1
        yDir = 0
        leftRight = 1
        upDown = 2
#         document.getElementsByClassName('Car').style.transform = 'scaleX(-1)'
    elif event.keyCode == 38: # up
        print('up')
        yDir = -1
        xDir = 0
        leftRight = 2
        upDown = 0
    elif event.keyCode == 40: # down
        print('down')
        yDir = 1
        xDir = 0
        leftRight = 2
        upDown = 1


def getCell():
    # print(f"R{row}C{column}")
    return document.getElementById(f"R{row}C{column}")

# the timer check function - runs every 300 milliseconds to update the car position
def updatePosition():
    global column, row
    global xDir, yDir
    if (xDir != 0) or (yDir != 0):
        # Set the cell where the car was, to empty
        cell = getCell()
        cell.className = "Empty"
        
        # Update the column position for the car
        
        column += xDir
        row += yDir
        
        # print(f'column: {column}, row: {row}, x: {xDir}, y: {yDir}')
        
        # Re-draw the car (or report a crash)
        cell = getCell()
#         try:
#             print('current cell class:', cell.className)
#         except exception as e:
#             print(e)
        # print(f'current x: {xDir} current y: {yDir}')
        # print(f'current row: {row} current column: {column}')
        try: # trys don't work for some reason
            if cell and (cell.className not in ['wall', 'flag','portal','key','exit','door']):
                carDirec(cell)
            elif cell.className == 'wall':
                handleCrash()
            elif cell.className in ['flag','door']:
                print('on flag')
                onFlag()
                xDir = 0
                yDir = 0
            elif cell.className == 'portal':
                print('on portal')
                onPortal1()
            elif cell.className == 'key':
                print('on key')
                document.getElementById('keyStatus').innerHTML = '1'
                storageChange('1')
                carDirec(cell)
            elif cell.className == 'exit':
                print('on exit')
                onExit()
        except Exception as e:
            print(e)

def carDirec(cell):
    if leftRight == 1:
        cell.className = 'car-flipped'
    elif leftRight == 0:
        cell.className = "Car"
    elif upDown == 0:
        cell.className = 'carUp'
    elif upDown == 1:
        cell.className = 'carDown'

# if the car has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("message").innerText = "Oops you crashed..."

# called when the page is loaded to start the timer checks
def runGame():
    global xDir, yDir, column, row
    global intervalHandle
    # to store movement direction
    xDir = 0
    yDir = 0

    # to store current column position
    column = 0
    row = 0
    print("Running Game")
    document.addEventListener('keydown', checkKey)
    intervalHandle = window.setInterval(updatePosition, 400)




def reset(f):
    print('resetting...')    
    document.getElementsByClassName('Car').className = 'Empty'
    document.getElementById('R0C0').className = 'Car'
    document.getElementById("message").innerText = ""
    runGame()
document.getElementById("btn").addEventListener("click", reset)

def onFlag():
    currentUrl = window.location.pathname
    # document.getElementById('RacingTrack').className = 'hidden'
    # document.getElementById('RacingTrack2').className = 'active RacingTrack'
    
    # runGame()
    if currentUrl == '/level1.html':
        window.location.replace("./level2.html")
    elif currentUrl == '/level2.html':
        window.location.replace('./level3.html')
    elif currentUrl == '/level3.html':
        if document.getElementById('keyStatus').innerHTML == '1':
            window.location.replace("./level4.html")
        else:
            document.getElementById("message").innerText = "That door is locked..."


def onExit():
    currentUrl = window.location.pathname
    if currentUrl == '/hiddenroom.html':
        window.location.replace("./level3.html")

def onPortal1():
    print('HIDDEN ROOM!!!')
    document.getElementById("message").innerText = "YOU HAVE FOUND A HIDDEN ROOM!"
    window.location.replace('./hiddenroom.html')


# class MyClass(object):
#     def method(self):
#         pass

# print(runGame.__name__)


#############################
# Main Program
#############################

runGame()
