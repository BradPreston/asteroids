# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(
        x = SCREEN_WIDTH / 2,
        y = SCREEN_HEIGHT / 2
    )
    asteroid = Asteroid(
        x = 0,
        y = 0,
        radius = 2
    )
    asteroidField = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        asteroids.update(dt)
        shots.update(dt)
        for asteroid in asteroids:
            for shot in shots:
                if shot.isColliding(asteroid):
                    shot.kill()
                    asteroid.split()
            if player.isColliding(asteroid):
                print("Game over!")
                sys.exit(0)

        for d in drawable:
            d.draw(screen)
        pygame.display.flip()
        timePassedInMS = clock.tick(60)
        dt = timePassedInMS / 1000 # convert MS to seconds


if __name__ == "__main__":
    main()
