from circleshape import CircleShape
import pygame
from constants import *
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(surface=screen, color='crimson', center=self.position, radius=self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20.0, 50.0)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            v1 = self.velocity.rotate(angle)
            v2 = self.velocity.rotate(-angle)

            split1 = Asteroid(self.position[0],self.position[1],new_radius)
            split2 = Asteroid(self.position[0],self.position[1],new_radius)

            split1.velocity = v1*1.2
            split2.velocity = v2*1.2





