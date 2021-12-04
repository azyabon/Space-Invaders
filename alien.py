import pygame
import random

class Alien(pygame.sprite.Sprite):
    """init Alien"""

    def __init__(self, screen):
        """init start position"""
        super(Alien, self).__init__()
        self.screen = screen
        self.aliens = ["assets/aliens/alien1.png", "assets/aliens/alien2.png", "assets/aliens/alien3.png", "assets/aliens/alien4.png", "assets/aliens/alien5.png"]
        self.image = pygame.image.load(self.aliens[random.randint(0, 4)])
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 600)
        self.rect.y = random.randint(-300, -60)
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        """output alien on dsp"""

        self.screen.blit(self.image, self.rect)

    def update(self):
        """moving alien"""

        self.y += 0.1
        self.rect.y = self.y