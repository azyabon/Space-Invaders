import pygame, sys
from bullet import Bullet
from alien import Alien


def events(screen, spaceship, bullets, aliens):
    """events"""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            spaceship.image = pygame.image.load("assets/spaceship_move.png")
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                spaceship.mright = True
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                spaceship.mleft = True
            elif event.key == pygame.K_w or event.key == pygame.K_UP:
                spaceship.mtop = True
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                spaceship.mbottom = True
            elif event.key == pygame.K_SPACE:
                pygame.mixer.music.load('assets/shoot.mp3')
                pygame.mixer.music.set_volume(0.2)
                pygame.mixer.music.play()
                new_bullet = Bullet(screen, spaceship)
                bullets.add(new_bullet)
            elif event.key == pygame.K_ESCAPE:
                pause(screen)
        elif event.type == pygame.KEYUP:
            spaceship.image = pygame.image.load("assets/spaceship.png")
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                spaceship.mright = False
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                spaceship.mleft = False
            elif event.key == pygame.K_w or event.key == pygame.K_UP:
                spaceship.mtop = False
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                spaceship.mbottom = False

def update_screen(bgc, bg_color, screen, stats, score, spaceship, aliens, bullets):
    """update screen"""

    screen.fill(bg_color)
    screen.blit(bgc, (0, 0))
    score.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    spaceship.output()
    aliens.draw(screen)
    pygame.display.flip()

def print_text(message, x, y, screen):
    text = pygame.font.SysFont(None, 40).render(message, True, (255, 255, 255))
    screen.blit(text, (x, y))

def pause(screen):
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        print_text("Press enter to continue game", 190, 280, screen)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            paused = False

        pygame.display.update()

def gameover(screen, alien):
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        print_text("GAME OVER", 290, 260, screen)
        print_text("Press enter to continue game", 190, 300, screen)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            paused = False
            create_alien(screen, alien, 4)

        pygame.display.update()

def gamewin():
    pass

def create_alien(screen, aliens, num):

    for i in range(num):
        alien = Alien(screen)
        aliens.add(alien)

def aliens_check(stats, score, screen, spaceship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            aliens.remove(alien)
            create_alien(screen, aliens, 1)
            pygame.mixer.music.load('assets/clash.mp3')
            pygame.mixer.music.play()
            life_kill(stats, score, screen, spaceship, aliens, bullets)

def update_aliens(stats, score, screen, spaceship, aliens, bullets):
    """update aliens position"""

    aliens.update()

    for alien in aliens.sprites():
        if pygame.sprite.spritecollideany(spaceship, aliens):
            aliens.remove(alien)
            create_alien(screen, aliens, 1)
            pygame.mixer.music.load('assets/clash.mp3')
            pygame.mixer.music.play()
            life_kill(stats, score, screen, spaceship, aliens, bullets)

def update_bullets(screen, stats, score, alien, bullets):
    """update position bullets"""

    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    collision = pygame.sprite.groupcollide(bullets, alien, True, True)

    if collision:
        create_alien(screen, alien, 1)
        pygame.mixer.music.load('assets/boom.mp3')
        pygame.mixer.music.play()
        for alien in collision.values():
            stats.score += 20 * len(alien)

        score.image_score()
        score.image_lifes()

def life_kill(stats, score, screen, spaceship, aliens, bullets):
    """destroyed spaceship"""

    if stats.lifes_left == 0:
        stats.lifes_left = 3
        stats.score = 0
        score.image_score()
        score.image_lifes()
        aliens.empty()
        bullets.empty()
        spaceship.create_spaceship()
        pygame.mixer.music.load('assets/gameover.wav')
        pygame.mixer.music.play()
        gameover(screen, aliens)
    else:
        stats.lifes_left -= 1
        stats.score -= 50
        score.image_score()
        score.image_lifes()
        # alien.empty()