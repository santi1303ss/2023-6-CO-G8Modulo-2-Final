import pygame
from game.utils.constants import FONT_STYLE1, SCREEN_HEIGHT, SCREEN_WIDTH, WALLPAPER, WALLPAPER2



class Menu:
    HALF_SCREEN_WIDTH = SCREEN_WIDTH // 2
    HALF_SCREEN_HEIGHT = SCREEN_HEIGHT //2

    def __init__(self, message, message_2, message_3, screen):
        screen.fill((255, 255, 255))
        self.font = pygame.font.Font(FONT_STYLE1, 30)
        self.text = self.font.render(message, True, (0,0,0))
        self.text_rect = self.text.get_rect()
        self.text_rect = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 100)
        self.text_2 = self.font.render(message_2, True, (0,0,0))
        self.text_rect_2 = self.text_2.get_rect()
        self.text_rect_2 = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 200)
        self.text_3 = self.font.render(message_3, True, (0,0,0))
        self.text_rect_3 = self.text_3.get_rect()
        self.text_rect_3 = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 300)
        self.wallpaper = pygame.transform.scale (WALLPAPER, (SCREEN_WIDTH, SCREEN_HEIGHT))

    def update(self, game):
        pygame.display.update()
        self.handle_events_on_menu(game)

    def draw (self, screen, game):
        screen.blit(self.wallpaper, (0, 0))
        screen.blit(self.text, self.text_rect)
        screen.blit(self.text_2, self.text_rect_2)
        screen.blit(self.text_3, self.text_rect_3)

    def handle_events_on_menu(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.playing = False
                game.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game.run()

    def reset_screen_color(self, screen):
        screen.fill((255, 255, 255))

    def update_message(self, message, message_2, message_3):
        self.text = self.font.render(message, True, (255,255,255))
        self.text_rect = self.text.get_rect()
        self.text_rect = (self.HALF_SCREEN_WIDTH - 200, self.HALF_SCREEN_HEIGHT - 80)
        self.text_2 = self.font.render(message_2, True, (255,255,255))
        self.text_rect_2 = self.text_2.get_rect()
        self.text_rect_2 = (self.HALF_SCREEN_WIDTH - 200, self.HALF_SCREEN_HEIGHT + 27)
        self.text_3 = self.font.render(message_3, True, (255,255,255))
        self.text_rect_3 = self.text_3.get_rect()
        self.text_rect_3 = (self.HALF_SCREEN_WIDTH - 200, self.HALF_SCREEN_HEIGHT + 130)
        self.wallpaper = pygame.transform.scale (WALLPAPER2, (SCREEN_WIDTH, SCREEN_HEIGHT))