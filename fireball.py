import pygame
from pygame.sprite import Sprite
from vector import Vector
from timer import Timer


class Fireball(Sprite):
    def __init__(self, mario, screen):
        super(Fireball, self).__init__()

        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.mario = mario

        self.timetolive = 500

        frames = [pygame.image.load('images/fire-1.png'),
                  pygame.image.load('images/fire-2.png'),
                  pygame.image.load('images/fire-3.png'),
                  pygame.image.load('images/fire-4.png')]

        self.images = Timer(frames)

        self.image = self.images.imagerect()
        self.rect = self.image.get_rect()

        self.rect.centery = float(mario.rect.centery)

        if mario.face_right:
            self.rect.left = mario.rect.right
            self.vector = Vector(1.4, 1)
        else:
            self.rect.right = mario.rect.left
            self.vector = Vector(-1.4, 1)

    def update(self):
        # Update position
        self.rect.centerx += self.vector.x
        self.rect.centery += self.vector.y

        self.vector.y += .1
        self.vector.y = min(2, self.vector.y)
        self.vector.y = max(-2, self.vector.y)

        # Account for ground
        if self.rect.bottom >= self.screen_rect.centery:
            self.vector.y = -self.vector.y

        self.timetolive -= 1

    def blitme(self):
        self.screen.blit(self.image, self.rect)


