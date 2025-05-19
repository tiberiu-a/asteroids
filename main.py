import pygame

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField()
    clock = pygame.time.Clock()
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for obj in updatable:
            obj.update(dt)
        for obj in drawable:
            obj.draw(screen)
        for obj in asteroids:
            if obj.collisions(player):
               print("Game over!")
               exit()
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()