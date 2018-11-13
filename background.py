import pygame


class Background:
    def __init__(self, screen, mario):
        self.screen = screen
        self.mario = mario
        self.screen_rect = self.screen.get_rect()
        self.mario_rect = self.mario.get_rect()

        self.reload()

    def update(self):
        if self.mario.mv_right and self.mario_rect.centerx > self.rect.centerx:
            self.rect.left -= self.mario.vector.x
        if self.mario.mv_left and self.mario_rect.centerx < self.rect.centerx:
            self.rect.left += self.mario.vector.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def reload(self):
        self.image = pygame.image.load('images/background.png')
        self.rect = self.image.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)

        self.rect.top = self.screen_rect.top
        self.rect.left = self.screen_rect.left
