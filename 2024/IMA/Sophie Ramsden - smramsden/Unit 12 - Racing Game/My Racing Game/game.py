#############################
# Library Imports
#############################
from js import document, window

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
            immunities.append("red")
            cell.className = "car"
        elif cell.className == "y":
            immunities.append("yellow")
            immunities.append("yellow")
            cell.className = "car"
        elif cell.className == "g":
            immunities.append("green")
            cell.className = "car"
        elif cell.className == "c":
            immunities.append("cyan")
            immunities.append("cyan")
            cell.className = "car"
        elif cell.className == "b":
            immunities.append("blue")
            immunities.append("blue")
            cell.className = "car"
        elif cell.className == "m":
            immunities.append("magenta")
            immunities.append("magenta")
            cell.className = "car"
        elif cell.className == "o":
            immunities.append("orange")
            immunities.append("orange")
            cell.className = "car"
        elif cell.className == "dg":
            immunities.append("darkg")
            immunities.append("darkg")
            cell.className = "car"
        elif cell.className == "p":
            immunities.append("purple")
            cell.className = "car"
        elif cell.className == "rmonster":
            if not "red" in immunities:
                handleMonsterCrash()
            else:
                immunities.remove("red")
                cell.className = "carandrmonster"
        elif cell.className == "ymonster":
            if not "yellow" in immunities:
                handleMonsterCrash()
            else:
                immunities.remove("yellow")
                cell.className = "carandymonster"
        elif cell.className == "gmonster":
            if not "green" in immunities:
                handleMonsterCrash()
            else:
                immunities.remove("green")
                cell.className = "carandgmonster"
        elif cell.className == "cmonster":
            if not "cyan" in immunities:
                handleMonsterCrash()
            else:
                immunities.remove("cyan")
                cell.className = "carandcmonster"
        elif cell.className == "bmonster":
            if not "blue" in immunities:
                handleMonsterCrash()
            else:
                immunities.remove("blue")
                cell.className = "carandbmonster"
        elif cell.className == "mmonster":
            if not "magenta" in immunities:
                handleMonsterCrash()
            else:
                immunities.remove("magenta")
                cell.className = "carandmmonster"
        elif cell.className == "omonster":
            if not "orange" in immunities:
                handleMonsterCrash()
            else:
                immunities.remove("orange")
                cell.className = "carandomonster"
        elif cell.className == "dgmonster":
            if not "darkg" in immunities:
                handleMonsterCrash()
            else:
                immunities.remove("darkg")
                cell.className = "caranddgmonster"
        elif cell.className == "pmonster":
            if not "purple" in immunities:
                handleMonsterCrash()
            else:
                immunities.remove("purple")
                cell.className = "carandpmonster"
        elif cell.className == "flag":
            cell.className = "carandflag"
            if coins == 3:
                endGame()
            else:
                notEnoughCoins()
        elif cell.className == "coin1":
            coins += 1
            cell.className = "car"
        elif cell.className == "coin2":
            coins += 1
            cell.className = "car"
        elif cell.className == "coin3":
            coins += 1
            cell.className = "car"
        elif cell.className == "player2":
            handleEvilMonsterCrash()
        else:
            cell.className = "car"


# if the car crashes, this tidies up including crash message
def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Oops Player 1 crashed... Player 2 wins."

def handleMonsterCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Player 1 - Don't go into monsters."

def handleEvilMonsterCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Player 1 went into Player 2... Player 2 wins."

# reaching the flag
def endGame():
    window.clearInterval(intervalHandle)
    score = 228 - moves
    document.getElementById("Message").innerText = "Player 1 won! Score: {}/114".format(score)

def notEnoughCoins():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Player 1 - You need all 3 coins to finish."

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
    window.clearInterval(player2intervalHandle)
    document.getElementById("Message").innerText = "Player 2 crashed... (yay)"

def endplayer2Game():
    window.clearInterval(player2intervalHandle)
    document.getElementById("Message").innerText = "Player 1 got caught and died. Player 2 wins."

# called when the page is loaded to start the timer checks
def runplayer2Game():
    global player2intervalHandle
    document.addEventListener('keydown', checkplayer2Key)
    player2intervalHandle = window.setInterval(updateplayer2Position, 300)

#############################
# Main Program
#############################
runGame()
runplayer2Game()