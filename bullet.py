import pygame

class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, spaceship):
        """create bullet in current position spaceship_gun"""

        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 3, 15)
        self.color = (13, 255, 0)
        self.speed = 0.7
        self.rect.centerx = spaceship.rect.centerx
        self.rect.top = spaceship.rect.top
        self.y = float(self.rect.y)

    def update(self):
        """move bullet"""

        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        """draw bullet on dsp"""

        pygame.draw.rect(self.screen, self.color, self.rect)