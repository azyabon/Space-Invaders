import pygame.font
from space_ship import SpaceShip
from pygame.sprite import Group

class Scores():
    """output game scores"""

    def __init__(self, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 36)
        self.image_score()
        self.image_lifes()

    def image_score(self):
        self.score_img = self.font.render(str(self.stats.score), True, self.text_color, (0, 0, 0))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 40
        self.score_rect.top = 20

    def image_lifes(self):
        """show current lifes"""

        self.spaceships = Group()
        for spaceship_num in range(self.stats.lifes_left):
            spaceship = SpaceShip(self.screen)
            spaceship.rect.x = 5 + spaceship_num * spaceship.rect.width
            spaceship.rect.y = 5
            self.spaceships.add(spaceship)

    def show_score(self):
        self.screen.blit(self.score_img, self.score_rect)
        self.spaceships.draw(self.screen)