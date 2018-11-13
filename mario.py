import pygame
from pygame.sprite import Sprite
from vector import Vector
from timer import Timer


class Mario(Sprite):
    def __init__(self, screen):
        super(Mario, self).__init__()

        # Set Small Mario Animation Frames
        self.small_image = pygame.image.load('images/mario/small-1.png')

        frames = [pygame.image.load('images/mario/small-1.png'),
                  pygame.image.load('images/mario/small-2.png'),
                  pygame.image.load('images/mario/small-3.png'),
                  pygame.image.load('images/mario/small-4.png'),
                  pygame.image.load('images/mario/small-5.png'),
                  pygame.image.load('images/mario/small-6.png')]
        self.small_right_timer = Timer(frames)

        self.image = self.small_image
        self.rect = self.small_image.get_rect()

        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.mv_left = False
        self.mv_right = False

        self.rect.left = self.screen_rect.left
        self.rect.centery = self.screen_rect.centery

        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        self.vector = Vector(0, 0)

        self.is_star = False
        self.star_timer = 1000
        self.is_super = False
        self.is_fire = False
        self.is_crouch = False

    def get_rect(self):
        return self.rect

    def update(self, background):
        # Handle X Movement
        if self.mv_left:
            self.vector.x = max(self.vector.x - .1, -1.5)
            background.rect.left -= min(0, abs(self.vector.x))
            self.image = pygame.transform.flip(self.small_right_timer.imagerect(), True, False)
        elif self.mv_right:
            self.vector.x = min(self.vector.x + .1, 1.5)
            background.rect.right -= min(background.rect.right, abs(self.vector.x))
            self.image = self.small_right_timer.imagerect()
        else:
            self.vector.x = 0
        self.rect.centerx = max(self.rect.centerx + self.vector.x, 0)

        # Handle Y Movement
        self.rect.centery += self.vector.y
        # print('Mario Pos: (' + str(self.rect.centerx) + ', ' + str(self.rect.centery))

        # Handle sprite changes
        if self.is_fire:
            if self.is_crouch:
                pass
               # self.rect = self.fire_rect_crouch
            else:
                pass
               # self.rect = self.fire_rect
        elif self.is_super:
            if self.is_crouch:
                pass
               # self.rect = self.super_rect_crouch
            else:
                pass
               # self.rect = self.super_rect
        else:
            pass
           # self.rect = self.small_rect

        # Handle invincibility timer
        if self.is_star:
            self.star_timer -= 1
            if self.star_timer == 0:
                pygame.mixer.Channel(7).stop()
                pygame.mixer.Channel(0).unpause()
                self.is_star = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def jump(self):
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('sound/small_jump.ogg'))

    def fire(self):
        if self.is_fire:
            pygame.mixer.Channel(2).play(pygame.mixer.Sound('sound/fireball.ogg'))

    def star(self):
        self.star_timer = 1000
        self.is_star = True
        pygame.mixer.Channel(0).pause()
        pygame.mixer.Channel(7).play(pygame.mixer.Sound('music/invincible.ogg'))


