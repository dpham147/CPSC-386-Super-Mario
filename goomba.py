import pygame
from pygame.sprite import Sprite
from timer import Timer


class Koopa(Sprite):
    def __init__(self, screen):
        super(Koopa, self).__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load('images/minion/koopa-1.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

        frames = [pygame.image.load('images/minion/koopa-1.png'),
                  pygame.image.load('images/minion/koopa-2.png')]
        self.koopa_moving_timer = Timer(frames)

        self.is_dead = False
        self.speed_factor = 1
        self.direction = -1  # -1 = left

    def update(self):
        self.x += (self.speed_factor * self.direction)
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)