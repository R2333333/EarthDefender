import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

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

def check_events(settings, stats, screen, play_button, ship, aliens, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown(event, settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup(event, ship)

        elif not stats.active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                check_play_button(settings, screen, stats,  play_button, ship, aliens, bullets, mouse_x, mouse_y)

def check_play_button(settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    if play_button.rect.collidepoint(mouse_x,mouse_y):
        stats.reset_stats()
        stats.active = True

        aliens.empty()
        bullets.empty()

        creat_fleet(settings, screen, ship, aliens)
        ship.center_ship()
        pygame.mouse.set_visible(False)

def update_screen(defaultSetting, stats, screen, ship, aliens, bullets, paly_button):
    screen.fill(defaultSetting.bg_color)
    ship.blitme()
    aliens.draw(screen)
    if not stats.active:
        paly_button.draw_botton()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    pygame.display.flip()


def update_bullets(settings, screen, ship, aliens, bullets):
    bullets.update()
    check_alien_collision(settings, screen, ship, aliens, bullets)
    #remove bullets out of screen
    for bullet in bullets:
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)

def check_alien_collision(settings, screen, ship, aliens, bullets):
    if len(aliens) == 0:
        bullets.empty()
        creat_fleet(settings, screen, ship, aliens)
    
    pygame.sprite.groupcollide(bullets, aliens, True, True)

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

def update_aliens(settings, stats, screen, ship, aliens, bullets):
    check_fleet_edges(settings, aliens)
    aliens.update()
    check_alien_bottom(settings, stats, screen, ship, aliens, bullets)

    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(settings, stats, screen, ship, aliens, bullets)

def ship_hit(settings, stats, screen, ship, aliens, bullets):
    if stats.ship_left > 0:
        stats.ship_left -= 1

        aliens.empty()
        bullets.empty()

        creat_fleet(settings, screen, ship, aliens)
        ship.center_ship()

        sleep(0.5)
    else:
        stats.active = False
        pygame.mouse.set_visible(True)

def check_alien_bottom(settings, stats, screen, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens:
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(settings, stats, screen, ship, aliens, bullets)
            break