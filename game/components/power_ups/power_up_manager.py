import random

import pygame
from game.components.power_ups.bomb import Bomb
from game.components.power_ups.more_bullets import MoreBullets
from game.components.power_ups.shield import Shield
from game.components.power_ups.heart import Heart
from game.components.power_ups.mini_AND_speed import MiniSpeed

from game.utils.constants import HEART, SPACESHIP, SPACESHIP_SHIELD, SPACESHIP_SMALL


class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.duration = random.randint(3, 5)
        self.when_appears = random.randint(5000, 10000)

    def update(self, game):
        current_time = pygame.time.get_ticks()

        if len(self.power_ups) == 0 and current_time >= self.when_appears:
            self.generate_power_up(game)
        
        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)

            if game.player.rect.colliderect(power_up.rect):
                if power_up.type == 'heart':
                    game.player.power_up_type = power_up.type
                    game.player.has_power_up = True
                    self.power_ups.remove(power_up)
                
                elif power_up.type == 'shield':
                    power_up.start_time = pygame.time.get_ticks()
                    game.player.power_up_type = power_up.type
                    game.player.has_power_up = True
                    game.player.power_time_up = power_up.start_time + (self.duration * 1000)
                    game.player.set_image((65, 75), SPACESHIP_SHIELD)
                    self.power_ups.remove(power_up)

                elif power_up.type == 'burst':
                    power_up.start_time = pygame.time.get_ticks()
                    game.player.power_up_type = power_up.type
                    game.player.has_power_up = True
                    game.player.power_time_up = power_up.start_time + (self.duration * 1000)
                    self.power_ups.remove(power_up)
                    
                elif power_up.type == 'mini_AND_speed':
                    power_up.start_time = pygame.time.get_ticks()
                    game.player.power_up_type = power_up.type
                    game.player.has_power_up = True
                    game.player.power_time_up = power_up.start_time + (self.duration * 1000)
                    game.player.set_image((30, 30), SPACESHIP_SMALL)
                    self.power_ups.remove(power_up)

                elif power_up.type == 'bomb':
                    game.player.power_up_type = power_up.type
                    game.player.has_power_up = True
                    self.power_ups.remove(power_up)
                    enemies_to_remove = []
                    for enemy in game.enemy_manager.enemies:
                        enemies_to_remove.append(enemy)
                        
                    for enemy in enemies_to_remove:
                        game.enemy_manager.enemies.remove(enemy)


    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def generate_power_up(self, game):
        list_power_ups = [Shield(), MoreBullets(), Heart(), MiniSpeed(), Bomb()]
        power_up = list_power_ups[random.randint(0,4)]
        self.when_appears += random.randint(5000, 10000)
        self.power_ups.append(power_up)

    def reset(self):
        self.power_ups = []