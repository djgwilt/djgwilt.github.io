##############################
# Library Imports
#############################
from js import document, window # type: ignore

#############################
# Global Variables
#############################

# to store current position (x,y)
position = [0, 0]

# to store movement directions (x,y)
direction = [0, 0]

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
    elif event.key == "ArrowUp":
        # up arrow
        direction[0] = 0
        direction[1] = -1
    elif event.key == "ArrowDown":
        # down arrow
        direction[0] = 0
        direction[1] = 1

def getCell():
    return document.getElementById("R{}C{}".format(position[1], position[0]))

# the timer check function - runs every 300 milliseconds to update the car position
# the timer check function - runs every 300 milliseconds to update the car position
def updatePosition():
    if direction[0] != 0 or direction[1] != 0:
        # Set the cell where player1 was to empty
        cell = getCell()
        cell.className = ""
        
        # Update the column and row positions for player1
        position[0] += direction[0]
        position[1] += direction[1]
        cell = getCell()

        if cell is None:
            handleCrash()
        elif cell.className == "wall":
            handleCrash()
        elif cell.className == "flag":
            handleWin()
        else:
            cell.className = "car" 
       

def handleWin(): 
    window.clearlnterval(intervalHandle) 
    document.getE1ementById( "Message" ).innerText = "You Win" 
        
def resetGame():
    # Define the variables
    global position, direction, num_rows, num_cols, flag_position

    # Reset the player's position
    position[0] = 0
    position[1] = 0

    # Reset the direction
    direction[0] = 0
    direction[1] = 0

    # Reset the cell classes
    for row in range(num_rows):
        for col in range(num_cols):
            cell = document.getElementById(f"R{row}C{col}")
            if cell.className == "car":
                cell.className = ""
            elif cell.className == "flag":
                continue
            else:
                cell.className = "road"

    # Redraw the car and flag
    car_cell = getCell()
    car_cell.className = "car"

    flag_cell = document.getElementById(f"R{flag_position[1]}C{flag_position[0]}")
    flag_cell.className = "flag"

# you are moving
# if the car has gone off the table, this tidies up including crash message

def handleCrash():
        window.clearInterval(intervalHandle)
        document.getElementById("Message").innerText = "Oops you crashed..."
def runGame():
    global intervalHandle
    print("Running Game")
    document.addEventListener('keydown', checkKey)
    intervalHandle = window.setInterval(updatePosition, 300)

# called when the page is loaded to start the timer checks


#############################
# Main Program
#############################

runGame()