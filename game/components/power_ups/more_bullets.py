from game.components.power_ups.power_up import PowerUp
from game.utils.constants import BULLETS, BULLETS_TYPE, EXPLOSION

class MoreBullets(PowerUp):
    def __init__(self):
        super().__init__(BULLETS, BULLETS_TYPE)
    