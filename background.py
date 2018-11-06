import pygame
# import MarioClass from mario

class Background:
    def __init__(self):
        self.image = pygame.image.load('images/')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.mario_rect = self.mario.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.mario_moving_right = False

    def update(self):
        if self.mario_moving_right and self.mario_rect.centerx > self.rect.centerx:
            #scroll background

