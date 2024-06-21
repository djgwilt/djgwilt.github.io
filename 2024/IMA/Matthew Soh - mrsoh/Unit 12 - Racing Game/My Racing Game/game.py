from js import document, window

position = [0, 0]

direction = [0,0]

intervalHandle = 0

def checkKey(event):
    global direction
    event.preventDefault()
    if event.key == "ArrowRight":
        direction = [0,1]
    elif event.key == "ArrowLeft":
        direction  = [0,-1]
    elif event.key == "ArrowDown":
        direction = [1,0]
    elif event.key == "ArrowUp":
        direction = [-1,0]
 
def getCell():
    return document.getElementById("R{}C{}".format(position[0],position[1]))

def updatePosition():
    global position
    cell = getCell()
    cell.className = ""
    print(position, direction)
    position[0] += direction[0]
    position[1] += direction[1]
    cell = getCell()
    if cell == None or cell.className == "wall":
        handleCrash()
    else:
        cell.className = "car"

def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Oops you crashed..."

def runGame():
    global intervalHandle
    print("Running Game")
    document.addEventListener('keydown', checkKey)
    intervalHandle = window.setInterval(updatePosition, 150)


runGame()
