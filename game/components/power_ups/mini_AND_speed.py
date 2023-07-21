from game.components.power_ups.power_up import PowerUp
from game.utils.constants import SPACESHIP, MINI_SPEED_TYPE

class MiniSpeed(PowerUp):
    def __init__(self):
        super().__init__(SPACESHIP, MINI_SPEED_TYPE)