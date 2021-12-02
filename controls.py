import pygame, sys
from bullet import Bullet


def events(screen, spaceship, bullets):
    """events"""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                spaceship.mright = True
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                spaceship.mleft = True
            elif event.type == pygame.K_SPACE:
                new_bullet = Bullet(screen, spaceship)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                spaceship.mright = False
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                spaceship.mleft = False

def update_screen(bg_color, screen, spaceship, bullets):
    """update screen"""

    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    spaceship.output()
    pygame.display.flip()

def update_bullets(bullets):
    """update position bullets"""

    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)