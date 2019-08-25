import sys
import pygame

def run_game():
    
    pygame.init()

    pygame.display.init()

    screen = pygame.display.set_mode((800, 400))
    
    pygame.display.set_caption("Alien Invasion")

    while True:
        for event in pygame.event.get():

            if event.type == pygame.quit():
                sys.exit()

        pygame.display.flip()


run_game()

