from game.components.power_ups.power_up import PowerUp
from game.utils.constants import EXPLOSION, BOMB_TYPE

class Bomb(PowerUp):
    def __init__(self):
        super().__init__(EXPLOSION, BOMB_TYPE)