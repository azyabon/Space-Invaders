import pygame
from pygame.sprite import Sprite

class SpaceShip(Sprite):

    def __init__(self, screen):
        """init spaceship"""

        super(SpaceShip, self).__init__()
        self.screen = screen
        self.image = pygame.image.load("assets/spaceship.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery + 200)
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False
        self.mtop = False
        self.mbottom = False

    def output(self):
        """draw spaceship"""

        self.screen.blit(self.image, self.rect)

    def update_spaceship(self):
        """update spaceship position"""

        if self.mright and self.rect.right < self.screen_rect.right:
            self.centerx += 0.3
        if self.mleft and self.rect.left > 0:
            self.centerx -= 0.3
        if self.mtop and self.rect.top > self.screen_rect.top:
            self.centery -= 0.3
        if self.mbottom and self.rect.bottom < self.screen_rect.bottom:
            self.centery += 0.3

        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def create_spaceship(self):
        """position spaceship"""
        self.centerx = self.screen_rect.centerx
        self.centery = self.screen_rect.centery + 200