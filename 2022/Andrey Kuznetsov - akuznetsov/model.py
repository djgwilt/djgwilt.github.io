import os
import time
import threading
from pynput import keyboard
from colorama import Fore
from pyfiglet import Figlet
from js import document, window

unnocupied_space = Fore.WHITE + '_'
snake_body = Fore.GREEN + '*'
apple = Fore.RED + '@'
border = Fore.BLUE + '+'
 

grid_width = 15
grid_height = 10
up = (0, -1)
down = (0, 1)
left = (-1, 0)
right = (1, 0)

frame_rate = 0.3

def game_over():
    os.system('cls')
    f = Figlet()
    print (f.renderText("Game Over"))
    quit()

def print_board(snake, apples):
    os.system('cls')
    for y in range(grid_height + 2):
        print_row(snake, apples, y)
        print()
    
        
def print_row(snake, apples, y):
    snake_dict = dict(snake) 
    for x in range(grid_width + 2):
        if y == 0 or y == grid_height + 1:
            print(border, end=" ")
        elif (x, y) in snake_dict:
            print(snake_dict[(x, y)], end=" ")
        elif (x, y) in apples:
            print(apples[x, y], end=" ")
        elif x == grid_width + 1 or x == 0:
            print(border,  end=" ")
        else:
            print(unnocupied_space, end=" ")


apples = { 
    (1, 5): apple, (4, 3): apple
    
}

snake = [
    ((7, 4), snake_body),
    ((7, 5), snake_body),
    ((7, 1), snake_body),
    ((7, 2), snake_body),
    ((7, 3), snake_body)
]

moving_direction = down

def find_current_head(snake):
    current_head = snake[-1] 
    (coordinates, snake_body) = current_head  
    (current_head_x, current_head_y) = coordinates
    return (current_head_x, current_head_y, coordinates, current_head)

def find_next_head(delta):
    (current_head_x, current_head_y, coordinates, current_head)  = find_current_head(snake)
    (delta_x, delta_y) = delta
    next_head_x = current_head_x + delta_x
    next_head_y = current_head_y + delta_y
    new_head = ((next_head_x, next_head_y), snake_body)
    return (new_head, coordinates)


def move(snake, delta):
    (new_head, coordinates) = find_next_head(delta)
    if coordinates in apples:
        snake.append(new_head)
        apples.pop(coordinates)
    else:
        snake.pop(0)
        snake.append(new_head)


def collision_check(snake, delta):
    (current_head_x, current_head_y, coordinates, current_head)  = find_current_head(snake)
    (new_head, coordinates) = find_next_head(delta)
    if current_head_x > grid_width or current_head_x < 1 or current_head_y > grid_height or current_head_y < 1:
        game_over() 
    

        
def on_key_pressed(key):
    global moving_direction
    try:
        if key.char == 'w' and moving_direction == down:
            pass
        elif key.char == 'w':
            moving_direction = up
                
        elif key.char == 's' and moving_direction == up:
            pass
        elif key.char == 's': 
            moving_direction = down
            
        elif key.char == 'a' and moving_direction == right:
            pass
        elif key.char == 'a':
            moving_direction = left

        elif key.char == 'd' and moving_direction == left:
            pass
        elif key.char == 'd':
            moving_direction = right

    except AttributeError: 
        None

def main():
    document.getElementById("Message").innerText = "this is main function"
    while True:
        collision_check(snake, moving_direction)
        move(snake, moving_direction)
        print_board(snake, apples)
        time.sleep(frame_rate)

th = threading.Thread(target=main)
th.start()

with keyboard.Listener(on_press=on_key_pressed) as listener:
    listener.join()

