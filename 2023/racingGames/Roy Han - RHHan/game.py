#############################
# Library Imports
#############################
from js import document, window

import random

#############################
# Global Variables
#############################

# to store current position (x,y)
position = [0, 0]

bluePosition = [14, 14]
orangePosition = [16, 14]
pinkPosition = [14, 16]
redPosition = [16, 16]

# to store movement directions (x,y)
direction = [0, 0]

blueDirection = [0, 0]
orangeDirection = [0, 0]
pinkDirection = [0, 0]
redDirection = [0, 0]

# to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 0

blueHandle = 0
orangeHandle = 0
pinkHandle = 0
redHandle = 0

# past cells
bluePastCell = ["", ""]
blueCount = 0

orangePastCell = ["", ""]
orangeCount = 0

pinkPastCell = ["", ""]
pinkCount = 0

redPastCell = ["", ""]
redCount = 0


# contact sprites
spriteBlock = ["blueR", "blueL", "blueD", "blueU", 
               "orangeR", "orangeL", "orangeD", "orangeU", 
               "pinkR", "pinkL", "pinkD", "pinkU", 
               "redR", "redL", "redD", "redU"]
ghostBlock = ["spriteR", "spriteL", "spriteD", "spriteU"]
blueBlock = ["orangeR", "orangeL", "orangeD", "orangeU", 
             "pinkR", "pinkL", "pinkD", "pinkU", 
             "redR", "redL", "redD", "redU"]
orangeBlock = ["blueR", "blueL", "blueD", "blueU", 
               "pinkR", "pinkL", "pinkD", "pinkU", 
               "redR", "redL", "redD", "redU"]
pinkBlock = ["blueR", "blueL", "blueD", "blueU", 
               "orangeR", "orangeL", "orangeD", "orangeU", 
               "redR", "redL", "redD", "redU"]
redBlock = ["blueR", "blueL", "blueD", "blueU", 
               "orangeR", "orangeL", "orangeD", "orangeU", 
               "pinkR", "pinkL", "pinkD", "pinkU"]


# stores coins
coins = [603]

#############################
# Track
#############################

# track dictionary
trackDct = {
    0: "coin",
    1: "wall",
    2: "spriteR",
    3: "empty",
    4: "blueR",
    5: "orangeR",
    6: "pinkR",
    7: "redR"
}

# track map
track = [
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0],
    [0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 4, 3, 5, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 3, 3, 3, 3, 3, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0],
    [0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 6, 3, 7, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0],
    [0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0],
    [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]


#############################
# Sub-Programs
#############################

# load track
def loadTrack():
    lst = [[trackDct[e] for e in track[idx]] for idx in range(len(track))]

    tableInnerHTML = ""
    for row in range(len(lst)):
        tableInnerHTML += "<tr>"
        for col in range(len(lst[0])):
            tableInnerHTML += "<td id='R{}C{}' class='{}'></td>".format(row, col, lst[row][col])
        tableInnerHTML += "</tr>"
    document.getElementById("RacingTrack").innerHTML = tableInnerHTML

# the function called when a key is pressed - sets direction variable
def checkKey(event):
    event.preventDefault()
    if event.key == "ArrowRight":
        direction[0] = 1
        direction[1] = 0
    elif event.key == "ArrowLeft":
        direction[0] = -1
        direction[1] = 0
    elif event.key == "ArrowUp":
        direction[0] = 0
        direction[1] = -1
    elif event.key == "ArrowDown":
        direction[0] = 0
        direction[1] = 1    


def getCell(objectPosition):
    return document.getElementById("R{}C{}".format(objectPosition[1], objectPosition[0]))


# the timer check function - runs every 300 milliseconds to update the car position
def updatePosition():
    if direction[0] != 0 or direction[1] != 0:
        # Set the cell where the car was to empty
        originalCell = getCell(position)
        currClass = originalCell.className
        
        if direction[0] > 0:
            currClass = "spriteR"
        elif direction[0] < 0:
            currClass = "spriteL"
        elif direction[1] > 0:
            currClass = "spriteD"
        elif direction[1] < 0:
            currClass = "spriteU"

        # Update the column position for the car
        position[0] += direction[0]
        position[1] += direction[1]

        newCell = getCell(position)

        # stop at walls
        if newCell == None: 
            position[0] -= direction[0]
            position[1] -= direction[1]
            
            if direction[0] > 0:
                currClass = "spriteR"
            elif direction[0] < 0:
                currClass = "spriteL"
            elif direction[1] > 0:
                currClass = "spriteD"
            elif direction[1] < 0:
                currClass = "spriteU"
            originalCell.className = currClass

        elif newCell.className == "wall":
            position[0] -= direction[0]
            position[1] -= direction[1]

            if direction[0] > 0:
                currClass = "spriteR"
            elif direction[0] < 0:
                currClass = "spriteL"
            elif direction[1] > 0:
                currClass = "spriteD"
            elif direction[1] < 0:
                currClass = "spriteU"
            originalCell.className = currClass

        # coin counting
        elif newCell.className == "coin":
            newCell.className = currClass
            coins[0] -= 1
            if coins[0] == 0:
                handleWin()
            else:
                newCell.className = currClass
                originalCell.className = ""
        
        # crash with ghosts
        elif newCell.className in spriteBlock:
            originalCell.className = ""
            handleCrash()

        else:
            originalCell.className = ""
            newCell.className = currClass


# if the car has gone off the table, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    window.clearInterval(blueHandle)
    window.clearInterval(orangeHandle)
    window.clearInterval(pinkHandle)
    window.clearInterval(redHandle)

    document.getElementById("Message").innerText = "Game over"


# if the car touches the flag the user has won
def handleWin():
    window.clearInterval(intervalHandle)
    window.clearInterval(blueHandle)
    window.clearInterval(orangeHandle)
    window.clearInterval(pinkHandle)
    window.clearInterval(redHandle)

    document.getElementById("Message").innerText = "You win!"


# finds position from ghost to player
def findDelta(ghostPosition):
    delta = [0, 0]
    deltaSign = delta
    delta[0] = position[0] - ghostPosition[0]
    delta[1] = position[1] - ghostPosition[1]

    if delta[0] == 0:
        deltaSign[0] = 0
    elif delta[0] > 0:
        deltaSign[0] = 1
    else:
        delta[0] = -1
    
    if delta[1] == 0:
        deltaSign[1] = 0
    elif delta[1] > 0:
        deltaSign[1] = 1
    else:
        delta[1] = -1

    return delta, deltaSign


#############################
# Blue Sub-Programs
#############################

def blueClass():
    if blueDirection[0] > 0:
        currClass = "blueR"
    elif blueDirection[0] < 0:
        currClass = "blueL"
    elif blueDirection[1] > 0:
        currClass = "blueD"
    elif blueDirection[1] < 0:
        currClass = "blueU"
    else:
        currClass = blueRandom()
    return currClass
    

def blueCompare(originalCell, currClass):
    global blueCount

    bluePosition[0] += blueDirection[0]
    bluePosition[1] += blueDirection[1]

    newCell = getCell(bluePosition)
    returnVal = 0

    if newCell == None: 
        bluePosition[0] -= blueDirection[0]
        bluePosition[1] -= blueDirection[1]
        originalCell.className = blueClass()
        returnVal = 1
        return returnVal

    elif newCell.className == "wall":
        bluePosition[0] -= blueDirection[0]
        bluePosition[1] -= blueDirection[1]
        originalCell.className = blueClass()
        returnVal = 1
        return returnVal
    
    elif newCell.className in blueBlock:
        bluePosition[0] -= blueDirection[0]
        bluePosition[1] -= blueDirection[1]
        originalCell.className = blueClass()
        returnVal = 1
        return returnVal

    elif newCell.className in ghostBlock:
        if (blueCount % 2) == 0:
            originalCell.className = bluePastCell[1]
        else:
            originalCell.className = bluePastCell[0]  
        newCell.className = currClass
        handleCrash()
    
    else:
        if newCell.className not in spriteBlock:
            if (blueCount % 2) == 0:
                bluePastCell[0] = newCell.className
            else:
                bluePastCell[1] = newCell.className 
                
            if (blueCount % 2) == 0:
                originalCell.className = bluePastCell[1]
            else:
                originalCell.className = bluePastCell[0]
            blueCount += 1
            
        newCell.className = currClass
        return returnVal 
    

def blueRandom():
    num = random.randint(0, 3)
    if num  == 0:
        blueDirection[0] = -1
        blueDirection[1] = 0
        currClass = "blueL"
    elif num == 1:
        blueDirection[0] = 1
        blueDirection[1] = 0
        currClass = "blueR"
    elif num == 2: 
        blueDirection[0] = 0
        blueDirection[1] = -1
        currClass = "blueU"
    else:
        blueDirection[0] = 0
        blueDirection[1] = 1
        currClass = "blueD"
    return currClass


def updateBlue():   
    originalCell = getCell(bluePosition)
    currClass = originalCell.className

    delta, deltaSign = findDelta(bluePosition)

    if abs(delta[0]) >= abs(delta[1]):
        blueDirection[0] = deltaSign[0]
        blueDirection[1] = 0
        currClass = blueClass()
        val = blueCompare(originalCell, currClass)

        if val == 1:
            blueDirection[0] = 0
            blueDirection[1] = deltaSign[1]
            currClass = blueClass()
            val = blueCompare(originalCell, currClass)

            if val == 1:
                currClass = blueRandom()
                blueCompare(originalCell, currClass)
    
    else:
        blueDirection[0] = 0
        blueDirection[1] = deltaSign[1]
        currClass = blueClass()
        val = blueCompare(originalCell, currClass)

        if val == 1:
            blueDirection[0] = deltaSign[0]
            blueDirection[1] = 0
            currClass = blueClass()
            val = blueCompare(originalCell, currClass)

            if val == 1:
                currClass = blueRandom()
                blueCompare(originalCell, currClass)


#############################
# orange Sub-Programs
#############################

def orangeClass():
    if orangeDirection[0] > 0:
        currClass = "orangeR"
    elif orangeDirection[0] < 0:
        currClass = "orangeL"
    elif orangeDirection[1] > 0:
        currClass = "orangeD"
    elif orangeDirection[1] < 0:
        currClass = "orangeU"
    else:
        currClass = orangeRandom()
    return currClass
    

def orangeCompare(originalCell, currClass):
    global orangeCount

    orangePosition[0] += orangeDirection[0]
    orangePosition[1] += orangeDirection[1]

    newCell = getCell(orangePosition)
    returnVal = 0

    if newCell == None: 
        orangePosition[0] -= orangeDirection[0]
        orangePosition[1] -= orangeDirection[1]
        originalCell.className = orangeClass()
        returnVal = 1
        return returnVal

    elif newCell.className == "wall":
        orangePosition[0] -= orangeDirection[0]
        orangePosition[1] -= orangeDirection[1]
        originalCell.className = orangeClass()
        returnVal = 1
        return returnVal
    
    elif newCell.className in orangeBlock:
        orangePosition[0] -= orangeDirection[0]
        orangePosition[1] -= orangeDirection[1]
        originalCell.className = orangeClass()
        returnVal = 1
        return returnVal

    elif newCell.className in ghostBlock:
        if (orangeCount % 2) == 0:
            originalCell.className = orangePastCell[1]
        else:
            originalCell.className = orangePastCell[0]  
        newCell.className = currClass
        handleCrash()
    
    else:
        if newCell.className not in spriteBlock:
            if (orangeCount % 2) == 0:
                orangePastCell[0] = newCell.className
            else:
                orangePastCell[1] = newCell.className 
                
            if (orangeCount % 2) == 0:
                originalCell.className = orangePastCell[1]
            else:
                originalCell.className = orangePastCell[0]
            orangeCount += 1
            
        newCell.className = currClass
        return returnVal 
    

def orangeRandom():
    num = random.randint(0, 3)
    if num  == 0:
        orangeDirection[0] = -1
        orangeDirection[1] = 0
        currClass = "orangeL"
    elif num == 1:
        orangeDirection[0] = 1
        orangeDirection[1] = 0
        currClass = "orangeR"
    elif num == 2: 
        orangeDirection[0] = 0
        orangeDirection[1] = -1
        currClass = "orangeU"
    else:
        orangeDirection[0] = 0
        orangeDirection[1] = 1
        currClass = "orangeD"
    return currClass


def updateOrange():   
    originalCell = getCell(orangePosition)
    currClass = originalCell.className

    delta, deltaSign = findDelta(orangePosition)

    if abs(delta[0]) >= abs(delta[1]):
        orangeDirection[0] = deltaSign[0]
        orangeDirection[1] = 0
        currClass = orangeClass()
        val = orangeCompare(originalCell, currClass)

        if val == 1:
            orangeDirection[0] = 0
            orangeDirection[1] = deltaSign[1]
            currClass = orangeClass()
            val = orangeCompare(originalCell, currClass)

            if val == 1:
                currClass = orangeRandom()
                orangeCompare(originalCell, currClass)
    
    else:
        orangeDirection[0] = 0
        orangeDirection[1] = deltaSign[1]
        currClass = orangeClass()
        val = orangeCompare(originalCell, currClass)

        if val == 1:
            orangeDirection[0] = deltaSign[0]
            orangeDirection[1] = 0
            currClass = orangeClass()
            val = orangeCompare(originalCell, currClass)

            if val == 1:
                currClass = orangeRandom()
                orangeCompare(originalCell, currClass)


#############################
# pink Sub-Programs
#############################

def pinkClass():
    if pinkDirection[0] > 0:
        currClass = "pinkR"
    elif pinkDirection[0] < 0:
        currClass = "pinkL"
    elif pinkDirection[1] > 0:
        currClass = "pinkD"
    elif pinkDirection[1] < 0:
        currClass = "pinkU"
    else:
        currClass = pinkRandom()
    return currClass
    

def pinkCompare(originalCell, currClass):
    global pinkCount

    pinkPosition[0] += pinkDirection[0]
    pinkPosition[1] += pinkDirection[1]

    newCell = getCell(pinkPosition)
    returnVal = 0

    if newCell == None: 
        pinkPosition[0] -= pinkDirection[0]
        pinkPosition[1] -= pinkDirection[1]
        originalCell.className = pinkClass()
        returnVal = 1
        return returnVal

    elif newCell.className == "wall":
        pinkPosition[0] -= pinkDirection[0]
        pinkPosition[1] -= pinkDirection[1]
        originalCell.className = pinkClass()
        returnVal = 1
        return returnVal
    
    elif newCell.className in pinkBlock:
        pinkPosition[0] -= pinkDirection[0]
        pinkPosition[1] -= pinkDirection[1]
        originalCell.className = pinkClass()
        returnVal = 1
        return returnVal

    elif newCell.className in ghostBlock:
        if (pinkCount % 2) == 0:
            originalCell.className = pinkPastCell[1]
        else:
            originalCell.className = pinkPastCell[0]  
        newCell.className = currClass
        handleCrash()
    
    else:
        if newCell.className not in spriteBlock:
            if (pinkCount % 2) == 0:
                pinkPastCell[0] = newCell.className
            else:
                pinkPastCell[1] = newCell.className 
                
            if (pinkCount % 2) == 0:
                originalCell.className = pinkPastCell[1]
            else:
                originalCell.className = pinkPastCell[0]
            pinkCount += 1
            
        newCell.className = currClass
        return returnVal 
    

def pinkRandom():
    num = random.randint(0, 3)
    if num  == 0:
        pinkDirection[0] = -1
        pinkDirection[1] = 0
        currClass = "pinkL"
    elif num == 1:
        pinkDirection[0] = 1
        pinkDirection[1] = 0
        currClass = "pinkR"
    elif num == 2: 
        pinkDirection[0] = 0
        pinkDirection[1] = -1
        currClass = "pinkU"
    else:
        pinkDirection[0] = 0
        pinkDirection[1] = 1
        currClass = "pinkD"
    return currClass


def updatePink():   
    originalCell = getCell(pinkPosition)
    currClass = originalCell.className

    delta, deltaSign = findDelta(pinkPosition)

    if abs(delta[0]) >= abs(delta[1]):
        pinkDirection[0] = deltaSign[0]
        pinkDirection[1] = 0
        currClass = pinkClass()
        val = pinkCompare(originalCell, currClass)

        if val == 1:
            pinkDirection[0] = 0
            pinkDirection[1] = deltaSign[1]
            currClass = pinkClass()
            val = pinkCompare(originalCell, currClass)

            if val == 1:
                currClass = pinkRandom()
                pinkCompare(originalCell, currClass)
    
    else:
        pinkDirection[0] = 0
        pinkDirection[1] = deltaSign[1]
        currClass = pinkClass()
        val = pinkCompare(originalCell, currClass)

        if val == 1:
            pinkDirection[0] = deltaSign[0]
            pinkDirection[1] = 0
            currClass = pinkClass()
            val = pinkCompare(originalCell, currClass)

            if val == 1:
                currClass = pinkRandom()
                pinkCompare(originalCell, currClass)


#############################
# red Sub-Programs
#############################

def redClass():
    if redDirection[0] > 0:
        currClass = "redR"
    elif redDirection[0] < 0:
        currClass = "redL"
    elif redDirection[1] > 0:
        currClass = "redD"
    elif redDirection[1] < 0:
        currClass = "redU"
    else:
        currClass = redRandom()
    return currClass
    

def redCompare(originalCell, currClass):
    global redCount

    redPosition[0] += redDirection[0]
    redPosition[1] += redDirection[1]

    newCell = getCell(redPosition)
    returnVal = 0

    if newCell == None: 
        redPosition[0] -= redDirection[0]
        redPosition[1] -= redDirection[1]
        originalCell.className = redClass()
        returnVal = 1
        return returnVal

    elif newCell.className == "wall":
        redPosition[0] -= redDirection[0]
        redPosition[1] -= redDirection[1]
        originalCell.className = redClass()
        returnVal = 1
        return returnVal
    
    elif newCell.className in redBlock:
        redPosition[0] -= redDirection[0]
        redPosition[1] -= redDirection[1]
        originalCell.className = redClass()
        returnVal = 1
        return returnVal

    elif newCell.className in ghostBlock:
        if (redCount % 2) == 0:
            originalCell.className = redPastCell[1]
        else:
            originalCell.className = redPastCell[0]  
        newCell.className = currClass
        handleCrash()
    
    else:
        if newCell.className not in spriteBlock:
            if (redCount % 2) == 0:
                redPastCell[0] = newCell.className
            else:
                redPastCell[1] = newCell.className 
                
            if (redCount % 2) == 0:
                originalCell.className = redPastCell[1]
            else:
                originalCell.className = redPastCell[0]
            redCount += 1
            
        newCell.className = currClass
        return returnVal 
    

def redRandom():
    num = random.randint(0, 3)
    if num  == 0:
        redDirection[0] = -1
        redDirection[1] = 0
        currClass = "redL"
    elif num == 1:
        redDirection[0] = 1
        redDirection[1] = 0
        currClass = "redR"
    elif num == 2: 
        redDirection[0] = 0
        redDirection[1] = -1
        currClass = "redU"
    else:
        redDirection[0] = 0
        redDirection[1] = 1
        currClass = "redD"
    return currClass


def updateRed():   
    originalCell = getCell(redPosition)
    currClass = originalCell.className

    delta, deltaSign = findDelta(redPosition)

    if abs(delta[0]) >= abs(delta[1]):
        redDirection[0] = deltaSign[0]
        redDirection[1] = 0
        currClass = redClass()
        val = redCompare(originalCell, currClass)

        if val == 1:
            redDirection[0] = 0
            redDirection[1] = deltaSign[1]
            currClass = redClass()
            val = redCompare(originalCell, currClass)

            if val == 1:
                currClass = redRandom()
                redCompare(originalCell, currClass)
    
    else:
        redDirection[0] = 0
        redDirection[1] = deltaSign[1]
        currClass = redClass()
        val = redCompare(originalCell, currClass)

        if val == 1:
            redDirection[0] = deltaSign[0]
            redDirection[1] = 0
            currClass = redClass()
            val = redCompare(originalCell, currClass)

            if val == 1:
                currClass = redRandom()
                redCompare(originalCell, currClass)


# called when the page is loaded to start the timer checks
def runGame():
    global intervalHandle
    global blueHandle
    global orangeHandle
    global pinkHandle
    global redHandle
    print("Running Game")
    document.addEventListener('keydown', checkKey)
    intervalHandle = window.setInterval(updatePosition, 150)
    
    # ghosts
    blueHandle = window.setInterval(updateBlue, 400)
    orangeHandle = window.setInterval(updateOrange, 400)
    pinkHandle = window.setInterval(updatePink, 400)
    redHandle = window.setInterval(updateRed, 400)

#############################
# Main Program
#############################
loadTrack()

runGame()
