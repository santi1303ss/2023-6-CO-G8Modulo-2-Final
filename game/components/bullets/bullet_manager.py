import pygame

from game.utils.constants import BULLETS_TYPE, DEFAULT_TYPE, HEART_TYPE, SHIELD_TYPE, SHOOT_SOUND

class BulletManager:
    def __init__(self):
        self.bullets = []
        self.enemy_bullets = []
        #self.score = 0

    def update (self, game):

        for bullet in self.bullets:
            bullet.update(self.bullets)

            for enemy in game.enemy_manager.enemies:
                if bullet.rect.colliderect(enemy.rect) and bullet.owner == 'player':
                    game.score += 10
                    game.soundShip.play()
                    game.soundShip.set_volume(0.1)
                    game.enemy_manager.enemies.remove(enemy)
                    if bullet in self.enemy_bullets:
                        self.bullets.remove(bullet)
                        
        for bullet in self.enemy_bullets:
            for enemy in self.enemy_bullets:
                bullet.update(self.enemy_bullets)
            if bullet.rect.colliderect(game.player.rect) and bullet.owner == 'enemy':
                if game.player.power_up_type == HEART_TYPE:
                    if bullet.rect.colliderect(game.player.rect) and bullet.owner == 'enemy':
                        game.player_has_power_up = False
                        game.player.power_up_type = DEFAULT_TYPE       
                elif game.player.power_up_type != SHIELD_TYPE and game.player.power_up_type != HEART_TYPE: 
                    game.sound.play()
                    game.sound.set_volume(0.1)
                    #game.score += 1
                    game.death_count += 1
                    game.playing = False
                    pygame.time.delay(1000)
                    break
                self.enemy_bullets.remove(bullet)
                
    def draw (self, screen):
        for bullet in self.bullets:
            bullet.draw(screen)
        for bullet in self.enemy_bullets:
            bullet.draw(screen)
    def add_bullet(self, bullet, game):
        if bullet.owner == 'player':
            if game.player.power_up_type != BULLETS_TYPE:   
                if len(self.bullets) < 3:
                    #pygame.mixer.Sound(SHOOT_SOUND)
                    self.bullets.append(bullet)
                    #TODO logica cañon doble
            else:
                if len(self.bullets) < 100:
                    self.bullets.append(bullet)
        elif bullet.owner == 'enemy' and len(self.enemy_bullets) < 3:
            self.enemy_bullets.append(bullet)
            
    def reset(self):
        self.bullets = []
        self.enemy_bullets = []