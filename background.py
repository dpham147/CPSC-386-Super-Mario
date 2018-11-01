import pygame
import MarioClass from mario

class Background:
    def __init__(self):
        self.image = pygame.image.load("'/images/1-1.png")
        self.rect = self.image.rect
        self.centerx = self.rect.x
        self.centery = self.rect.y