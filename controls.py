import pygame, sys
from bullet import Bullet
from alien import Alien


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
            elif event.key == pygame.K_w or event.key == pygame.K_UP:
                spaceship.mtop = True
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                spaceship.mbottom = True
            elif event.key == pygame.K_SPACE:
                pygame.mixer.music.load('assets/shoot.mp3') #dura
                pygame.mixer.music.set_volume(0.2)
                pygame.mixer.music.play()
                new_bullet = Bullet(screen, spaceship)
                bullets.add(new_bullet)
            elif event.key == pygame.K_ESCAPE:
                pause(screen)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                spaceship.mright = False
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                spaceship.mleft = False
            elif event.key == pygame.K_w or event.key == pygame.K_UP:
                spaceship.mtop = False
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                spaceship.mbottom = False

def update_screen(bgc, bg_color, screen, stats, score, spaceship, alien, bullets):
    """update screen"""

    screen.fill(bg_color)
    screen.blit(bgc, (0, 0))
    score.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    spaceship.output()
    alien.draw(screen)
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

def gameover(screen):
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

        pygame.display.update()

def gamewin(screen):
    pass


def create_alien(screen, aliens):
    alien = Alien(screen)
    aliens.add(alien)

def aliens_check(stats, score, screen, spaceship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            pygame.mixer.music.load('assets/clash.mp3')
            pygame.mixer.music.play()
            life_kill(stats, score, screen, spaceship, aliens, bullets)

def update_aliens(stats, score, screen, spaceship, alien, bullets):
    """update aliens position"""

    alien.update()

    if pygame.sprite.spritecollideany(spaceship, alien):
        pygame.mixer.music.load('assets/clash.mp3') #kasino
        pygame.mixer.music.play()
        life_kill(stats, score, screen, spaceship, alien, bullets)

def update_bullets(screen, stats, score, alien, bullets):
    """update position bullets"""

    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    collision = pygame.sprite.groupcollide(bullets, alien, True, True)

    if collision:
        pygame.mixer.music.load('assets/boom.mp3') #nemestniy
        pygame.mixer.music.play()
        for alien in collision.values():
            stats.score += 20 * len(alien)

        score.image_score()
        score.image_lifes()

    if len(alien) == 0:
        create_alien(screen, alien)

def life_kill(stats, score, screen, spaceship, alien, bullets):
    """destroyed spaceship"""

    if stats.lifes_left == 0:
        stats.lifes_left = 3
        stats.score = 0
        score.image_score()
        score.image_lifes()
        alien.empty()
        bullets.empty()
        spaceship.create_spaceship()
        pygame.mixer.music.load('assets/gameover.wav')  # nemestniy
        pygame.mixer.music.play()
        gameover(screen)
    else:
        stats.lifes_left -= 1
        stats.score -= 50
        score.image_score()
        score.image_lifes()
        alien.empty()