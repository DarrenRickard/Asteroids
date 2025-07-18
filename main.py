import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fpsClock = pygame.time.Clock()
    dt = 0 
    fps = 60
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    # Initialize the player
    player = Player(x, y)
    while True:
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
        dt = fpsClock.tick(fps) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


if __name__ == "__main__":
    main()
