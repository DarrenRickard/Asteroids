import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fpsClock = pygame.time.Clock()
    dt = 0 
    fps = 60
    while True:
        screen.fill("black")
        pygame.display.flip()
        dt = fpsClock.tick(fps) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


if __name__ == "__main__":
    main()
