import pygame
from eventloop import EventLoop
from background import Background
from mario import Mario
from scoreboard import Scoreboard
from stats import Stats


class Game:

    def __init__(self):
        # Init the display
        pygame.init()
        self.screen = pygame.display.set_mode((700, 400))
        pygame.display.set_caption("Super Mario")

        # Init audio
        pygame.mixer.init()
        pygame.mixer.set_num_channels(8)
        pygame.mixer.Channel(0).play(pygame.mixer.Sound('music/main_theme.ogg'), -1)

        # Create Mario
        self.mario = Mario(self.screen)

        # Create the level
        self.background = Background(self.screen, self.mario)

        # Create stats object
        self.stats = Stats()
        self.stats.reset()

        # Set scoreboard
        self.scoreboard = Scoreboard(self.screen, self.stats)

    def play(self):
        eloop = EventLoop(finished=False)
        while not eloop.finished:
            eloop.check_events(self.mario, self.background, self.stats)

            self.update_screen()

    def update_screen(self):
        self.screen.fill((0, 0, 0))
        self.background.blitme()
        self.mario.blitme()
        self.scoreboard.update()
        pygame.display.flip()


game = Game()
game.play()
