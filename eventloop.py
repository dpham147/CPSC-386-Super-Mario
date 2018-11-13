import pygame
import sys


class EventLoop:
    def __init__(self, finished):
        self.finished = finished

    def check_events(self, mario, background, stats):
        mario.update(background)
        stats.tick()

        for event in pygame.event.get():
            # Exit Game
            if event.type == pygame.QUIT:
                sys.exit()
            # Keydown events
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    mario.jump()
                elif event.key == pygame.K_LSHIFT:
                    print("Pew pew")
                    mario.shoot()
                elif event.key == pygame.K_d:
                    mario.mv_right = True
                elif event.key == pygame.K_s:
                    if mario.is_super or mario.is_fire:
                        mario.is_crouch = True
                elif event.key == pygame.K_a:
                    mario.mv_left = True
                elif event.key == pygame.K_q:
                    sys.exit()

                # Debugging Keys
                elif event.key == pygame.K_TAB:
                    if not mario.is_star:
                        mario.star()
                    else:
                        mario.normal()
                elif event.key == pygame.K_COMMA:
                    if not mario.is_super:
                        mario.super()
                    else:
                        mario.normal()
                elif event.key == pygame.K_PERIOD:
                    if not mario.is_fire:
                        mario.fire()
                    else:
                        mario.normal()
                elif event.key == pygame.K_k:
                    mario.die()
                    background.reload()

            # Keyup events
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    mario.mv_right = False
                elif event.key == pygame.K_s:
                    mario.is_crouch = False
                elif event.key == pygame.K_a:
                    mario.mv_left = False