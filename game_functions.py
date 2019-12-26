import sys
import pygame
from bullet import Bullet
from alien import Alien

def check_keydown(event, settings, screen, ship, bullets):
    if event.key == pygame.K_q:
        pygame.quit()
        sys.exit()

    if event.key == pygame.K_RIGHT:
        ship.movingR = True
    elif event.key == pygame.K_LEFT:
        ship.movingL = True
    elif event.key == pygame.K_SPACE:
        new_bullet = Bullet(settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.movingR = False

    elif event.key == pygame.K_LEFT:
        ship.movingL = False

def check_events(settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown(event, settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup(event, ship)

def update_screen(defaultSetting, screen, ship, aliens, bullets):
    screen.fill(defaultSetting.bg_color)
    ship.blitme()
    aliens.draw(screen)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    pygame.display.flip()


def update_bullets(aliens, bullets):
    bullets.update()
    #remove bullets out of screen
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    for bullet in bullets:
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)

def get_num_alien_x(settings, alien_width):
    avaible_space = settings.screen_width - 2 * alien_width
    alien_number_x = int(avaible_space/(2 * alien_width))
    return alien_number_x

def creat_alian(settings, screen, aliens, alien_number, row_number):
    alien = Alien(settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def creat_fleet(settings, screen, ship, aliens):
    alien = Alien(settings, screen)
    alien_number_x = get_num_alien_x(settings, alien.rect.width)
    num_rows = get_num_rows(settings, ship.rect.height, alien.rect.height)

    for row in range(num_rows):
        for num in range(alien_number_x):
            creat_alian(settings, screen, aliens, num, row)

def get_num_rows(settings, ship_height, alien_height):
    avaible_space_y = (settings.screen_height - 3 * alien_height - ship_height)
    num_rows = int(avaible_space_y / (2 * alien_height))
    return num_rows

def change_fleet_direction(settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += settings.drop_speed
    settings.fleet_direction *= -1

def check_fleet_edges(settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edge():
            change_fleet_direction(settings, aliens)
            break

def update_aliens(settings, aliens):
    check_fleet_edges(settings, aliens)
    aliens.update()
