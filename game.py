import pygame
from eventloop import EventLoop
from background import Background


class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(pygame.FULLSCREEN)
        pygame.display.set_caption("Super Mario")

    def play(self):
        eloop = EventLoop(finished=False)

    def update_screen(self):
        self.screen.fill(0, 0, 0)
        self.background.blitme()
