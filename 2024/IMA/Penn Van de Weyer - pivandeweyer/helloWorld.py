# write me a program that will detect key presses and display them on the screen
# when the user presses the 'q' key, the program should quit
# when the user presses the 'c' key, the program should clear the screen

import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((400, 400))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
            if event.key == pygame.K_c:
                screen.fill((0, 0, 0))
            print(pygame.key.name(event.key))  # Print the name of the key
        if event.type == pygame.KEYUP:
            print(pygame.key.name(event.key))  # Print the name of the key
    pygame.display.flip()


# Path: helloWorld.py
# write me a program that will detect key presses and display them on the screen