import pygame
import os

pygame.init()
pygame.mixer.init()

# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 60
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")
SOUND_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")
TEXT_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants

#Background
BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track13.webp'))
BG2 = pygame.image.load(os.path.join(IMG_DIR, 'Other/Parallax2.png'))
BG3 = pygame.image.load(os.path.join(IMG_DIR, 'Other/Parallax3.png'))

ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

OVER = pygame.image.load(os.path.join(IMG_DIR, 'Other/GameOver.png'))
EXPLOSION = pygame.image.load(os.path.join(IMG_DIR, 'Other/Explosion.png'))
BULLETS = pygame.image.load(os.path.join(IMG_DIR, 'Other/Bullets.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/Heart.png'))

#Star and game over
WALLPAPER = pygame.image.load(os.path.join(IMG_DIR, 'Other/Wallpaper.png'))
WALLPAPER2 = pygame.image.load(os.path.join(IMG_DIR, 'Other/Wallpaper2.png'))


#SKINS PLAYER
SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
SPACESHIP_SMALL = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_small.png"))

#Bullets
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))
BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_4.png"))
INNER_SHIP_BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_4.png")) #Burger_bullet

#SKIN ENEMIES
ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))#One
ENEMY_2 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png"))#Two
ENEMY_3 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_5.png"))#brother of Boliver
ENEMY_4 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_3.png"))#Ovni


#Fuentes
FONT_STYLE = os.path.join(TEXT_DIR, 'Other/fuente_1.ttf')
FONT_STYLE1 = os.path.join(TEXT_DIR, 'Other/fuente_2.ttf')
FONT_STYLE2 = os.path.join(TEXT_DIR, 'Other/fuente_3.otf')

#power_ups
DEFAULT_TYPE = "default"
MINI_SPEED_TYPE = 'mini_AND_speed'
SHIELD_TYPE = 'shield'
HEART_TYPE = 'heart'
BOMB_TYPE = 'bomb'
BULLETS_TYPE = 'burst'

#Sonidos
BACKGROUND_MUSIC = os.path.join(SOUND_DIR, 'sounds/background.mp3')
ADDRESS_SOUND = os.path.join(SOUND_DIR, 'sounds/passLite.mp3')
SHOOT_SOUND = os.path.join(SOUND_DIR, 'sounds/shoot_sound.wav')
EXPLOSION_SOUND = os.path.join(SOUND_DIR, 'sounds/invaderkilled.wav')
BACK_SOUND = os.path.join(SOUND_DIR, 'sounds/back.mp3')