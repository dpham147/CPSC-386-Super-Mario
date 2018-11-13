import pygame
from pygame.sprite import Sprite


class Floor(Sprite):
    def __init__(self, screen):
        super(Floor, self).__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load('images/floor.png')
        self.rect = self.image.get_rect()

    def blitme(self):
        self.screen.blit(self.image, self.rect)