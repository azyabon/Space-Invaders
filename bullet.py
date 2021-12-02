import pygame

class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, spaceship):
        """create bullet in current position spaceship_gun"""

        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 6, 12)
        self.color = 255, 255, 255
        self.speed = 1.5
        self.rect.centerx = spaceship.rect.centerx
        self.rect.top = spaceship.rect.top
        self.y = float(self.rect.y)

    def update_bullet(self):
        """move bullet"""

        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        """draw bullet on dsp"""

        pygame.draw.rect(self.screen, self.color, self.rect)