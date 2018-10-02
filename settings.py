class Settings():
    # 储存游戏所有设置的类

    def __init__(self):
        # 初始化游戏设置
        # 屏幕设置

        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # 外星人设置
        self.alien_speed_factor = 1
        self.fleet.drop_speed = 10
        # fleet_direction 为1 表示向右移，为-1 向左
        self.fleet_direction = 1

        # 飞船的设置
        self.ship_speed_factor = 5
        # 子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3