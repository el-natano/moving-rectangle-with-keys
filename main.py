# Pygame game template

import pygame
import sys
import config  
import random
import shapes

def init_game():
    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))  
    pygame.display.set_caption(config.TITLE)
    return screen

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True

def draw_rectangle(screen, rect, color, thickness):
    """Draws a rectangle on the Pygame window."""
    pygame.draw.rect(screen, color, rect, thickness)


def main():

    screen = init_game()
    clock = pygame.time.Clock() 

    my_rect1 = [150, 250, 200, 150]
    thickness1 = 8 # Line thickness (width) in pixels



    

    running = True
    while running:
        running = handle_events()
        screen.fill(config.WHITE)  

        draw_rectangle(screen, my_rect1, config.RED, thickness)




        
        
    
        pygame.display.flip()

        clock.tick(config.FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
