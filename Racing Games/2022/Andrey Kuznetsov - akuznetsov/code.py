#############################
# Library Imports
#############################
from asyncio import events
from faulthandler import disable
from multiprocessing import Event
# from multiprocessing.reduction import duplicate
from re import U
from js import document, window
import random



#############################
# Global Variables
#############################

# to store movement direction
xDir = 0
yDir = 0
# to store current column position
column = 0

# to store the handle code for the timer interval to cancel it when we crash
intervalHandle = 0
crashed = False
# snake list
unnocupied_space = 'Fore.WHITE' + '_'
snake_body = 'Fore.GREEN' + '*'
orange = 'orange'
border = 'Fore.BLUE' + '+'
duplicates = False
snake_body_horizontal = "Snake_body_horizontal"
snake_body_vertical = "Snake_body_vertical"
snake_head_up = "Snake_head_up"
snake_head_down = "Snake_head_down"
snake_head_left = "Snake_head_left"
snake_head_right = "Snake_head_right"
Left_Up_turn = "Left_Up_turn"
Right_Up_turn = "Right_Up_turn"
Left_Down_turn = "Left_Down_turn"
Right_Down_turn = "Right_Down_turn"
tail_Right = "Tail_Right"
tail_Left = "Tail_Left"
tail_Up = "Tail_Up"
tail_Down = "Tail_Down"
rock = "rock"
grid_width = 15
grid_height = 10
up = (0, -1)
down = (0, 1)
left = (-1, 0)
right = (1, 0)

frame_rate = 300

obstacles = {}

oranges = {}

for i in range(10):
    rx = random.randint(-1, grid_width)
    ry = random.randint(-1, grid_height)
    oranges[(rx, ry)] = orange

snake = [
    ((7, 1), down),
    ((7, 2), down),
    ((7, 3), down),
    ((7, 4), down),
    ((7, 5), down),
    ((7, 6), down),
    ((7, 7), down),
    ((7, 8), down)
]

for i in range(10):
    rx = random.randint(-1, grid_width)
    ry = random.randint(-1, grid_height)
    obstacles[(rx, ry)] = rock



moving_direction = down

#############################
# Sub-Programs
###########################



# the function called when a key is pressed - sets direction variable
def checkKey(event):
    global moving_direction
    event.preventDefault()
    try:
        if event.key == 'w' and moving_direction == down:
            pass
        elif event.key == 'w':
            moving_direction = up
                
        elif event.key == 's' and moving_direction == up:
            pass
        elif event.key == 's': 
            moving_direction = down
            
        elif event.key == 'a' and moving_direction == right:
            pass
        elif event.key == 'a':
            moving_direction = left

        elif event.key == 'd' and moving_direction == left:
            pass
        elif event.key == 'd':
            moving_direction = right

    except AttributeError: 
        None

def getCell(x,y):
    return document.getElementById(f"R{y}C{x}")

# if the car has gone off the table, this tidies up including crash message
def handleCrash():
    crashed = True
    window.clearInterval(intervalHandle)
    document.getElementById("Message").innerText = "Oops you crashed..."

# called when the page is loaded to start the timer checks
def runGame():
    global intervalHandle
    print("Running Game")
    create_grid()
    print("Game Grid Created")
    document.addEventListener('keydown', checkKey)
    intervalHandle = window.setInterval(updatePosition, frame_rate)

#############################
# Main Program
#############################


def create_row(y):
    tr = document.createElement("tr")
    for x in range(grid_width):
        td = document.createElement("td")
        td.id = "R" + str(y) + "C" + str(x)
        if (x, y) in oranges:   
            td.className = orange
        elif (x, y) in obstacles:
            td.className = rock
        tr.appendChild(td)
        
    return tr

def create_grid():
    table = document.getElementById("RacingTrack")
    for y in range(grid_height):
        row = create_row(y)

        table.appendChild(row)

def find_current_head(snake):
    current_head = snake[-1] 
    (coordinates, _) = current_head  
    (current_head_x, current_head_y) = coordinates
    return (current_head_x, current_head_y, coordinates, current_head)

def find_next_head(delta):
    (current_head_x, current_head_y, coordinates, current_head)  = find_current_head(snake)
    (delta_x, delta_y) = delta
    next_head_x = current_head_x + delta_x
    next_head_y = current_head_y + delta_y
    new_head = ((next_head_x, next_head_y), delta)
    return (new_head, coordinates)
    

def move(snake, delta):
    (new_head, coordinates) = find_next_head(delta)
    ((head_x, head_y), head_direction) = new_head
    previous_body_direction = up
    snake_tail = snake[1]
    ((snake_tail_x, snake_tail_y),snake_tail_direction) = snake_tail
    current_tail_cell = getCell(snake_tail_x, snake_tail_y)
    (current_head_x, current_head_y, coordinates, current_head)  = find_current_head(snake)
    (new_head, coordinates) = find_next_head(delta)
    
    if coordinates in oranges:
        snake.append(new_head)
        oranges.pop(coordinates)
    elif current_head_x > grid_width or current_head_x < 1 or current_head_y > grid_height or current_head_y < 1:
        handleCrash()
    elif (head_x, head_y) in obstacles:
        handleCrash()

    else:
        ((prev_tail_x, prev_tail_y), _) = snake.pop(0)
        prev_tail_cell = getCell(prev_tail_x, prev_tail_y)
        if prev_tail_cell:
            prev_tail_cell.className = ""

            
        for ((x, y), current_body_direction) in snake:
            current_body_direction_index = snake.index(((x, y), current_body_direction))
            next_body_direction = head_direction
            if current_body_direction_index + 1 < len(snake):
                ((xx, yy), next_body_direction) = snake[current_body_direction_index + 1]
            body_cell = getCell(x,y)
            if body_cell:
                if current_body_direction != next_body_direction:
                    if current_body_direction == up and next_body_direction == left or current_body_direction == right and next_body_direction == down:
                        body_cell.className = Right_Down_turn
                    elif current_body_direction == up and next_body_direction == right or current_body_direction == left and next_body_direction == down:
                        body_cell.className = Left_Down_turn
                    elif current_body_direction == down and next_body_direction == left or current_body_direction == right and next_body_direction == up:
                        body_cell.className = Right_Up_turn
                    elif current_body_direction == down and next_body_direction == right or current_body_direction == left and next_body_direction== up:
                        body_cell.className = Left_Up_turn
                    
                elif current_body_direction == up or current_body_direction == down:
                    body_cell.className = snake_body_vertical
                else:
                    body_cell.className = snake_body_horizontal

            previous_body_direction = current_body_direction

        snake.append(new_head)
        head_cell = getCell(head_x, head_y)
        
       

        if head_cell:
            if head_direction == up:
                head_cell.className = snake_head_up
            elif head_direction == down:
                head_cell.className = snake_head_down
            elif head_direction == left:
                head_cell.className = snake_head_left
            else:
                head_cell.className = snake_head_right
        if current_tail_cell:
            if snake_tail_direction == up:
                current_tail_cell.className = tail_Up
            elif snake_tail_direction == down:
                 current_tail_cell.className = tail_Down
            elif snake_tail_direction == left:
                current_tail_cell.className = tail_Left
            else:
                current_tail_cell.className = tail_Right


def checkIfDuplicates_1(snake):
    if len(snake) == len(set(snake)):
        return False
    else:
        return True



def collision_check(snake, delta):
    (current_head_x, current_head_y, coordinates, current_head)  = find_current_head(snake)
    (new_head, coordinates) = find_next_head(delta)
    if current_head_x > grid_width-1 or current_head_x < 1 or current_head_y > grid_height -1 or current_head_y < 1:
        handleCrash()
    elif coordinates in obstacles:
        handleCrash()

def updatePosition():

    move(snake, moving_direction)
    collision_check(snake, moving_direction)
    
    
    
 
    
   

runGame()
