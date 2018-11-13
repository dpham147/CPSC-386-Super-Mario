import pygame
class Stats:
    def __init__(self):
        self.reset()

    def reset(self):
        self.lives = 3
        self.coins = 0
        self.score = 0
        self.time = 400
        self.level = '1-1'

    def tick(self):
        if pygame.time.get_ticks() % 100 == 0:
            self.time -= 1
