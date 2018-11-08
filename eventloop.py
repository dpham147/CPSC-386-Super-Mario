import pygame
import sys


class EventLoop:
    def __init__(self, finished):
        self.finished = finished

    def check_events(self, mario):
        mario.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    mario.jump()
                elif event.key == pygame.K_LSHIFT:
                    print("Pew pew")
                    # Mario fireball
                elif event.key == pygame.K_d:
                    mario.mv_right = True
                elif event.key == pygame.K_s:
                    mario.is_crouch = True
                elif event.key == pygame.K_a:
                    mario.mv_left = True
                elif event.key == pygame.K_q:
                    sys.exit()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    mario.mv_right = False
                elif event.key == pygame.K_s:
                    mario.is_crouch = False
                elif event.key == pygame.K_a:
                    mario.mv_left = False