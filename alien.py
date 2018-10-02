import pygame

from pygame.sprite import Sprite


class Alien(Sprite):
    # 表示单个外星人的类
    def __init__(self, ai_settings, screen):
        # 初始化外星人并设置其初始位置
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载外星人图片并设置其rect属性
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # 每个外星人最初都在屏幕的左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 储存外星人的准确位置
        self.x = float(self.rect.x)

    def update(self):
        # 向右移动外星人
        self.x += self.ai_settings.alien_speed_factor
        self.rect.x = self.x

    def blimte(self):
        # 指定位置绘制外星人
        self.screen.blit(self.image, self.rect)
