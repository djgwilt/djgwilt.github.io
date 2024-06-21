import time
from js import document, window
from datetime import datetime
from js import document, window
import random



position = [0, 0]
direction = [0, 0]
bullets = []
hit_count = 0
bullet_time = -4
bullettrue = (time.perf_counter() - bullet_time) >1
intervalHandle = 0
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
    return document.getElementById("R{}C{}".format(y, x))

from js import document, window
from datetime import datetime
entities = []
def updateEntities():
    global entity_position
    for entity in entities:
        entity_position, entity_direction = entity

        # Set the cell where the entity was to empty
        cell = getCell(entity_position[0], entity_position[1])
        cell.className = ""

        # Update the position for the entity
        entity_position[0] = (entity_position[0] + entity_direction[0]) % 31  # 31 columns
        entity_position[1] = (entity_position[1] + entity_direction[1]) % 7   # 7 rows
        entity_direction = [random.randint(0,1),random.randint(0,1)]
        # Re-draw the entity
        cell = getCell(entity_position[0], entity_position[1])
        cell.className = "entity"  
        # Update the entity in the list
        entity[:] = [entity_position, entity_direction]
def powertracker():
    bullettrue = (time.perf_counter() - bullet_time) >1
    if hit_count>10:
        bullettrue = (time.perf_counter() - bullet_time) >0.5

def spawnEntity():
    entity_position = [random.randint(0, 30), random.randint(0, 6)]
    entity_direction = [random.choice([-1, 1, 0]), random.choice([-1, 1, 0])]
    entities.append([entity_position, entity_direction])
    updateEntities()
def handlecrash():
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Game over"
def bulletFunction():
    global hit_count
    # Temporary lists to 
    bullets_to_remove = []
    entities_to_remove = []
    for bullet in bullets:
        bullet_position, bullet_direction, bullet_creation_time = bullet

        for entity in entities:
            entity_position, entity_direction = entity

            if bullet_position == entity_position:
                hit_count += 1
                # Mark the entity 
                entities_to_remove.append(entity)

                # Mark the bullet 
                bullets_to_remove.append(bullet)
                break

    # Remove marked entities
    for entity in entities_to_remove:
        entity_position, entity_direction = entity
        cell = getCell(entity_position[0], entity_position[1])
        cell.className = ""
        entities.remove(entity)
    for bullet in bullets_to_remove:
        bullet_position, bullet_direction, bullet_creation_time = bullet
        cell = getCell(bullet_position[0], bullet_position[1])
        cell.className = ""
        bullets.remove(bullet)

    current_time = datetime.now()
    for i, (bullet_position, bullet_direction, bullet_creation_time) in enumerate(bullets):
        
        if (current_time - bullet_creation_time).total_seconds() > 1:
            
            cell = getCell(bullet_position[0], bullet_position[1])
            cell.className = ""
            continue  

        cell = getCell(bullet_position[0], bullet_position[1])
        cell.className = ""
        
        # Update the position 
        bullet_position[0] = (bullet_position[0] + bullet_direction[0]) % 31  
        bullet_position[1] = (bullet_position[1] + bullet_direction[1]) % 7   

        
        cell = getCell(bullet_position[0], bullet_position[1])
        cell.className = "bullet"
        
        
        bullets[i] = (bullet_position, bullet_direction, bullet_creation_time)

    # Remove old bullets
    bullets[:] = [bullet for bullet in bullets if (current_time - bullet[2]).total_seconds() <= 1]

def fireBullet():
    global bullet_time

    if direction[0] != 0 or direction[1] != 0:
        bullet_position = position[:]
        bullet_direction = [direction[0] * 3, direction[1] * 3]
        bullet_time = time.perf_counter()
        bullet_creation_time = datetime.now()
        bullets.append((bullet_position, bullet_direction, bullet_creation_time))

def updatePosition():
    if direction[0] != 0 or direction[1] != 0:
        cell = getCell(position[0], position[1])
        cell.className = ""
        position[0] = (position[0] + direction[0]) % 31  # 31 columns
        position[1] = (position[1] + direction[1]) % 7   # 7 rows

        cell = getCell(position[0], position[1])
        cell.className = "car"
    for entity in entities:
        entity_position, entity_direction = entity

        if position == entity_position:
            handlecrash()

      


def show():
    document.getElementById("Message").innerText = bullettrue

def runGame():
    global intervalHandle
    print("Running Game")
    document.addEventListener('keydown', checkKey)
    intervalHandle = window.setInterval(updatePosition, 300)
    intervalHandle = window.setInterval(updateEntities, 300)
    intervalHandle = window.setInterval(bulletFunction, 150)
    intervalHandle = window.setInterval(show,500)
    window.setInterval(spawnEntity, 3000)

runGame()