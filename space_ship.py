import pygame

class SpaceShip():

    def __init__(self, screen):
        """init spaceship"""

        self.screen = screen
        self.image = pygame.image.load("assets/spaceship.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False

    def output(self):
        """draw spaceship"""

        self.screen.blit(self.image, self.rect)

    def update_spaceship(self):
        """update spaceship position"""

        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += 0.3
        if self.mleft and self.rect.left > 0:
            self.center -= 0.3

        self.rect.centerx = self.center