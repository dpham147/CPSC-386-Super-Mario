import pygame
from pygame.sprite import Sprite
from timer import Timer


class Koopa(Sprite):
    def __init__(self, screen):
        super(Koopa, self).__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load('image/minion/koopa-1.png')
        self.rect = self.image.get_rect()

        frames = [pygame.image.load('image/minion/koopa-1.png'),
                  pygame.image.load('image/minion/koopa-2.png')]
        self.koopa_moving_timer = Timer(frames)


    def blitme(self):
        self.screen.blit(self.image, self.rect)