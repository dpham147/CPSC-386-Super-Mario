import pygame.font


class Scoreboard:
    def __init__(self, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats

        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 28)

    def prep_score(self):
        score = int(self.stats.score)
        score_val = "{:,}".format(score)
        score_str = "Score:"
        self.score_image = self.font.render(score_str, True, self.text_color)
        self.score_val_image = self.font.render(score_val, True, self.text_color)

        self.score_rect = self.score_image.get_rect()
        self.score_val_rect = self.score_val_image.get_rect()
        self.score_rect.top = 10
        self.score_val_rect.top = 30
        self.score_rect.centerx = self.screen_rect.right / 6
        self.score_val_rect.centerx = self.screen_rect.right / 6

    def prep_coins(self):
        coins = int(self.stats.coins)
        coins_val = "{:,}".format(coins)
        coins_str = "Coins:"
        self.coins_image = self.font.render(coins_str, True, self.text_color)
        self.coins_val_image = self.font.render(coins_val, True, self.text_color)

        self.coins_rect = self.coins_image.get_rect()
        self.coins_val_rect = self.coins_val_image.get_rect()
        self.coins_rect.top = 10
        self.coins_val_rect.top = 30
        self.coins_rect.centerx = self.screen_rect.right * 2 / 6
        self.coins_val_rect.centerx = self.screen_rect.right * 2 / 6

    def prep_world(self):
        world = self.stats.level
        world_str = "Level:"
        self.world_image = self.font.render(world_str, True, self.text_color)
        self.world_val_image = self.font.render(world, True, self.text_color)

        self.world_rect = self.score_image.get_rect()
        self.world_val_rect = self.world_val_image.get_rect()
        self.world_rect.top = 10
        self.world_val_rect.top = 30
        self.world_rect.centerx = self.screen_rect.right * 3 / 6
        self.world_val_rect.centerx = self.screen_rect.right * 3 / 6

    def prep_time(self):
        time = int(self.stats.time)
        time_val = "{:,}".format(time)
        time_str = "Time:"
        self.time_image = self.font.render(time_str, True, self.text_color)
        self.time_val_image = self.font.render(time_val, True, self.text_color)

        self.time_rect = self.time_image.get_rect()
        self.time_val_rect = self.time_val_image.get_rect()
        self.time_rect.top = 10
        self.time_val_rect.top = 30
        self.time_rect.centerx = self.screen_rect.right * 4 / 6
        self.time_val_rect.centerx = self.screen_rect.right * 4 / 6

    def prep_lives(self):
        lives = int(self.stats.lives)
        lives_val = "{:,}".format(lives)
        lives_str = "Lives:"
        self.lives_image = self.font.render(lives_str, True, self.text_color)
        self.lives_val_image = self.font.render(lives_val, True, self.text_color)

        self.lives_rect = self.score_image.get_rect()
        self.lives_val_rect = self.score_val_image.get_rect()
        self.lives_rect.top = 10
        self.lives_val_rect.top = 30
        self.lives_rect.centerx = self.screen_rect.right * 5 / 6
        self.lives_val_rect.centerx = self.screen_rect.right * 5 / 6

    def update(self):
        self.prep_score()
        self.prep_coins()
        self.prep_world()
        self.prep_time()
        self.prep_lives()

        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.score_val_image, self.score_val_rect)

        self.screen.blit(self.coins_image, self.coins_rect)
        self.screen.blit(self.coins_val_image, self.coins_val_rect)

        self.screen.blit(self.world_image, self.world_rect)
        self.screen.blit(self.world_val_image, self.world_val_rect)

        self.screen.blit(self.time_image, self.time_rect)
        self.screen.blit(self.time_val_image, self.time_val_rect)

        self.screen.blit(self.lives_image, self.lives_rect)
        self.screen.blit(self.lives_val_image, self.lives_val_rect)
