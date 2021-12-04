import pygame, controls, sys, os, time, threading
from space_ship import SpaceShip
from pygame.sprite import Group
from stats import Stats
from scores import Scores
from menu import Menu

def run():

    def start_game():
        while True:
            controls.events(screen, spaceship, bullets)
            spaceship.update_spaceship()
            controls.update_screen(bgc, bg_color, screen, stats, score, spaceship, alien, bullets)
            controls.update_bullets(screen, stats, score, alien, bullets)
            controls.update_aliens(stats, score, screen, spaceship, alien, bullets)
            controls.aliens_check(stats, score, screen, spaceship, alien, bullets)

    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Space Invaders")
    bg_color = (0, 0, 0)
    bgc = pygame.image.load("assets/bgc.jpg")
    spaceship = SpaceShip(screen)
    bullets = Group()
    alien = Group()
    controls.create_alien(screen, alien)
    stats = Stats()
    score = Scores(screen, stats)
    menu = Menu()
    menu.append_option("Start", start_game)
    menu.append_option("Settings", lambda: print(1))
    menu.append_option("Quit", sys.exit)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    menu.switch(-1)
                    pygame.mixer.music.load('assets/menu_move.mp3')
                    pygame.mixer.music.play()
                elif event.key == pygame.K_s:
                    menu.switch(1)
                    pygame.mixer.music.load('assets/menu_move.mp3')
                    pygame.mixer.music.play()
                elif event.key == pygame.K_SPACE:
                    menu.select()
            screen.fill((0, 0, 0))
            menu.draw(screen, 100, 100, 80)
            pygame.display.flip()


run()
