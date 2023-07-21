import math
import pygame
from game.components.enemies.enemy import Enemy
from game.utils.constants import ENEMY_3, SCREEN_HEIGHT, SCREEN_WIDTH, BULLET_ENEMY_TYPE

class Ovni(Enemy):
    WIDTH = 60
    HEIGHT = 60
    SPEED = 20
    SHOOTING_TIME = 600

    def __init__(self):
        self.image = OVNI
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image)
        self.is_alive = True
        self.shooting_time = 0
        self.current_angle = 0
        self.radius = 50
        self.radius_increment = 1 
        self.center_x = 550
        self.center_y = 100

    def update(self, bullet_manager):
        if self.rect.y >= SCREEN_HEIGHT or self.rect.x >= SCREEN_WIDTH:
            self.is_alive = False

        self.shooting_time += 1
        self.move()
        self.shoot(bullet_manager)

    def move(self):
        self.current_angle += math.radians(self.SPEED)
        self.radius += self.radius_increment
        self.rect.x = self.center_x + self.radius * math.cos(self.current_angle)
        self.rect.y = self.center_y + self.radius * math.sin(self.current_angle)

    def shoot(self, bullet_manager):
        if self.shooting_time % self.SHOOTING_TIME == 0:
            bullet_manager.add_bullet(BULLET_ENEMY_TYPE, self.rect.center)
