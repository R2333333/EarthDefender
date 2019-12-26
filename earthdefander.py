from settings import Settings
from ship import Ship
import game_functions as gf
from alien import Alien
from game_stats import GameStats
from button import Button

def run_game():
    pygame = gf.pygame
    pygame.init()
    defaultSetting = Settings()
    screen = pygame.display.set_mode(
        (defaultSetting.screen_width,defaultSetting.screen_height))
    pygame.display.set_caption('Eath Defender')
    play_button = Button(defaultSetting, screen, 'Play')

    stats = GameStats(defaultSetting)
    ship = Ship(defaultSetting, screen)
    bullets = pygame.sprite.Group()
    aliens = pygame.sprite.Group()
    gf.creat_fleet(defaultSetting, screen, ship, aliens)

    #main loop of the game
    while True:
        gf.check_events(defaultSetting, stats, screen, play_button, ship, aliens, bullets)
        
        if stats.active:
            ship.update()
            gf.update_bullets(defaultSetting, screen, ship, aliens, bullets)
            gf.update_aliens(defaultSetting, stats, screen, ship, aliens, bullets)
        gf.update_screen(defaultSetting, stats, screen,ship, aliens, bullets, play_button)


run_game()
