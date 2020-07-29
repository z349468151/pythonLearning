import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    '''表示单个外星人'''

    def __init__(self, ai_settings, screen):
        # 初始化外星人，并设置其位置
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载外星人图像，设置Rect属性
        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()

        # 每个外星人开始都在左上角
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人准确位置
        self.x = float(self.rect.x)

    def blitme(self):
        # 在指定位置绘制外星人
        self.screen.blit(self.image, self.rect)
