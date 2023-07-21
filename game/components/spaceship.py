import pygame
from pygame.sprite import Sprite
from game.components.bullets.bullet import Bullet
from game.utils.constants import (
    DEFAULT_TYPE,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    SPACESHIP,
    ADDRESS_SOUND,
    SHOOT_SOUND,
)


class Spaceship(Sprite):
    SHIP_WIDTH = 40
    SHIP_HEIGHT = 60
    X_POS = (SCREEN_WIDTH // 2) - SHIP_WIDTH
    Y_POS = 500
    SHIP_SPEED = 10
    LIMIT_Y = 300

    def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(
            self.image, (self.SHIP_WIDTH, self.SHIP_HEIGHT)
        )
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.type = "player"
        self.power_up_type = DEFAULT_TYPE
        self.has_power_up = False
        self.power_time_up = 0

    def update(self, user_input, game):
        if user_input[pygame.K_a] or user_input[pygame.K_LEFT]:
            self.move_left()
        if user_input[pygame.K_d] or user_input[pygame.K_RIGHT]:
            self.move_right()
        if user_input[pygame.K_w] or user_input[pygame.K_UP]:
            self.move_up()
        if user_input[pygame.K_s] or user_input[pygame.K_DOWN]:
            self.move_down()
        if user_input[pygame.K_SPACE]:
            #pygame.mixer.Sound(SHOOT_SOUND)
            self.shoot(game)


        if self.has_power_up and self.power_up_type == "mini_AND_speed":
            current_time = pygame.time.get_ticks()
            if current_time >= self.power_time_up:
                self.set_image((self.SHIP_WIDTH, self.SHIP_HEIGHT), SPACESHIP)
                self.has_power_up = False
                self.power_up_type = DEFAULT_TYPE
                
                self.SHIP_SPEED = 10
            else:
                self.SHIP_SPEED = 30
        else:
            self.SHIP_SPEED = 10

    def move_left(self):
        self.rect.x -= self.SHIP_SPEED
        pygame.mixer.Sound(ADDRESS_SOUND).play
        self.display_limit()
        

    def move_right(self):
        self.rect.x += self.SHIP_SPEED
        pygame.mixer.Sound(ADDRESS_SOUND).play
        self.display_limit()

    def move_up(self):
        self.rect.y -= self.SHIP_SPEED
        self.display_limit()

    def move_down(self):
        self.rect.y += self.SHIP_SPEED
        self.display_limit()

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def display_limit(self):
        if self.rect.x < 0:  # Limite izquierdo
            self.rect.x = SCREEN_WIDTH  # Reaparece lado derecho
            pygame.mixer.Sound(ADDRESS_SOUND).play()
        if self.rect.x > SCREEN_WIDTH:  # Limite derecho
            self.rect.x = 0  # Reaparece lado izquierdo
            pygame.mixer.Sound(ADDRESS_SOUND).play()

        if self.rect.y < self.LIMIT_Y:  # Limite de Y
            self.rect.y = self.LIMIT_Y  # Mantiene la posición
        if self.rect.y > SCREEN_HEIGHT - self.SHIP_HEIGHT:
            self.rect.y = SCREEN_HEIGHT - self.SHIP_HEIGHT

    def shoot(self, game):
        bullet = Bullet(self)
        game.bullet_manager.add_bullet(bullet, game)

    def set_image(self, size=(SHIP_WIDTH, SHIP_HEIGHT), image=SPACESHIP):
        self.image = image
        self.image = pygame.transform.scale(self.image, size)
