import pygame

class Ship():

    def __init__(self, settings, screen):
        self.screen = screen
        self.settings = settings

        #load the image of ship and get the rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.image = pygame.transform.scale(self.image, (90, 100))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #place the new ship at the bottom
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        #ship's status
        self.movingR = False
        self.movingL = False

    def blitme(self):
        # draw ship at position
        # blit_alpha(self.screen, self.image, self.rect, 128)
        
        self.screen.blit(self.image,self.rect)


    def update(self):
        if self.movingR and self.rect.right < self.screen_rect.right:
            self.center += self.settings.ship_speed_factor
        elif self.movingL and self.rect.left > self.screen_rect.left:
            self.center -= self.settings.ship_speed_factor

        self.rect.centerx = self.center
