from js import document, window

# Game state
position = [0, 0]
direction = [0, 0]
intervalHandle = 0
coins = 0

# Enemy state
enemy_position = [9, 8] 
enemy_speed = 0.5 

def checkKey(event):
    event.preventDefault()
    if event.key == "d":
        direction[0] = 1
        direction[1] = 0
    elif event.key == "a":
        direction[0] = -1
        direction[1] = 0
    elif event.key == "w":
        direction[1] = -1
        direction[0] = 0
    elif event.key == "s":
        direction[1] = 1
        direction[0] = 0

def getCell():
    return document.getElementById("R{}C{}".format(position[1], position[0]))

def isEnemyHittingWall(enemy_position):
    # Check the tiles/colliders around the enemy's new position
    new_x = enemy_position[0] + direction[0] * enemy_speed
    new_y = enemy_position[1] + direction[1] * enemy_speed

    # Get all the wall elements and check for intersection
    wall_elements = document.getElementsByClassName("wall")
    for wall in wall_elements:
        x, y = map(int, wall.id.split("R")[1].split("C"))
        if (
            new_x + 1 > x and
            new_x < x + 1 and
            new_y + 1 > y and
            new_y < y + 1
        ):
            # Enemy is colliding with a wall, don't let them move
            return True

    # Check for coins
    coin_elements = document.getElementsByClassName("coin")
    for coin in coin_elements:
        x, y = map(int, coin.id.split("R")[1].split("C"))
        if (
            new_x + 1 > x and
            new_x < x + 1 and
            new_y + 1 > y and
            new_y < y + 1
        ):
            # Enemy is on a coin, jump over it
            return False

    # No collision detected, enemy can move
    return False

def update_enemy_position():
    global enemy_position

    dx = position[0] - enemy_position[0]
    dy = position[1] - enemy_position[1]

    norm = (dx**2 + dy**2)**0.5
    if norm > 0:
        dx /= norm
        dy /= norm

    old_enemy_position = enemy_position.copy()
    new_enemy_position = [
        enemy_position[0] + dx * enemy_speed,
        enemy_position[1] + dy * enemy_speed
    ]

    if not isEnemyHittingWall(new_enemy_position):
        enemy_position = new_enemy_position

    enemy_cell = document.getElementById(f"R{int(old_enemy_position[1])}C{int(old_enemy_position[0])}")
    enemy_cell.className = ""
    enemy_cell = document.getElementById(f"R{int(enemy_position[1])}C{int(enemy_position[0])}")
    enemy_cell.className = "enemy"

def updatePosition():
    if direction[0] != 0 or direction[1] != 0:
        cell = getCell()
        cell.className = ""

        position[0] += direction[0]
        position[1] += direction[1]

        update_enemy_position()

        cell = getCell()
        if cell is None or cell.classList.contains("wall"):
            handleCrash()
        elif cell.className == "coin":
            handelCoinGet()
        elif cell.className == "end":
            handelWin(7)
        elif cell.className == "enemy":
            handleDeath()
        else:
            cell.className = "car"

def handleCrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Oops you crashed..."

def handleDeath():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Oh no, the enemy caught you!"

def handelCoinGet():
    global coins
    coins += 1
    cell = getCell()
    cell.className = ""
    cell.className = "car"

def handelWin(totalcoins):
    global coins
    window.clearInterval(intervalHandle)
    if coins == totalcoins:
        document.getElementById("Message").innerText = f"You win, you got {coins} coins"
    else:
        document.getElementById("Message").innerText = "Collect all the coins to win"
        cell = getCell()
        cell.className = ""
        cell.className = "car"

def runGame():
    global intervalHandle

    print("Running Game")

    document.addEventListener('keydown', checkKey)

    intervalHandle = window.setInterval(updatePosition, 300)

runGame()