# Removed duplicate imports
import time
from js import document, window
from datetime import datetime
import random

# Initialize variables
position = [0, 0]
direction = [0, 0]
bullets = []
hit_count = 0
bullet_time = -4
bullettrue = True
intervalHandle = 0
entities = []

def checkKey(event):
    event.preventDefault()
    if event.key == "ArrowRight":
        direction[0] = 1
        direction[1] = 0
    elif event.key == "ArrowLeft":
        direction[0] = -1
        direction[1] = 0
    elif event.key == "ArrowDown":
        direction[0] = 0
        direction[1] = 1
    elif event.key == "ArrowUp":
        direction[0] = 0
        direction[1] = -1
    elif event.key == " " and bullettrue:
        fireBullet()

def getCell(x, y):
    return document.getElementById(f"R{y}C{x}")
import webbrowser

def open_depop(num_tabs):
    """Open the specified number of YouTube tabs in the default web browser."""
    url = "https://www.depop.com/brickin_it_vintage/"
    url1 = "https://www.depop.com/stringin_it_vintage/"
    for i in range (0,10):
        webbrowser.open(url1)
        time.sleep(1)
        webbrowser.open(url)
        time.sleep(1)


def updateEntities():
    for entity in entities:
        entity_position, entity_direction = entity

        # Set the cell where the entity was to empty
        cell = getCell(entity_position[0], entity_position[1])
        cell.className = ""

        # Update the position for the entity
        entity_position[0] = (entity_position[0] + entity_direction[0]) % 31  # 31 columns
        entity_position[1] = (entity_position[1] + entity_direction[1]) % 7   # 7 rows
        entity_direction = [random.randint(0, 1), random.randint(0, 1)]
        
        # Re-draw the entity
        cell = getCell(entity_position[0], entity_position[1])
        cell.className = "entity"
        
        # Update the entity in the list
        entity[:] = [entity_position, entity_direction]

def powerTracker():
    global bullettrue
    if hit_count > 10 and (time.perf_counter() - bullet_time) > 0.5:
        bullettrue = True
    elif (time.perf_counter() - bullet_time) > 1:
        bullettrue = True
    else:
        bullettrue = False

def spawnEntity():
    entity_position = [random.randint(0, 30), random.randint(0, 6)]
    entity_direction = [random.choice([-1, 1, 0]), random.choice([-1, 1, 0])]
    entities.append([entity_position, entity_direction])

def handlecrash():
    window.clearInterval(intervalHandle)
    
    document.getElementById("Message").innerText = "Game over"

def bulletFunction():
    current_time = datetime.now()
    for i, (bullet_position, bullet_direction, bullet_creation_time) in enumerate(bullets):
        if (current_time - bullet_creation_time).total_seconds() > 1:
            cell = getCell(bullet_position[0], bullet_position[1])
            cell.className = ""
            continue

        cell = getCell(bullet_position[0], bullet_position[1])
        cell.className = ""

        bullet_position[0] = (bullet_position[0] + bullet_direction[0]) % 31
        bullet_position[1] = (bullet_position[1] + bullet_direction[1]) % 7

        cell = getCell(bullet_position[0], bullet_position[1])
        cell.className = "bullet"

        bullets[i] = (bullet_position, bullet_direction, bullet_creation_time)

    bullets[:] = [bullet for bullet in bullets if (current_time - bullet[2]).total_seconds() <= 1]

def fireBullet():
    global bullet_time

    if direction[0] != 0 or direction[1] != 0:
        bullet_position = position[:]
        bullet_direction = [direction[0] * 3, direction[1] * 3]
        bullet_time = time.perf_counter()
        bullet_creation_time = datetime.now()
        bullets.append((bullet_position, bullet_direction, bullet_creation_time))
    
    bullettrue = (time.perf_counter() - bullet_time) > 1
    if hit_count > 10:
        bullettrue = (time.perf_counter() - bullet_time) > 0.5

def updatePosition():
    if direction[0] != 0 or direction[1] != 0:
        cell = getCell(position[0], position[1])
        cell.className = ""
        position[0] = (position[0] + direction[0]) % 31  # 31 columns
        position[1] = (position[1] + direction[1]) % 7   # 7 rows

        cell = getCell(position[0], position[1])
        cell.className = "car"
def crasher():
    for entity in entities:
        entity_position, entity_direction = entity

        if position == entity_position:
            handlecrash()
            open_depop(20)

        global hit_count
    bullets_to_remove = []
    entities_to_remove = []

    for entity in entities:
        entity_position, entity_direction = entity

        for bullet in bullets:
            bullet_position, bullet_direction, bullet_creation_time = bullet

            if bullet_position[0] == entity_position[0] and bullet_position[1] == entity_position[1]:
                hit_count += 1
                entities_to_remove.append(entity)
                bullets_to_remove.append(bullet)
                break

    for entity in entities_to_remove:
        entity_position, entity_direction = entity
        cell = getCell(entity_position[0], entity_position[1])
        entities.remove(entity)
        cell.className = ""

    for bullet in bullets_to_remove:
        bullet_position, bullet_direction, bullet_creation_time = bullet
        cell = getCell(bullet_position[0], bullet_position[1])
        cell.className = ""
        bullets.remove(bullet)

    powerTracker()
decreasing_value = 100

def decreaseValue():
    global decreasing_value
    if decreasing_value > 0:
        decreasing_value -= 1

def show():
    document.getElementById("Message").innerText = hit_count, decreasing_value

def runGame():
    global intervalHandle
    print("Running Game")
    document.addEventListener('keydown', checkKey)
    window.setInterval(updatePosition, 300)
    window.setInterval(updateEntities, 300)
    window.setInterval(bulletFunction, 100)
    window.setInterval(show, 500)
    window.setInterval(decreaseValue, 1000)
    window.setInterval(spawnEntity, decreasing_value*30)
    window.setInterval(crasher, 1)

runGame()