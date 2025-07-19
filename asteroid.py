import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "gray", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self, field):
        self.kill()  
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        # Split into two smaller asteroids
        random_angle = random.uniform(20, 50) 
        pos_velocity = self.velocity.rotate(random_angle)
        neg_velocity = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        field.spawn(new_radius, self.position, pos_velocity * 1.2)
        field.spawn(new_radius, self.position, neg_velocity * 1.2)