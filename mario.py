import pygame
from pygame.sprite import Sprite
from vector import Vector


class Mario(Sprite):
    def __init__(self, screen):
        super(Mario, self).__init__()
        #self.timer = Timer(frames)
        self.image = pygame.image.load('images/mario/small-1.png')
        self.rect = self.image.get_rect()
        self.screen = screen

        self.mv_left = False
        self.mv_right = False

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.vector = Vector(0, 0)

        self.is_super = False
        self.is_fire = False

    def get_rect(self):
        return self.rect

    def update(self):
        if self.mv_left:
            self.vector.x -= 10
        elif self.mv_right:
            self.vector.y += 10
        self.x += self.vector.x
        self.y += self.vector.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def jump(self):
        pass

    def fire(self):
        if self.is_fire:
            pass
