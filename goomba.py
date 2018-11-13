import pygame


class Goomba:
    def __init__(self, screen, mario):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.mario = mario
        self.mario_rect = self.mario.get_rect()
        self.image = pygame.image.load('image')