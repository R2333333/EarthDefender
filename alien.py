import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """docstring for Alien."""

    def __init__(self, settings, screen):
        super().__init__()
        self.settings = settings
        self.screen = screen

        #load graph
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = 0
        self.rect.y = 0

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def check_edge(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
        else:
            return False

    def update(self):
        self.x += (self.settings.alien_speed_factor *
                        self.settings.fleet_direction)
        self.rect.x = self.x
