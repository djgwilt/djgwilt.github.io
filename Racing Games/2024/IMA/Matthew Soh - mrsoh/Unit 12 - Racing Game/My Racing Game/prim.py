import random
import matplotlib.pyplot as plt
import numpy as np
import time

def create_maze(width, height):
    maze = [['wall' for _ in range(width)] for _ in range(height)]
    start_x, start_y = (0, 0)
    maze[start_y][start_x] = 'car'
    
    walls = [(start_x,start_y)]
    visited = []
    while walls:
        x, y = random.choice(walls)
        walls.remove((x, y))
        
        if maze[y][x] == 'wall' or maze[y][x] == 'car':
            if maze[y][x] == 'wall':
                maze[y][x] = ''
            neighbors = [(x+dx, y+dy) for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]]
            random.shuffle(neighbors)
            for nx, ny in neighbors:
                if 0 <= nx < width and 0 <= ny < height and maze[ny][nx] == 'wall' and (nx,ny) not in visited:
                    if random.random() < 0.35:
                        maze[ny][nx] = ''
                        # visited.append((nx, ny))
                        # break
                    # maze[ny][nx] = ''
                    visited.append((nx, ny))
                    break
            for nx, ny in neighbors:
                if 0 <= nx < width and 0 <= ny < height and maze[ny][nx] == 'wall' and (nx,ny) not in visited:
                    walls.append((nx, ny))
        # display_maze(maze,stop = True)
        # time.sleep(1)
    
    return maze

def display_maze(maze, stop = False):
    print(maze)
    maze_np = np.array(maze)
    color_map = {'wall': 0, 'car': 1, '': 2}
    maze_np = np.vectorize(color_map.get)(maze_np)
    
    # Display the maze
    plt.imshow(maze_np, cmap='hot', interpolation='nearest')
    if stop:
        plt.draw()
        plt.pause(0.01)
    else:plt.show()

display_maze(create_maze(int(input()),int(input())))
print(create_maze(int(input()), int(input())))

# import random
# from PIL import Image

# class Maze:
#     def __init__(self, width, height):
#         self.grid = [['wall' for _ in range(width)] for _ in range(height)]
#         self.width = width
#         self.height = height

# def generate(maze):
#     def is_legal(x, y):
#         return 0 < x < maze.width - 1 and 0 < y < maze.height - 1

#     def frontier(x, y):
#         return [(nx, ny) for nx, ny in [(x-2, y), (x+2, y), (x, y-2), (x, y+2)] if is_legal(nx, ny) and maze.grid[ny][nx] == 'wall']

#     def neighbor(x, y):
#         return [(nx, ny) for nx, ny in [(x-2, y), (x+2, y), (x, y-2), (x, y+2)] if is_legal(nx, ny) and maze.grid[ny][nx] == '']

#     def random_cell():
#         return random.randint(0, maze.width - 1), random.randint(0, maze.height - 1)

#     def remove_at(index, lst):
#         return [item for i, item in enumerate(lst) if i != index]

#     def between(p1, p2):
#         dx = p2[0] - p1[0]
#         dy = p2[1] - p1[1]
#         x = p1[0] + dx // 2
#         y = p1[1] + dy // 2
#         return x, y

#     def connect_random_neighbor(x, y):
#         neighbors = neighbor(x, y)
#         picked_index = random.randint(0, len(neighbors) - 1)
#         xn, yn = neighbors[picked_index]
#         xb, yb = between((x, y), (xn, yn))
#         maze.grid[yb][xb] = ''

#     def extend(front):
#         while front:
#             picked_index = random.randint(0, len(front) - 1)
#             xf, yf = front[picked_index]
#             maze.grid[yf][xf] = ''
#             connect_random_neighbor(xf, yf)
#             front = remove_at(picked_index, front) + frontier(xf, yf)

#     x, y = random_cell()
#     maze.grid[y][x] = ''
#     extend(frontier(x, y))

#     return maze

# def render(maze):
#     cell_width = 10
#     cell_height = 10
#     pw = maze.width * cell_width
#     ph = maze.height * cell_height
#     img = Image.new('RGB', (pw, ph), "black")
#     pixels = img.load()

#     for y in range(maze.height):
#         for x in range(maze.width):
#             if maze.grid[y][x] == '':
#                 for dy in range(cell_height):
#                     for dx in range(cell_width):
#                         pixels[x*cell_width+dx, y*cell_height+dy] = (255, 255, 255)

#     img.save("maze.bmp")

# maze = Maze(int(input()), int(input()))
# maze = generate(maze)
# # print(maze.grid[1][1])
# display_maze(maze.grid)
# # render(maze)