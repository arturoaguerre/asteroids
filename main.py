import pygame
from player import Player
from asteroid import Asteroid
from constants import *
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)


    Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField()

    dt = 0
    
    print("Starting asteroids!")
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)

        screen.fill((0, 0, 0))

        for drawing in drawable:     
            drawing.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
