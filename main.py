import pygame, controls
from space_ship import SpaceShip
from pygame.sprite import Group

def run():

    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Space Invaders")
    bg_color = (0, 0, 0)
    spaceship = SpaceShip(screen)
    bullets = Group()

    while True:
        controls.events(screen, spaceship, bullets)
        spaceship.update_spaceship()
        controls.update_screen(bg_color, screen, spaceship, bullets)
        controls.update_bullets(bullets)


run()
