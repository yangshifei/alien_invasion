import pygame

from settings import Settings

from ship import Ship


import game_functions as gf

from pygame.sprite import Group
# 游戏主程序入口

from game_stats import GameStats

from button import Button

from game_stats import GameStats

from scoreboard import Scoreboard


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
    #  创建外星人群

    stats = GameStats(ai_settings)
    # 创建一个用于存储游戏统计信息的实例,并创建记分牌
    sb = Scoreboard(ai_settings, screen, stats)
    pygame.display.set_caption("Alien Invasion")

    # 创建play按钮
    play_button = Button(ai_settings, screen, "Play")

    while True:

        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, stats, play_button, ship, bullets)
        ship.update()
        gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
        gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)


run_game()

