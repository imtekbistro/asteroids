from circleshape import *
from constants import *
import random
import pygame

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        rnd_ang = random.uniform(20, 50)
        split1_vect = self.velocity.rotate(rnd_ang)
        split2_vect = self.velocity.rotate(-rnd_ang)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        split1 = Asteroid(self.position.x, self.position.y, new_radius)
        split1.velocity = split1_vect * 1.2
        split2 = Asteroid(self.position.x, self.position.y, new_radius)
        split2.velocity = split2_vect * 1.2


    
