import pygame

from settings import Settings

from ship import Ship


import game_functions as gf

from pygame.sprite import Group
# 游戏主程序入口


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                     ai_settings.screen_height))
    pygame.display.set_caption("alien_invasion")
    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个外星人编组
    aliens = Group()
    # 创建一个用于存储子弹的编组
    bullets = Group()
    # 开始游戏主循环
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # 创建外星人群

    while True:

        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
        gf.update_aliens(ai_settings, aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()

