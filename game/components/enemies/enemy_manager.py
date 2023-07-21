import random
import time
from game.components.enemies.enemy import Enemy


class EnemyManager:
    def __init__(self):
        self.enemies = []
        self.enemy_time = time.time()

    def update (self, game):
        self.add_enemy(game)
        for enemy in self.enemies:
            enemy.update(self.enemies, game)

    def draw (self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def add_enemy(self, game):
        #if len(self.enemies) < 1:
        if len(self.enemies) < 1 or (time.time() - self.enemy_time >= 2 and len(self.enemies) < 6):
            enemy = Enemy()
            self.enemies.append(enemy)
            self.enemy_time = time.time()

    def reset(self):
        self.enemies = []