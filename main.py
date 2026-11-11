import sys

import pygame

from logger import log_event,log_state
from constants import SCREEN_HEIGHT,SCREEN_WIDTH
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()


    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()



    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots,drawable, updatable)

    asterofield = AsteroidField()

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x,y)

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

            for shot_on_asteroid in shots:
                if shot_on_asteroid.collides_with(asteroid_obj):
                    log_event("asteroid_shot")
                    shot_on_asteroid.kill()
                    asteroid_obj.split()

        screen.fill("black")

        for drawables in drawable:
            drawables.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000







if __name__ == "__main__":
    main()
