import pygame
from imagerect import ImageRect


class Background:

    BRICK_SIZE = 16

    def __init__(self, screen, mario):
        self.screen = screen
        self.mario = mario

        self.filename = 'levels/1-1.txt'
        with open(self.filename, 'r') as f:
            self.rows = f.readlines()

        self.floor = []
        self.coins = []
        self.breakables = []
        self.unbreakables = []
        self.question = []
        self.pipes = []
        self.goombas = []

        sz = Background.BRICK_SIZE

        self.brick = ImageRect(screen, 'floor-150x150', sz, sz)
        self.coin = ImageRect(screen, 'items/coin-1', sz, sz)
        self.breakable = ImageRect(screen, 'bricks/brick_initial', sz, sz)
        self.unbreakable = ImageRect(screen, 'bricks/brick_initial', sz, sz)
        self.question_brick = ImageRect(screen, 'question_block/question_block_initial-1', sz, sz)
        self.pipe = ImageRect(screen, 'bricks/brick_initial', sz, sz)
        self.goomba = ImageRect(screen, 'minions/goomba-1', sz, sz)

        self.deltax = self.deltay = sz

        self.screen_rect = self.screen.get_rect()
        self.mario_rect = self.mario.get_rect()

        self.reload()

    def shift_left(self):
        self.rect.left -= self.mario.vector.x

        for rect in self.floor:
            rect.left -= self.mario.vector.x

        for rect in self.coins:
            rect.left -= self.mario.vector.x

        for rect in self.breakables:
            rect.left -= self.mario.vector.x

        for rect in self.unbreakables:
            rect.left -= self.mario.vector.x

        for rect in self.question:
            rect.left -= self.mario.vector.x

        for rect in self.pipes:
            rect.left -= self.mario.vector.x

        for rect in self.goombas:
            rect.left -= self.mario.vector.x

    def update(self):
        print(self.mario.rect.centerx)
        if self.mario.mv_right and self.mario_rect.centerx > self.screen_rect.centerx:
            self.shift_left()

    def blitme(self):
        self.screen.blit(self.image, self.rect)

        for rect in self.floor:
            self.screen.blit(self.brick.image, rect)

        for rect in self.coins:
            self.screen.blit(self.coin.image, rect)

        for rect in self.breakables:
            self.screen.blit(self.breakable.image, rect)

        for rect in self.unbreakables:
            self.screen.blit(self.unbreakable.image, rect)

        for rect in self.question:
            self.screen.blit(self.question_brick.image, rect)

        for rect in self.pipes:
            self.screen.blit(self.pipe.image, rect)

        for rect in self.goombas:
            self.screen.blit(self.goomba.image, rect)

    def reload(self):
        self.image = pygame.image.load('images/background.png')
        self.rect = self.image.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)

        self.rect.top = self.screen_rect.top
        self.rect.left = self.screen_rect.left

        rect = self.brick.rect
        w, h = rect.width, rect.height
        dx, dy = self.deltax, self.deltay

        for nrow in range(len(self.rows)):
            row = self.rows[nrow]
            for ncol in range(len(row)):
                col = row[ncol]
                if col == 'F':
                    self.floor.append(pygame.Rect(ncol * dx, nrow * dy, w, h))
                elif col == 'C':
                    self.coins.append(pygame.Rect(ncol * dx, nrow * dy, w, h))
                elif col == 'B':
                    self.breakables.append(pygame.Rect(ncol * dx, nrow * dy, w, h))
                elif col == 'U':
                    self.unbreakables.append(pygame.Rect(ncol * dx, nrow * dy, w, h))
                elif col == '?':
                    self.question.append(pygame.Rect(ncol * dx, nrow * dy, w, h))
                elif col == 'P':
                    self.pipes.append(pygame.Rect(ncol * dx, nrow * dy, w, h))
                elif col == 'G':
                    self.goombas.append(pygame.Rect(ncol * dx, nrow * dy, w, h))