#############################
# Library Imports
#############################
from js import document, window, jQuery

#############################
# Global Variables
#############################

# to store current position (x,y)
position = [0, 0]

# to store movement directions (x,y)
direction = [0, 0]

# to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 0

immunities = []
coins = 0
moves = 0

audioWin = document.getElementById("audioWin")
audioCoin = document.getElementById("audioCoin")
audioCrash = document.getElementById("audioCrash")
audioMonsterCrash = document.getElementById("audioMonsterCrash")
audioPlayerCrash = document.getElementById("audioPlayerCrash")
audioImmunity = document.getElementById("audioImmunity")
audioMonster = document.getElementById("audioMonster")

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

# the timer check function - runs every 300 milliseconds to update the car position
def updatePosition():
    global moves
    moves += 1
    if direction[0] != 0 or direction[1] != 0:
        # Set the cell where the car was to empty
        cell = getCell()
        if cell.className == "car":
            cell.className = ""
        elif cell.className == "carandrmonster":
            cell.className = "rmonster"
        elif cell.className == "carandymonster":
            cell.className = "ymonster"
        elif cell.className == "carandgmonster":
            cell.className = "gmonster"
        elif cell.className == "carandcmonster":
            cell.className = "cmonster"
        elif cell.className == "carandbmonster":
            cell.className = "bmonster"
        elif cell.className == "carandmmonster":
            cell.className = "mmonster"
        elif cell.className == "carandomonster":
            cell.className = "omonster"
        elif cell.className == "caranddgmonster":
            cell.className = "dgmonster"
        elif cell.className == "carandpmonster":
            cell.className = "pmonster"
        elif cell.className == "carandflag":
            cell.className = "flag"

        # Update the column position for the car
        position[0] += direction[0]
        position[1] += direction[1]

        # Re-draw the car (or report a crash)
        global coins
        cell = getCell()
        if cell == None or cell.className == "wall":
            handleCrash()
        elif cell.className == "r":
            audioImmunity.play()
            immunities.append("red")
            colorImmunity = document.getElementById("Red")
            colorImmunity.className = "redcolor"
            cell.className = "car"
        elif cell.className == "y":
            audioImmunity.play()
            immunities.append("yellow")
            immunities.append("yellow")
            colorImmunity = document.getElementById("Yellow")
            colorImmunity.className = "yellowcolor"
            cell.className = "car"
        elif cell.className == "g":
            audioImmunity.play()
            immunities.append("green")
            colorImmunity = document.getElementById("Green")
            colorImmunity.className = "greencolor"
            cell.className = "car"
        elif cell.className == "c":
            audioImmunity.play()
            immunities.append("cyan")
            immunities.append("cyan")
            colorImmunity = document.getElementById("Cyan")
            colorImmunity.className = "cyancolor"
            cell.className = "car"
        elif cell.className == "b":
            audioImmunity.play()
            immunities.append("blue")
            immunities.append("blue")
            colorImmunity = document.getElementById("Blue")
            colorImmunity.className = "bluecolor"
            cell.className = "car"
        elif cell.className == "m":
            audioImmunity.play()
            immunities.append("magenta")
            immunities.append("magenta")
            colorImmunity = document.getElementById("Magenta")
            colorImmunity.className = "magentacolor"
            cell.className = "car"
        elif cell.className == "o":
            audioImmunity.play()
            immunities.append("orange")
            immunities.append("orange")
            colorImmunity = document.getElementById("Orange")
            colorImmunity.className = "orangecolor"
            cell.className = "car"
        elif cell.className == "dg":
            audioImmunity.play()
            immunities.append("darkg")
            immunities.append("darkg")
            colorImmunity = document.getElementById("DarkGreen")
            colorImmunity.className = "darkgreencolor"
            cell.className = "car"
        elif cell.className == "p":
            audioImmunity.play()
            immunities.append("purple")
            colorImmunity = document.getElementById("Purple")
            colorImmunity.className = "purplecolor"
            cell.className = "car"
        elif cell.className == "rmonster":
            if not "red" in immunities:
                handleMonsterCrash()
            else:
                audioMonster.play()
                immunities.remove("red")
                if not "red" in immunities:
                    colorImmunity = document.getElementById("Red")
                    colorImmunity.className = "R"
                cell.className = "carandrmonster"
        elif cell.className == "ymonster":
            if not "yellow" in immunities:
                handleMonsterCrash()
            else:
                audioMonster.play()
                immunities.remove("yellow")
                if not "yellow" in immunities:
                    colorImmunity = document.getElementById("Yellow")
                    colorImmunity.className = "Y"
                cell.className = "carandymonster"
        elif cell.className == "gmonster":
            if not "green" in immunities:
                handleMonsterCrash()
            else:
                audioMonster.play()
                immunities.remove("green")
                if not "green" in immunities:
                    colorImmunity = document.getElementById("Green")
                    colorImmunity.className = "G"
                cell.className = "carandgmonster"
        elif cell.className == "cmonster":
            if not "cyan" in immunities:
                handleMonsterCrash()
            else:
                audioMonster.play()
                immunities.remove("cyan")
                if not "cyan" in immunities:
                    colorImmunity = document.getElementById("Cyan")
                    colorImmunity.className = "C"
                cell.className = "carandcmonster"
        elif cell.className == "bmonster":
            if not "blue" in immunities:
                handleMonsterCrash()
            else:
                audioMonster.play()
                immunities.remove("blue")
                if not "blue" in immunities:
                    colorImmunity = document.getElementById("Blue")
                    colorImmunity.className = "B"
                cell.className = "carandbmonster"
        elif cell.className == "mmonster":
            if not "magenta" in immunities:
                handleMonsterCrash()
            else:
                audioMonster.play()
                immunities.remove("magenta")
                if not "magenta" in immunities:
                    colorImmunity = document.getElementById("Magenta")
                    colorImmunity.className = "M"
                cell.className = "carandmmonster"
        elif cell.className == "omonster":
            if not "orange" in immunities:
                handleMonsterCrash()
            else:
                audioMonster.play()
                immunities.remove("orange")
                if not "orange" in immunities:
                    colorImmunity = document.getElementById("Orange")
                    colorImmunity.className = "O"
                cell.className = "carandomonster"
        elif cell.className == "dgmonster":
            if not "darkg" in immunities:
                handleMonsterCrash()
            else:
                audioMonster.play()
                immunities.remove("darkg")
                if not "darkg" in immunities:
                    colorImmunity = document.getElementById("DarkGreen")
                    colorImmunity.className = "DG"
                cell.className = "caranddgmonster"
        elif cell.className == "pmonster":
            if not "purple" in immunities:
                handleMonsterCrash()
            else:
                audioMonster.play()
                immunities.remove("purple")
                if not "purple" in immunities:
                    colorImmunity = document.getElementById("Purple")
                    colorImmunity.className = "P"
                cell.className = "carandpmonster"
        elif cell.className == "flag":
            cell.className = "carandflag"
            if coins == 3:
                endGame()
            else:
                notEnoughCoins()
        elif cell.className == "coin1":
            audioCoin.play()
            coins += 1
            cell.className = "car"
        elif cell.className == "coin2":
            audioCoin.play()
            coins += 1
            cell.className = "car"
        elif cell.className == "coin3":
            audioCoin.play()
            coins += 1
            cell.className = "car"
        elif cell.className == "player2":
            handleEvilMonsterCrash()
        else:
            cell.className = "car"


# if the car crashes, this tidies up including crash message
def handleCrash():
    audioCrash.play()
    window.clearInterval(intervalHandle)
    if player2dead == True:
        document.getElementById("Message").innerText = "Oops Player 1 crashed too... You both lose."
    else:
        window.clearInterval(player2intervalHandle)
        document.getElementById("Message").innerText = "Player 1 crashed... Player 2 wins."

def handleMonsterCrash():
    audioMonsterCrash.play()
    window.clearInterval(intervalHandle)
    window.clearInterval(player2intervalHandle)
    document.getElementById("Message").innerText = "Player 1 went into a monster... Player 2 wins."

def handleEvilMonsterCrash():
    audioPlayerCrash.play()
    window.clearInterval(intervalHandle)
    window.clearInterval(player2intervalHandle)
    document.getElementById("Message").innerText = "Player 1 went into Player 2... Player 2 wins."

# reaching the flag
def endGame():
    audioWin.play()
    window.clearInterval(intervalHandle)
    window.clearInterval(player2intervalHandle)
    score = 238 - moves
    if score <= 0:
        document.getElementById("Message").innerText = "Player 1 won! (But took too long) Score: 0/119 _-_-_-_-_-_-_-_-_-_-_-_-_ Refresh page to play again"
    elif score <= 119:
        document.getElementById("Message").innerText = "Player 1 won! Score: {}/119 _-_-_-_-_-_-_-_-_-_-_-_-_ Refresh page to play again".format(score)
    else:
        document.getElementById("Message").innerText = "Player 1 won! Score: {}/119 (Well done that shouldn't be possible) _-_-_-_-_-_-_-_-_-_-_-_-_ Refresh page to play again".format(score)

def notEnoughCoins():
    document.getElementById("Message").innerText = "Player 1 - You need all 3 coins to win."
    global immunities
    colorImmunity = document.getElementById("Red")
    colorImmunity.className = "redcolor"
    colorImmunity = document.getElementById("Yellow")
    colorImmunity.className = "yellowcolor"
    colorImmunity = document.getElementById("Green")
    colorImmunity.className = "greencolor"
    colorImmunity = document.getElementById("Cyan")
    colorImmunity.className = "cyancolor"
    colorImmunity = document.getElementById("Blue")
    colorImmunity.className = "bluecolor"
    colorImmunity = document.getElementById("Magenta")
    colorImmunity.className = "magentacolor"
    colorImmunity = document.getElementById("Orange")
    colorImmunity.className = "orangecolor"
    colorImmunity = document.getElementById("DarkGreen")
    colorImmunity.className = "darkgreencolor"
    colorImmunity = document.getElementById("Purple")
    colorImmunity.className = "purplecolor"
    immunities = ["red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple"]

# called when the page is loaded to start the timer checks
def runGame():
    global intervalHandle
    print("Running Game")
    document.addEventListener('keydown', checkKey)
    intervalHandle = window.setInterval(updatePosition, 300)

#############################
# Library Imports
#############################
from js import document, window

#############################
# Global Variables
#############################

# to store current position (x,y)
player2position = [6, 0]

# to store movement directions (x,y)
player2direction = [0, 0]

# to store the handle code for the timer interval to cancel it when we crash
player2intervalHandle = 0

player2dead = False


#############################
# Sub-Programs
#############################

# the function called when a key is pressed - sets direction variable
def checkplayer2Key(event):
    event.preventDefault()
    if event.key == "d":
        player2direction[0] = 1
        player2direction[1] = 0
    elif event.key == "a":
        # left arrow
        player2direction[0] = -1
        player2direction[1] = 0
    elif event.key == "w":
        player2direction[0] = 0
        player2direction[1] = -1
    elif event.key == "s":
        player2direction[0] = 0
        player2direction[1] = 1

def getplayer2Cell():
    return document.getElementById("R{}C{}".format(player2position[1], player2position[0]))

# the timer check function - runs every 300 milliseconds to update the car position
def updateplayer2Position():
    if player2direction[0] != 0 or player2direction[1] != 0:
        # Set the cell where the car was to empty
        player2cell = getplayer2Cell()
        if player2cell.className == "player2":
            player2cell.className = ""
        elif player2cell.className == "player2andrmonster":
            player2cell.className = "rmonster"
        elif player2cell.className == "player2andymonster":
            player2cell.className = "ymonster"
        elif player2cell.className == "player2andgmonster":
            player2cell.className = "gmonster"
        elif player2cell.className == "player2andcmonster":
            player2cell.className = "cmonster"
        elif player2cell.className == "player2andbmonster":
            player2cell.className = "bmonster"
        elif player2cell.className == "player2andmmonster":
            player2cell.className = "mmonster"
        elif player2cell.className == "player2andomonster":
            player2cell.className = "omonster"
        elif player2cell.className == "player2anddgmonster":
            player2cell.className = "dgmonster"
        elif player2cell.className == "player2andpmonster":
            player2cell.className = "pmonster"
        elif player2cell.className == "player2andr":
            player2cell.className = "r"
        elif player2cell.className == "player2andy":
            player2cell.className = "y"
        elif player2cell.className == "player2andg":
            player2cell.className = "g"
        elif player2cell.className == "player2andc":
            player2cell.className = "c"
        elif player2cell.className == "player2andb":
            player2cell.className = "b"
        elif player2cell.className == "player2andm":
            player2cell.className = "m"
        elif player2cell.className == "player2ando":
            player2cell.className = "o"
        elif player2cell.className == "player2anddg":
            player2cell.className = "dg"
        elif player2cell.className == "player2andp":
            player2cell.className = "p"
        elif player2cell.className == "player2andflag":
            player2cell.className = "flag"
        elif player2cell.className == "player2andcoin1":
            player2cell.className = "coin1"
        elif player2cell.className == "player2andcoin2":
            player2cell.className = "coin2"
        elif player2cell.className == "player2andcoin3":
            player2cell.className = "coin3"
        
        # Update the column position for the car
        player2position[0] += player2direction[0]
        player2position[1] += player2direction[1]

        # Re-draw the car (or report a crash)
        player2cell = getplayer2Cell()
        if player2cell == None or player2cell.className == "wall":
            handleplayer2Crash()
        elif player2cell.className == "r":
            player2cell.className = "player2andr"
        elif player2cell.className == "y":
            player2cell.className = "player2andy"
        elif player2cell.className == "g":
            player2cell.className = "player2andg"
        elif player2cell.className == "c":
            player2cell.className = "player2andc"
        elif player2cell.className == "b":
            player2cell.className = "player2andb"
        elif player2cell.className == "m":
            player2cell.className = "player2andm"
        elif player2cell.className == "o":
            player2cell.className = "player2ando"
        elif player2cell.className == "dg":
            player2cell.className = "player2anddg"
        elif player2cell.className == "p":
            player2cell.className = "player2andp"
        elif player2cell.className == "rmonster":
            player2cell.className = "player2andrmonster"
        elif player2cell.className == "ymonster":
            player2cell.className = "player2andymonster"
        elif player2cell.className == "gmonster":
            player2cell.className = "player2andgmonster"
        elif player2cell.className == "cmonster":
            player2cell.className = "player2andcmonster"
        elif player2cell.className == "bmonster":
            player2cell.className = "player2andbmonster"
        elif player2cell.className == "mmonster":
            player2cell.className = "player2andmmonster"
        elif player2cell.className == "omonster":
            player2cell.className = "player2andomonster"
        elif player2cell.className == "dgmonster":
            player2cell.className = "player2anddgmonster"
        elif player2cell.className == "pmonster":
            player2cell.className = "player2andpmonster"
        elif player2cell.className == "flag":
            player2cell.className = "player2andflag"
        elif player2cell.className == "coin1":
            player2cell.className = "player2andcoin1"
        elif player2cell.className == "coin2":
            player2cell.className = "player2andcoin2"
        elif player2cell.className == "coin3":
            player2cell.className = "player2andcoin3"
        elif player2cell.className == "car":
            player2cell.className = "player2"
            endplayer2Game()
        else:
            player2cell.className = "player2"


# if the car crashes, this tidies up including crash message
def handleplayer2Crash():
    global player2dead
    window.clearInterval(player2intervalHandle)
    document.getElementById("Message").innerText = "Player 2 crashed... (yay)"
    player2dead = True

def endplayer2Game():
    window.clearInterval(intervalHandle)
    window.clearInterval(player2intervalHandle)
    document.getElementById("Message").innerText = "Player 1 got caught and died. Player 2 wins."

# called when the page is loaded to start the timer checks
def runplayer2Game():
    global player2intervalHandle
    document.addEventListener('keydown', checkplayer2Key)
    player2intervalHandle = window.setInterval(updateplayer2Position, 300)

#############################
# Library Imports
#############################
from js import document, window

#############################
# Global Variables
#############################

# to store current position (x,y)
singleplayerposition = [0, 0]

# to store movement directions (x,y)
singleplayerdirection = [0, 0]

# to store the handle code for the timer interval to cancel it when we crash
singleplayerintervalHandle = 0

singleplayerimmunities = []
singleplayercoins = 0
singleplayermoves = 0

audioWin = document.getElementById("audioWin")
audioCoin = document.getElementById("audioCoin")
audioCrash = document.getElementById("audioCrash")
audioMonsterCrash = document.getElementById("audioMonsterCrash")
audioPlayerCrash = document.getElementById("audioPlayerCrash")
audioImmunity = document.getElementById("audioImmunity")
audioMonster = document.getElementById("audioMonster")

#############################
# Sub-Programs
#############################

# the function called when a key is pressed - sets direction variable
def singleplayercheckKey(event):
    event.preventDefault()
    if event.key == "ArrowRight":
        singleplayerdirection[0] = 1
        singleplayerdirection[1] = 0
    elif event.key == "ArrowLeft":
        # left arrow
        singleplayerdirection[0] = -1
        singleplayerdirection[1] = 0
    elif event.key == "ArrowUp":
        singleplayerdirection[0] = 0
        singleplayerdirection[1] = -1
    elif event.key == "ArrowDown":
        singleplayerdirection[0] = 0
        singleplayerdirection[1] = 1

def singleplayergetCell():
    return document.getElementById("R{}C{}".format(singleplayerposition[1], singleplayerposition[0]))

# the timer check function - runs every 300 milliseconds to update the car position
def singleplayerupdatePosition():
    global singleplayermoves
    singleplayermoves += 1
    if singleplayerdirection[0] != 0 or singleplayerdirection[1] != 0:
        # Set the cell where the car was to empty
        singleplayercell = singleplayergetCell()
        if singleplayercell.className == "car":
            singleplayercell.className = ""
        elif singleplayercell.className == "carandrmonster":
            singleplayercell.className = "rmonster"
        elif singleplayercell.className == "carandymonster":
            singleplayercell.className = "ymonster"
        elif singleplayercell.className == "carandgmonster":
            singleplayercell.className = "gmonster"
        elif singleplayercell.className == "carandcmonster":
            singleplayercell.className = "cmonster"
        elif singleplayercell.className == "carandbmonster":
            singleplayercell.className = "bmonster"
        elif singleplayercell.className == "carandmmonster":
            singleplayercell.className = "mmonster"
        elif singleplayercell.className == "carandomonster":
            singleplayercell.className = "omonster"
        elif singleplayercell.className == "caranddgmonster":
            singleplayercell.className = "dgmonster"
        elif singleplayercell.className == "carandpmonster":
            singleplayercell.className = "pmonster"
        elif singleplayercell.className == "carandflag":
            singleplayercell.className = "flag"
        
        # Update the column position for the car
        singleplayerposition[0] += singleplayerdirection[0]
        singleplayerposition[1] += singleplayerdirection[1]

        # Re-draw the car (or report a crash)
        global singleplayercoins
        singleplayercell = singleplayergetCell()
        if singleplayercell == None or singleplayercell.className == "wall":
            singleplayerhandleCrash()
        elif singleplayercell.className == "r":
            audioImmunity.play()
            singleplayerimmunities.append("red")
            singleplayercolorImmunity = document.getElementById("Red")
            singleplayercolorImmunity.className = "redcolor"
            singleplayercell.className = "car"
        elif singleplayercell.className == "y":
            audioImmunity.play()
            singleplayerimmunities.append("yellow")
            singleplayerimmunities.append("yellow")
            singleplayercolorImmunity = document.getElementById("Yellow")
            singleplayercolorImmunity.className = "yellowcolor"
            singleplayercell.className = "car"
        elif singleplayercell.className == "g":
            audioImmunity.play()
            singleplayerimmunities.append("green")
            singleplayercolorImmunity = document.getElementById("Green")
            singleplayercolorImmunity.className = "greencolor"
            singleplayercell.className = "car"
        elif singleplayercell.className == "c":
            audioImmunity.play()
            singleplayerimmunities.append("cyan")
            singleplayerimmunities.append("cyan")
            singleplayercolorImmunity = document.getElementById("Cyan")
            singleplayercolorImmunity.className = "cyancolor"
            singleplayercell.className = "car"
        elif singleplayercell.className == "b":
            audioImmunity.play()
            singleplayerimmunities.append("blue")
            singleplayerimmunities.append("blue")
            singleplayercolorImmunity = document.getElementById("Blue")
            singleplayercolorImmunity.className = "bluecolor"
            singleplayercell.className = "car"
        elif singleplayercell.className == "m":
            audioImmunity.play()
            singleplayerimmunities.append("magenta")
            singleplayerimmunities.append("magenta")
            singleplayercolorImmunity = document.getElementById("Magenta")
            singleplayercolorImmunity.className = "magentacolor"
            singleplayercell.className = "car"
        elif singleplayercell.className == "o":
            audioImmunity.play()
            singleplayerimmunities.append("orange")
            singleplayerimmunities.append("orange")
            singleplayercolorImmunity = document.getElementById("Orange")
            singleplayercolorImmunity.className = "orangecolor"
            singleplayercell.className = "car"
        elif singleplayercell.className == "dg":
            audioImmunity.play()
            singleplayerimmunities.append("darkg")
            singleplayerimmunities.append("darkg")
            singleplayercolorImmunity = document.getElementById("DarkGreen")
            singleplayercolorImmunity.className = "darkgreencolor"
            singleplayercell.className = "car"
        elif singleplayercell.className == "p":
            audioImmunity.play()
            singleplayerimmunities.append("purple")
            singleplayercolorImmunity = document.getElementById("Purple")
            singleplayercolorImmunity.className = "purplecolor"
            singleplayercell.className = "car"
        elif singleplayercell.className == "rmonster":
            if not "red" in singleplayerimmunities:
                singleplayerhandleMonsterCrash()
            else:
                audioMonster.play()
                singleplayerimmunities.remove("red")
                if not "red" in singleplayerimmunities:
                    singleplayercolorImmunity = document.getElementById("Red")
                    singleplayercolorImmunity.className = "R"
                singleplayercell.className = "carandrmonster"
        elif singleplayercell.className == "ymonster":
            if not "yellow" in singleplayerimmunities:
                singleplayerhandleMonsterCrash()
            else:
                audioMonster.play()
                singleplayerimmunities.remove("yellow")
                if not "yellow" in singleplayerimmunities:
                    singleplayercolorImmunity = document.getElementById("Yellow")
                    singleplayercolorImmunity.className = "Y"
                singleplayercell.className = "carandymonster"
        elif singleplayercell.className == "gmonster":
            if not "green" in singleplayerimmunities:
                singleplayerhandleMonsterCrash()
            else:
                audioMonster.play()
                singleplayerimmunities.remove("green")
                if not "green" in singleplayerimmunities:
                    singleplayercolorImmunity = document.getElementById("Green")
                    singleplayercolorImmunity.className = "G"
                singleplayercell.className = "carandgmonster"
        elif singleplayercell.className == "cmonster":
            if not "cyan" in singleplayerimmunities:
                singleplayerhandleMonsterCrash()
            else:
                audioMonster.play()
                singleplayerimmunities.remove("cyan")
                if not "cyan" in singleplayerimmunities:
                    singleplayercolorImmunity = document.getElementById("Cyan")
                    singleplayercolorImmunity.className = "C"
                singleplayercell.className = "carandcmonster"
        elif singleplayercell.className == "bmonster":
            if not "blue" in singleplayerimmunities:
                singleplayerhandleMonsterCrash()
            else:
                audioMonster.play()
                singleplayerimmunities.remove("blue")
                if not "blue" in singleplayerimmunities:
                    singleplayercolorImmunity = document.getElementById("Blue")
                    singleplayercolorImmunity.className = "B"
                singleplayercell.className = "carandbmonster"
        elif singleplayercell.className == "mmonster":
            if not "magenta" in singleplayerimmunities:
                singleplayerhandleMonsterCrash()
            else:
                audioMonster.play()
                singleplayerimmunities.remove("magenta")
                if not "magenta" in singleplayerimmunities:
                    singleplayercolorImmunity = document.getElementById("Magenta")
                    singleplayercolorImmunity.className = "M"
                singleplayercell.className = "carandmmonster"
        elif singleplayercell.className == "omonster":
            if not "orange" in singleplayerimmunities:
                singleplayerhandleMonsterCrash()
            else:
                audioMonster.play()
                singleplayerimmunities.remove("orange")
                if not "orange" in singleplayerimmunities:
                    singleplayercolorImmunity = document.getElementById("Orange")
                    singleplayercolorImmunity.className = "O"
                singleplayercell.className = "carandomonster"
        elif singleplayercell.className == "dgmonster":
            if not "darkg" in singleplayerimmunities:
                singleplayerhandleMonsterCrash()
            else:
                audioMonster.play()
                singleplayerimmunities.remove("darkg")
                if not "darkg" in singleplayerimmunities:
                    singleplayercolorImmunity = document.getElementById("DarkGreen")
                    singleplayercolorImmunity.className = "DG"
                singleplayercell.className = "caranddgmonster"
        elif singleplayercell.className == "pmonster":
            if not "purple" in singleplayerimmunities:
                singleplayerhandleMonsterCrash()
            else:
                audioMonster.play()
                singleplayerimmunities.remove("purple")
                if not "purple" in singleplayerimmunities:
                    singleplayercolorImmunity = document.getElementById("Purple")
                    singleplayercolorImmunity.className = "P"
                singleplayercell.className = "carandpmonster"
        elif singleplayercell.className == "flag":
            singleplayercell.className = "carandflag"
            if singleplayercoins == 3:
                singleplayerendGame()
            else:
                singleplayernotEnoughCoins()
        elif singleplayercell.className == "coin1":
            audioCoin.play()
            singleplayercoins += 1
            singleplayercell.className = "car"
        elif singleplayercell.className == "coin2":
            audioCoin.play()
            singleplayercoins += 1
            singleplayercell.className = "car"
        elif singleplayercell.className == "coin3":
            audioCoin.play()
            singleplayercoins += 1
            singleplayercell.className = "car"
        else:
            singleplayercell.className = "car"


# if the car crashes, this tidies up including crash message
def singleplayerhandleCrash():
    audioCrash.play()
    window.clearInterval(singleplayerintervalHandle)
    document.getElementById("Message").innerText = "Oops you crashed... You lose."

def singleplayerhandleMonsterCrash():
    audioMonsterCrash.play()
    window.clearInterval(singleplayerintervalHandle)
    document.getElementById("Message").innerText = "Oops you went into a monster... You lose."

# reaching the flag
def singleplayerendGame():
    audioWin.play()
    window.clearInterval(singleplayerintervalHandle)
    singleplayerscore = 238 - singleplayermoves
    if singleplayerscore <= 0:
        document.getElementById("Message").innerText = "You won! (but you took a too long) Score: 0/119 _-_-_-_-_-_-_-_-_-_-_-_-_ Refresh page to play again"
    elif singleplayerscore <= 119:
        document.getElementById("Message").innerText = "You won! Score: {}/119 _-_-_-_-_-_-_-_-_-_-_-_-_ Refresh page to play again".format(singleplayerscore)
    else:
        document.getElementById("Message").innerText = "You won! Score: {}/119 (Well done that shouldn't be possible) _-_-_-_-_-_-_-_-_-_-_-_-_ Refresh page to play again".format(singleplayerscore)

def singleplayernotEnoughCoins():
    document.getElementById("Message").innerText = "You need all 3 coins to win."
    global singleplayerimmunities
    singleplayercolorImmunity = document.getElementById("Red")
    singleplayercolorImmunity.className = "redcolor"
    singleplayercolorImmunity = document.getElementById("Yellow")
    singleplayercolorImmunity.className = "yellowcolor"
    singleplayercolorImmunity = document.getElementById("Green")
    singleplayercolorImmunity.className = "greencolor"
    singleplayercolorImmunity = document.getElementById("Cyan")
    singleplayercolorImmunity.className = "cyancolor"
    singleplayercolorImmunity = document.getElementById("Blue")
    singleplayercolorImmunity.className = "bluecolor"
    singleplayercolorImmunity = document.getElementById("Magenta")
    singleplayercolorImmunity.className = "magentacolor"
    singleplayercolorImmunity = document.getElementById("Orange")
    singleplayercolorImmunity.className = "orangecolor"
    singleplayercolorImmunity = document.getElementById("DarkGreen")
    singleplayercolorImmunity.className = "darkgreencolor"
    singleplayercolorImmunity = document.getElementById("Purple")
    singleplayercolorImmunity.className = "purplecolor"
    singleplayerimmunities = ["red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple", "red", "yellow", "green", "cyan", "blue", "magenta", "orange", "darkg", "purple"]

# called when the page is loaded to start the timer checks
def singleplayerrunGame():
    global singleplayerintervalHandle
    print("Running Game")
    document.addEventListener('keydown', singleplayercheckKey)
    singleplayerintervalHandle = window.setInterval(singleplayerupdatePosition, 300)

#############################
# Main Program
#############################
choice = int(input("1 or 2 players?"))
audioWin.autoplay = False
audioWin.load()
audioCoin.autoplay = False
audioCoin.load()
audioCrash.autoplay = False
audioCrash.load()
audioMonsterCrash.autoplay = False
audioMonsterCrash.load()
audioPlayerCrash.autoplay = False
audioPlayerCrash.load()
if choice == 2:
    runGame()
    runplayer2Game()
elif choice == 1:
    UNWANTEDPLAYER = document.getElementById("R0C6")
    UNWANTEDPLAYER.className = ""
    singleplayerrunGame()