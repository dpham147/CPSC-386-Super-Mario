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
        self.screen_rect = self.screen.get_rect()

        self.mv_left = False
        self.mv_right = False

        self.rect.left = self.screen_rect.left
        self.rect.centery = self.screen_rect.centery

        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        self.vector = Vector(0, 0)

        self.is_super = False
        self.is_fire = False
        self.is_crouch = False

    def get_rect(self):
        return self.rect

    def update(self):
        # Handle X Movement
        if self.mv_left:
            self.vector.x = max(self.vector.x - .1, -1.5)
            print('Moving X left: ' + str(self.vector.x))
        elif self.mv_right:
            self.vector.x = min(self.vector.x + .1, 1.5)
            print('Moving X right: ' + str(self.vector.x))
        else:
            self.vector.x = 0
        self.rect.centerx = max(self.rect.centerx + self.vector.x, 0)

        self.rect.centery += self.vector.y

        # print('Mario Pos: (' + str(self.rect.centerx) + ', ' + str(self.rect.centery))

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def jump(self):
        pass

    def fire(self):
        if self.is_fire:
            pass
