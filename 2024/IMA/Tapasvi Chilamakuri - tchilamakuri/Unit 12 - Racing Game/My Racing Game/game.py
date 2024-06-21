from js import document, window

position1 = [3, 2]
position2 = [4, 2]  
direction1 = [0, 0]
direction2 = [0, 0]
intervalHandle1 = 0
intervalHandle2 = 0
defaultTime = 300
boostTime = 100
curbTime = 700
limitTime = 650
limitsTime = 3000

laps_completed1 = 0
laps_completed2 = 0
blockstraveled1 = 0
blockstraveled2 = 0
total_laps = 5

player1class = "player11"
player2class = "player21"

def checkKey(event):
    event.preventDefault()
    if event.key == "ArrowRight":
        direction1[0] = 1
        direction1[1] = 0
    elif event.key == "ArrowLeft":
        direction1[0] = -1
        direction1[1] = 0
    elif event.key == "ArrowUp":
        direction1[0] = 0
        direction1[1] = -1
    elif event.key == "ArrowDown":
        direction1[0] = 0
        direction1[1] = 1
    elif event.key == "d":
        direction2[0] = 1
        direction2[1] = 0
    elif event.key == "a":
        direction2[0] = -1
        direction2[1] = 0
    elif event.key == "w":
        direction2[0] = 0
        direction2[1] = -1
    elif event.key == "s":
        direction2[0] = 0
        direction2[1] = 1

def getCell1():
    return document.getElementById("R{}C{}".format(position1[1], position1[0]))

def getCell2():
    return document.getElementById("R{}C{}".format(position2[1], position2[0]))

def updatePosition1():
    global position1, direction1, player1class, laps_completed1, total_laps, blockstraveled1
    currentTime1 = defaultTime
    changeInterval1 = False

    if (position1 == [3, 1] or position1 == [4, 1] or position1 == [5, 1]) and (blockstraveled1 % 5 == 0):
        laps_completed1 += 1
        print(f"Player 1 completed {laps_completed1} laps.")
        if laps_completed1 == total_laps:
            end_game("Player 1")
            return

    oldsprite1 = player1class
    if direction1 == [0, 1]:
        player1class = "player11"
    elif direction1 == [0, -1]:
        player1class = "player12"
    elif direction1 == [1, 0]:
        player1class = "player13"
    elif direction1 == [-1, 0]:
        player1class = "player14"

    if position1 == [13, 0]:
        cell = getCell1()
        if cell:
            cell.classList.remove("player12")
        position1 = [3, 0]
        cell = getCell1()
        if cell:
            cell.classList.add("player11")
            cell.classList.remove("player11")
        direction1 = [0, 1]
        currentTime1 = defaultTime
        changeInterval1 = True
    elif position1 == [14, 0]:
        cell = getCell1()
        if cell:
            cell.classList.remove("player12")
        position1 = [4, 0]
        cell = getCell1()
        if cell:
            cell.classList.add("player11")
            cell.classList.remove("player11")
        direction1 = [0, 1]
        currentTime1 = defaultTime
        changeInterval1 = True
    elif position1 == [15, 0]:
        cell = getCell1()
        if cell:
            cell.classList.remove("player12")
        position1 = [5, 0]
        cell = getCell1()
        if cell:
            cell.classList.add("player11")
            cell.classList.remove("player11")
        direction1 = [0, 1]
        currentTime1 = defaultTime
        changeInterval1 = True
    else:
        cell = getCell1()
        if cell:
            cell.classList.remove(oldsprite1)
        position1[0] += direction1[0]
        position1[1] += direction1[1]
        cell = getCell1()
        if cell is None:
            handleCrash1()
        elif cell.classList.contains("curb"):
            currentTime1 = curbTime
            changeInterval1 = True
            cell.classList.add(player1class)
        elif cell.classList.contains("limit"):
            currentTime1 = limitTime
            changeInterval1 = True
            cell.classList.add(player1class)
        elif cell.classList.contains("limits"):
            currentTime1 = limitsTime
            changeInterval1 = True
            cell.classList.add(player1class)
        elif cell.classList.contains("boost"):
            currentTime1 = boostTime
            changeInterval1 = True
            cell.classList.add(player1class)
            blockstraveled1 =+ 1
        else:
            currentTime1 = defaultTime
            changeInterval1 = True
            cell.classList.add(player1class)

    if changeInterval1:
        updateInterval1(currentTime1)

def updatePosition2():
    global position2, direction2, player2class, laps_completed2, total_laps, blockstraveled2
    currentTime2 = defaultTime
    changeInterval2 = False

    if (position2 == [3, 1] or position2 == [4, 1] or position2 == [5, 1]) and (blockstraveled2 % 5 == 0):
        laps_completed2 += 1
        print(f"Player 2 completed {laps_completed2} laps.")
        if laps_completed2 == total_laps:
            end_game("Player 2")
            return

    oldsprite2 = player2class
    if direction2 == [0, 1]:
        player2class = "player21"
    elif direction2 == [0, -1]:
        player2class = "player22"
    elif direction2 == [1, 0]:
        player2class = "player23"
    elif direction2 == [-1, 0]:
        player2class = "player24"

    if position2 == [13, 0]:
        cell = getCell2()
        if cell:
            cell.classList.remove("player22")
        position2 = [3, 0]
        cell = getCell2()
        if cell:
            cell.classList.add("player21")
            cell.classList.remove("player21")
        direction2 = [0, 1]
        currentTime2 = defaultTime
        changeInterval2 = True
    elif position2 == [14, 0]:
        cell = getCell2()
        if cell:
            cell.classList.remove("player22")
        position2 = [4, 0]
        cell = getCell2()
        if cell:
            cell.classList.add("player21")
            cell.classList.remove("player21")
        direction2 = [0, 1]
        currentTime2 = defaultTime
        changeInterval2 = True
    elif position2 == [15, 0]:
        cell = getCell2()
        if cell:
            cell.classList.remove("player22")
        position2 = [5, 0]
        cell = getCell2()
        if cell:
            cell.classList.add("player21")
            cell.classList.remove("player21")
        direction2 = [0, 1]
        currentTime2 = defaultTime
        changeInterval2 = True
    else:
        cell = getCell2()
        if cell:
            cell.classList.remove(oldsprite2)
        position2[0] += direction2[0]
        position2[1] += direction2[1]
        cell = getCell2()
        if cell is None:
            handleCrash2()
        elif cell.classList.contains("curb"):
            currentTime2 = curbTime
            changeInterval2 = True
            cell.classList.add(player2class)
        elif cell.classList.contains("limit"):
            currentTime2 = limitTime
            changeInterval2 = True
            cell.classList.add(player2class)
        elif cell.classList.contains("limits"):
            currentTime2 = limitsTime
            changeInterval2 = True
            cell.classList.add(player2class)
        elif cell.classList.contains("boost"):
            currentTime2 = boostTime
            changeInterval2 = True
            cell.classList.add(player2class)
            blockstraveled2 =+ 1
        else:
            currentTime2 = defaultTime
            changeInterval2 = True
            cell.classList.add(player2class)


    if changeInterval2:
        updateInterval2(currentTime2)

def updateInterval1(newTime):
    global intervalHandle1
    window.clearInterval(intervalHandle1)
    intervalHandle1 = window.setInterval(updatePosition1, newTime)

def updateInterval2(newTime):
    global intervalHandle2
    window.clearInterval(intervalHandle2)
    intervalHandle2 = window.setInterval(updatePosition2, newTime)

def handleCrash1():
    global position1, direction1
    window.clearInterval(intervalHandle1)
    document.getElementById("Message").innerText = "Player 1 got injured"
    position1 = [3, 2]
    direction1 = [0, 1] 
    updatePosition1() 

def handleCrash2():
    global position2, direction2
    window.clearInterval(intervalHandle2)
    document.getElementById("Message").innerText = "Player 2 got injured"
    position2 = [4, 2] 
    direction2 = [0, 1] 
    updatePosition2()  

def end_game(winner):
    global intervalHandle1, intervalHandle2
    if intervalHandle1 != 0:
        window.clearInterval(intervalHandle1)
    if intervalHandle2 != 0:
        window.clearInterval(intervalHandle2)
    print(f"{winner} wins the game!")

def runGame():
    global intervalHandle1, intervalHandle2, defaultTime
    print("Running Game")
    document.addEventListener('keydown', checkKey)
    intervalHandle1 = window.setInterval(updatePosition1, defaultTime)
    intervalHandle2 = window.setInterval(updatePosition2, defaultTime)

runGame()