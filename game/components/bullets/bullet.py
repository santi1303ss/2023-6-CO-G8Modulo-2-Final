import pygame
from pygame.sprite import Sprite

from game.utils.constants import BULLET, BULLET_ENEMY, SCREEN_HEIGHT, SHOOT_SOUND


class Bullet(Sprite):
    BULLET_SIZE = pygame.transform.scale(BULLET, (15,20))
    BULLET_ENEMY_SIZE = pygame.transform.scale(BULLET_ENEMY, (15,20))
    BULLETS = {'player': BULLET_SIZE, 'enemy': BULLET_ENEMY_SIZE}
    SPEED = 20

    def __init__(self, spaceshift):
        self.image = self.BULLETS[spaceshift.type]
        self.rect = self.image.get_rect()
        self.rect.center = spaceshift.rect.center
        self.owner = spaceshift.type
    
    #TODO Power doble cañon

    def update(self, bullets):
        if self.owner == 'enemy':
            self.rect.y += self.SPEED
            if self.rect.y>= SCREEN_HEIGHT:
                if self in bullets:
                    bullets.remove(self)
        else:
            self.rect.y -= self.SPEED
            if self.rect.y<= 0:
                if self in bullets:
                    bullets.remove(self)

    def draw (self, screen):
        screen.blit(self.image,(self.rect.x, self.rect.y))