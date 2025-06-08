import pygame, random
from constants import SHOT_RADIUS, ASTEROID_MIN_RADIUS
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x , y, radius, updatables, drawables, asteroids_group):
        super().__init__(x, y, radius)
        self.updatables = updatables
        self.drawables = drawables
        self.asteroids_group = asteroids_group
        self.updatables.add(self)
        self.drawables.add(self)
        self.asteroids_group.add(self)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            asteroid1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS, self.updatables, self.drawables,self.asteroids_group)
            asteroid1.velocity = self.velocity.rotate(random_angle) * 1.2
            asteroid2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS, self.updatables, self.drawables, self.asteroids_group)
            asteroid2.velocity = self.velocity.rotate(-random_angle) * 1.2
       
class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.radius = SHOT_RADIUS
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += (self.velocity * dt)
