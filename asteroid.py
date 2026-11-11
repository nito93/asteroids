import pygame
import random
from logger import log_event
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH



class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,LINE_WIDTH)

    def update(self,dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        safe_random = random.uniform(20,50)
        new_vector_split_asteroids = self.velocity.rotate(safe_random)
        new_vector_split_asteroids_opposite = self.velocity.rotate(-1 * safe_random)

        new_radius_split_asteroids = self.radius - ASTEROID_MIN_RADIUS

        asteroid_split_one = Asteroid(self.position.x,self.position.y,new_radius_split_asteroids)
        asteroid_split_one.velocity = new_vector_split_asteroids * 1.2

        asteroid_split_two = Asteroid(self.position.x,self.position.y,new_radius_split_asteroids)
        asteroid_split_two.velocity = new_vector_split_asteroids_opposite * 1.2
