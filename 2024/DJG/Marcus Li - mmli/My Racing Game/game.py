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
coincount = []
bag = []
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

def getCell():
    return document.getElementById("R{}C{}".format(position[1], position[0]))
# the timer check function - runs every 300 milliseconds to update player2's position
def updatePosition():
    if direction[0] != 0 or direction[1] != 0:
        # Set the cell where player2 was to empty
        cell = getCell()
        cell.className = ""
        # Update the column position for player2
        position[0] += direction[0]
        position[1] += direction[1]
        cell = getCell()
        if cell == None:
            handleCrash()
        elif cell.className == "coin":
            cell.className = "player1"
            coincount.append(1)
            document.getElementById("Message").innerText = "You collected a piece of coral!"
        elif cell.className == "orangekey":
            bag.append("an orange key")
            cell.className = "player1"
            document.getElementById("Message").innerText = "You collected an orange key!"
        elif cell.className == "yellowkey":
            bag.append("a yellow key")
            cell.className = "player1"
            document.getElementById("Message").innerText = "You collected a yellow key!"
        elif cell.className == "greenkey":
            bag.append("a green key")
            cell.className = "player1"
            document.getElementById("Message").innerText = "You collected a green key!"
        elif cell.className == "bluekey":
            bag.append("a blue key")
            cell.className = "player1"
            document.getElementById("Message").innerText = "You collected a blue key!"
        elif cell.className == "orangekeydoor":
            if "an orange key" in bag:
                bag.remove("an orange key")
                cell.className = "player1"
                document.getElementById("Message").innerText = "You used your orange key to open the orange door!"
            else:
                position[0] -= direction[0]
                position[1] -= direction[1]
                cell = getCell()
                cell.className = "player1"
                document.getElementById("Message").innerText = "Hmm... You don't have the right key to get through this door."
        elif cell.className == "yellowkeydoor":
            if "a yellow key" in bag:
                bag.remove("a yellow key")
                cell.className = "player1"
                document.getElementById("Message").innerText = "You used your yellow key to open the yellow door!"
            else:
                position[0] -= direction[0]
                position[1] -= direction[1]
                cell = getCell()
                cell.className = "player1"
                document.getElementById("Message").innerText = "Hmm... You don't have the right key to get through this door."
        elif cell.className == "greenkeydoor":
            if "a green key" in bag:
                bag.remove("a green key")
                cell.className = "player1"
                document.getElementById("Message").innerText = "You used your green key to open the green door!"
            else:
                position[0] -= direction[0]
                position[1] -= direction[1]
                cell = getCell()
                cell.className = "player1"
                document.getElementById("Message").innerText = "Hmm... You don't have the right key to get through this door."
        elif cell.className == "bluekeydoor":
            if "a blue key" in bag:
                bag.remove("a blue key")
                cell.className = "player1"
                document.getElementById("Message").innerText = "You used your blue key to open the blue door!"
            else:
                position[0] -= direction[0]
                position[1] -= direction[1]
                cell = getCell()
                cell.className = "player1"
                document.getElementById("Message").innerText = "Hmm... You don't have the right key to get through this door."
        elif cell.className == "wall":
            crashwall()
        elif cell.className == "flag":
            cell.className = "player1"
            win()
        elif cell.className == "":
            if len(bag) == 0:
                document.getElementById("Message").innerText = "You have no items"
            elif len(bag) == 1:
                document.getElementById("Message").innerText = "You have {}".format(bag[0])
            elif len(bag) == 2:
                document.getElementById("Message").innerText = "You have {} and {}".format(bag[0],bag[1])
            elif len(bag) == 3:
                document.getElementById("Message").innerText = "You have {}, {} and {}".format(bag[0],bag[1],bag[2])
            elif len(bag) == 4:
                document.getElementById("Message").innerText = "You have {}, {}, {} and {}".format(bag[0],bag[1],bag[2],bag[3])
            cell.className = "player1"
        direction[0] = 0
        direction[1] = 0
        # Re-draw player1 (or report a crash)

# if player2 has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Oh no your fish swam away... Thanks for playing! Refresh the page to play again."

def win():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Congratulations! You got your fish back to its coral reef home! You collected {} pieces of coral! Thanks for playing! Refresh the page to play again.".format(sum(coincount))

def crashwall():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Oh no your fish crashed into a shipwreck... Thanks for playing! Refresh the page to play again."


# called when the page is loaded to start the timer checks
def runGame():
    global intervalHandle
    templist = ["player2","","","","wall","coin","","wall","","","","","","","","","","","","","","","","","","","","","","","wall","wall","wall","","wall","wall","yellowkeydoor","wall","","wall","wall","wall","wall","wall","wall","wall","wall","wall","","wall","","wall","wall","wall","wall","wall","wall","wall","wall","","coin","orangekeydoor","","","","","orangekey","wall","","wall","","","","","","","","wall","","wall","","wall","","","","wall","bluekey","coin","wall","","wall","","wall","wall","wall","wall","wall","coin","","wall","","wall","wall","wall","wall","wall","","wall","","wall","","wall","","wall","","","","wall","wall","","wall","","wall","","","","","wall","","wall","","wall","","","","wall","","wall","","wall","","wall","","wall","wall","wall","wall","wall","wall","","","","wall","","wall","wall","","wall","","wall","","wall","","wall","","wall","","wall","","wall","","wall","","","","","","","","","","wall","wall","","","wall","","wall","","wall","","wall","","wall","","wall","","wall","","wall","","wall","wall","wall","wall","wall","wall","wall","wall","wall","","wall","","wall","","wall","","wall","","wall","","wall","coin","wall","","wall","","wall","greenkeydoor","wall","","","","","","","","","","coin","","","","","","wall","","wall","","wall","","","","wall","","wall","","wall","","","wall","wall","wall","wall","wall","wall","wall","wall","wall","wall","wall","wall","wall","wall","wall","wall","","wall","","wall","wall","wall","wall","wall","","wall","","wall","","wall","","","","","","","","","","","","","","","","","","wall","","","","","","","","wall","","wall","","wall","","wall","","wall","wall","wall","wall","wall","wall","","wall","","wall","wall","coin","wall","wall","greenkey","wall","wall","wall","wall","wall","wall","wall","wall","","wall","bluekeydoor","","","wall","","wall","","","","","","","","","wall","","wall","","","","","","","","","","","","","wall","wall","coin","wall","wall","","wall","","wall","wall","wall","wall","wall","wall","","","","","","wall","wall","wall","wall","wall","wall","wall","wall","wall","wall","wall","","wall","wall","","wall","","wall","","","","","","","wall","","wall","wall","wall","","wall","coin","","","","","","","","","","","","","","","","wall","coin","wall","yellowkey","wall","wall","flag",]
    number = 0
    for firstnumber in range(15):
        tempposition = [firstnumber, 0]
        for secondnumber in range(30):
            tempposition[1] = secondnumber
            tempcell = document.getElementById("R{}C{}".format(tempposition[0], tempposition[1]))
            tempcell.className = templist[number]
            number += 1
    print("Go!")
    document.addEventListener('keydown', create_proxy(checkKey))
    intervalHandle = window.setInterval(create_proxy(updatePosition), 0)

#############################
# Main Program
#############################
runGame()