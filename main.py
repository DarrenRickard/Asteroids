import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fpsClock = pygame.time.Clock()
    dt = 0 
    fps = 60
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable) 
    Shot.containers = (updatable, drawable, shots)

    # Initialize the player
    player = Player(x, y)
    field = AsteroidField()
    while True:
        screen.fill("black")
        # Update and draw all sprites
        updatable.update(dt)
        for sprite in drawable:
            sprite.draw(screen)
        # Check for collisions
        for asteroid in asteroids:
            if player.detect_collision(asteroid):
                print("Game over!")
                pygame.quit()
                return
        # Update display
        pygame.display.flip()
        dt = fpsClock.tick(fps) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


if __name__ == "__main__":
    main()
