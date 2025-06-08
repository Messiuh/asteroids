import pygame
from constants import *
from player import Player
from asteroid import Asteroid, Shot
from asteroidfield import AsteroidField

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()
    shot_group = pygame.sprite.Group()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, updatables, drawables, shot_group)
    updatables.add(player)
    drawables.add(player)
    Player.containers = (updatables, drawables)
    Asteroid.containers = (updatables, drawables, asteroids_group)
    AsteroidField.containers = (updatables)
    Shot.containers = (updatables, drawables, shot_group)
    asteroid_field = AsteroidField(updatables, drawables, asteroids_group)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        updatables.update(dt)
        for drawable in drawables:
            drawable.draw(screen)
        pygame.display.update()
        for asteroid in asteroids_group:
            if player.collide(asteroid):
                print("Game Over!")
                raise SystemExit
        for asteroid in asteroids_group:
            for shot in shot_group:
                if asteroid.collide(shot):
                    asteroid.split()
                    asteroid.kill()
                    shot.kill()
        dt = clock.tick(60) / 1000
        
        
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()