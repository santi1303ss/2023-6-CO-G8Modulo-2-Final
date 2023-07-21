import pygame 
from game.components.enemies.enemy import Enemy
from game.utils.constants import BULLET_INNER_SHIP_TYPE, ENEMY_4

class InnerShip (Enemy):
    WIDTH = 60
    HEIGHT = 60
    SPEED_Y = 40
    SHOOTING_TIME = 15
    
    def __init__(self):
        self.image = ENEMY_4
        self.image = pygame.transform.scale(self.image, (self.HEIGHT, self.WIDTH))
        super().__init__()
        
    def move (self):
        self.rect.y += self.SPEED_Y
        
    def shoot(self, bullet_manager):
        current_time = pygame.time.get_ticks()
        round_time = round((self.shooting_time - current_time) / 1000)
        if round_time <= 0:
            bullet_manager.add_bullet(BULLET_INNER_SHIP_TYPE, self.rect.center)
            self.shooting_time = current_time + 2000
                                                    #Tipo  | lugar
                                                