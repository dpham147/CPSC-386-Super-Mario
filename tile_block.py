import pygame


class TileBlock:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('image/tile_block.png')
        self.screen_rect = self.screen.get_rect()
        self.rect = self.image.get_rect()

    def blitme(self):
        self.screen.blit(self.image, self.rect)
