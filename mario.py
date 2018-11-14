import pygame
from pygame.sprite import Sprite
from pygame.sprite import Group
from vector import Vector
from timer import Timer
from fireball import Fireball


class Mario(Sprite):
    def __init__(self, screen):
        super(Mario, self).__init__()

        # Set Small Mario Animation Frames
        self.small_image = pygame.image.load('images/mario/small-1.png')
        self.small_jump = pygame.image.load('images/mario/small-6.png')
        self.small_invincible = pygame.image.load('images/mario/inv_small_mario_color1-1.png')

        self.big_image = pygame.image.load('images/mario/big-1.png')
        self.big_jump = pygame.image.load('images/mario/big-6.png')
        self.big_crouch = pygame.image.load('images/mario/big-7.png')

        self.fire_image = pygame.image.load('images/mario/fire-1.png')
        self.fire_jump = pygame.image.load('images/mario/fire-6.png')
        self.fire_crouch = pygame.image.load('images/mario/fire-7.png')

        frames = [pygame.image.load('images/mario/small-2.png'),
                  pygame.image.load('images/mario/small-3.png'),
                  pygame.image.load('images/mario/small-4.png')]
        self.small_right_timer = Timer(frames)

        frames = [pygame.image.load('images/mario/inv_small_mario_color1-2.png'),
                  pygame.image.load('images/mario/inv_small_mario_color1-3.png'),
                  pygame.image.load('images/mario/inv_small_mario_color1-4.png')]
        self.small_invincible_timer = Timer(frames)

        frames = [pygame.image.load('images/mario/big-2.png'),
                  pygame.image.load('images/mario/big-3.png'),
                  pygame.image.load('images/mario/big-4.png')]
        self.big_right_timer = Timer(frames)

        frames = [pygame.image.load('images/mario/fire-2.png'),
                  pygame.image.load('images/mario/fire-3.png'),
                  pygame.image.load('images/mario/fire-4.png')]
        self.fire_right_timer = Timer(frames)

        self.image = self.small_image
        self.rect = self.small_image.get_rect()

        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.fireballs = Group()
        self.fireball_delay = 100

        self.restart()

    def get_rect(self):
        return self.rect

    def get_status(self):
        if self.is_star:
            print('Invincible')
        if self.is_fire:
            print('FIRE')
        if self.is_super:
            print('SUPER')
        if self.is_crouch:
            print('CROUCHING')
        if self.airborne:
            print('AIRBORNE')

    def update(self, background):
        if not self.is_dead:
            # Handle X Movement
            if self.mv_left and not self.is_crouch:
                # Manip position
                # self.vector.x = max(self.vector.x - Vector.forces().x, -1)
                background.rect.left -= min(0, self.vector.x)
                self.face_right = False

                # Select Image if grounded
                if not self.airborne:
                    if self.is_fire:
                        self.image = pygame.transform.flip(self.fire_right_timer.imagerect(), True, False)
                    elif self.is_super:
                        self.image = pygame.transform.flip(self.big_right_timer.imagerect(), True, False)
                    else:
                        if self.is_star:
                            self.image = pygame.transform.flip(self.small_invincible_timer.imagerect(), True, False)
                        else:
                            self.image = pygame.transform.flip(self.small_right_timer.imagerect(), True, False)

            elif self.mv_right and not self.is_crouch:
                # Manip position
                self.vector.x = min(self.vector.x + Vector.forces().x, 1)
                # background.rect.right -= min(background.rect.right, abs(self.vector.x))
                self.face_right = True

                # Select Image if grounded
                if not self.airborne:
                    if self.is_fire:
                        self.image = self.fire_right_timer.imagerect()
                    elif self.is_super:
                        self.image = self.big_right_timer.imagerect()
                    else:
                        if self.is_star:
                            self.image = self.small_invincible_timer.imagerect()
                        else:
                            self.image = self.small_right_timer.imagerect()

            else:
                if not self.airborne:
                    if not self.face_right:
                        if self.is_fire:
                            if self.is_crouch:
                                self.image = pygame.transform.flip(self.fire_crouch, True, False)
                            else:
                                self.image = pygame.transform.flip(self.fire_image, True, False)
                        elif self.is_super:
                            if self.is_crouch:
                                self.image = pygame.transform.flip(self.big_crouch, True, False)
                            else:
                                self.image = pygame.transform.flip(self.big_image, True, False)
                        else:
                            if self.is_star:
                                self.image = pygame.transform.flip(self.small_invincible, True, False)
                            else:
                                self.image = pygame.transform.flip(self.small_image, True, False)
                    elif self.face_right:
                        if self.is_fire:
                            if self.is_crouch:
                                self.image = self.fire_crouch
                            else:
                                self.image = self.fire_image
                        elif self.is_super:
                            if self.is_crouch:
                                self.image = self.big_crouch
                            else:
                                self.image = self.big_image
                        else:
                            if self.is_star:
                                self.image = self.small_invincible
                            else:
                                self.image = self.small_image

                self.vector.x = 0

            self.rect.centerx = max(self.rect.centerx + self.vector.x, 0)

            # Handle Y Movement
            if self.airborne:
                self.rect.centery += self.vector.y
                self.vector.y += Vector.forces().y
            elif self.rect.collidelist(background.floor):
                self.rect.centery += 0
                self.vector.y += 0
            else:
                self.rect.centery -= self.vector.y
                self.vector.y -= Vector.forces().y

            # Handle falling
            # if falling = True:
            #    self.airborne = True

            # Prevent floor clipping
            # if self.rect.bottom >= self.screen_rect.centery and not self.airborne:
            #    self.rect.bottom = self.screen_rect.centery

            # Handle invincibility timer
            if self.is_star:
                self.star_timer -= 1
                if self.star_timer == 0:
                    pygame.mixer.Channel(7).stop()
                    pygame.mixer.Channel(0).unpause()
                    self.is_star = False

            self.fireball_delay = min(100, self.fireball_delay + 1)
            self.fireballs.update()
            for ball in self.fireballs:
                if ball.timetolive <= 0:
                    ball.kill()
        else:
            self.rect.centery += self.vector.y
            self.vector.y += Vector.forces().y
            self.rect.top = min(self.screen_rect.bottom, self.rect.top)
            self.death_timer -= 1
            print(self.death_timer)
            if self.death_timer == 0:
                self.restart()

    def restart(self):
        self.death_timer = 600
        self.is_star = False
        self.star_timer = 1000
        self.is_super = False
        self.is_fire = False
        self.is_crouch = False
        self.airborne = False
        self.face_right = True
        self.is_dead = False

        self.mv_left = False
        self.mv_right = False

        self.vector = Vector(0, 0)

        self.rect.left = self.screen_rect.left
        self.rect.bottom = self.screen_rect.centery

        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

    def blitme(self):
        self.screen.blit(self.image, self.rect)
        self.fireballs.draw(self.screen)

    def jump(self):
        if not self.airborne:
            self.airborne = True
            pygame.mixer.Channel(1).play(pygame.mixer.Sound('sound/small_jump.ogg'))

            if self.is_fire:
                self.vector.y = -4.5
                if not self.face_right:
                    self.image = pygame.transform.flip(self.fire_jump, True, False)
                elif self.face_right:
                    self.image = self.fire_jump
            elif self.is_super:
                self.vector.y = -4.5
                if not self.face_right:
                    self.image = pygame.transform.flip(self.big_jump, True, False)
                elif self.face_right:
                    self.image = self.big_jump
            else:
                self.vector.y = -3
                if not self.face_right:
                    self.image = pygame.transform.flip(self.small_jump, True, False)
                elif self.face_right:
                    self.image = self.small_jump

    def shoot(self):
        if self.is_fire and len(self.fireballs) < 4 and self.fireball_delay == 100:
            pygame.mixer.Channel(2).play(pygame.mixer.Sound('sound/fireball.ogg'))
            fireball = Fireball(self, self.screen)
            self.fireballs.add(fireball)
            self.fireball_delay = 0

    def star(self):
        self.star_timer = 1000
        self.is_star = True
        bottom = self.rect.bottom
        centerx = self.rect.centerx
        if not self.face_right:
            self.image = pygame.transform.flip(self.small_invincible, True, False)
            self.rect = self.image.get_rect()
            self.rect.bottom = bottom
            self.rect.centerx = centerx
        elif self.face_right:
            self.image = self.small_invincible
            self.rect = self.image.get_rect()
            self.rect.bottom = bottom
            self.rect.centerx = centerx
        pygame.mixer.Channel(0).pause()
        pygame.mixer.Channel(7).play(pygame.mixer.Sound('music/invincible.ogg'))

    def super(self):
        self.is_fire = False
        self.is_super = True
        bottom = self.rect.bottom
        centerx = self.rect.centerx
        if not self.face_right:
            self.image = pygame.transform.flip(self.big_image, True, False)
            self.rect = self.image.get_rect()
            self.rect.bottom = bottom
            self.rect.centerx = centerx
        elif self.face_right:
            self.image = self.big_image
            self.rect = self.image.get_rect()
            self.rect.bottom = bottom
            self.rect.centerx = centerx

    def fire(self):
        self.is_fire = True
        self.is_super = False
        bottom = self.rect.bottom
        centerx = self.rect.centerx
        if not self.face_right:
            self.image = pygame.transform.flip(self.fire_image, True, False)
            self.rect = self.image.get_rect()
            self.rect.bottom = bottom
            self.rect.centerx = centerx
        elif self.face_right:
            self.image = self.fire_image
            self.rect = self.image.get_rect()
            self.rect.bottom = bottom
            self.rect.centerx = centerx

    def normal(self):
        self.is_fire = False
        self.is_super = False
        bottom = self.rect.bottom
        centerx = self.rect.centerx
        if not self.face_right:
            self.image = pygame.transform.flip(self.small_image, True, False)
            self.rect = self.image.get_rect()
            self.rect.bottom = bottom
            self.rect.centerx = centerx
        elif self.face_right:
            self.image = self.small_image
            self.rect = self.image.get_rect()
            self.rect.bottom = bottom
            self.rect.centerx = centerx

    def die(self):
        self.is_dead = True
        self.vector.y = -2.5
        pygame.mixer.Channel(0).play(pygame.mixer.Sound('music/death.wav'))