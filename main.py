import sys
import pygame
from asteroid import Asteroid
from constants import *
from logger import log_state
from player import Player
from asteroidfield import AsteroidField
from logger import log_event

def main():
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(x,y)
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable)
    astrofield = AsteroidField()

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    dt = 0.0

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        for asteroid_obj in asteroids:
           if asteroid_obj.collides_with(player):
               log_event("player_hit")
               print("Game over!")
               sys.exit()

        screen.fill("black")

        for drawables in drawable:
            drawables.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000







if __name__ == "__main__":
    main()
