from settings import Settings
from ship import Ship
import game_functions as gf
from alien import Alien

def run_game():
    pygame = gf.pygame
    pygame.init()
    defaultSetting = Settings()
    screen = pygame.display.set_mode(
        (defaultSetting.screen_width,defaultSetting.screen_height))
    pygame.display.set_caption('Eath Defender')

    ship = Ship(defaultSetting, screen)
    bullets = pygame.sprite.Group()
    aliens = pygame.sprite.Group()
    gf.creat_fleet(defaultSetting, screen, ship, aliens)

    #main loop of the game
    while True:
        gf.check_events(defaultSetting, screen, ship, bullets)
        ship.update()
        gf.update_bullets(aliens, bullets)
        gf.update_aliens(defaultSetting, aliens)
        gf.update_screen(defaultSetting,screen,ship, aliens, bullets)


run_game()
