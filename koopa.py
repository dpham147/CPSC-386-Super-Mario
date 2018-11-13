import pygame
from pygame.sprite import Sprite
from timer import Timer


class Goomba(Sprite):
    def __init__(self, screen):
        super(Goomba, self).__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load('image/minion/goomba-1.png')
        self.rect = self.image.get_rect()

        frames = [pygame.image.load('image/minion/goomba-1.png'),
                  pygame.image.load('image/minion/goomba-2.png')]
        self.goomba_moving_timer = Timer(frames)


    def blitme(self):
        self.screen.blit(self.image, self.rect)