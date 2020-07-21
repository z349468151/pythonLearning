import pygame


class Ship(object):
    def __init__(self, screen, ai_setting):
        '''初始化飞船并设置其初始位置'''
        self.screen = screen
        self.ai_setting = ai_setting
        # 加载飞船，获取其外接矩形
        self.image = pygame.image.load('images/ship.png')
        # get_rect()返回值包含矩形的居中属性（center centerx centery），获取图片矩形居中位置
        self.rect = self.image.get_rect()
        # 获取程序窗口矩形居中属性
        self.screen_rect = screen.get_rect()
        # 使得图片x值等于程序窗口X值
        self.rect.centerx = self.screen_rect.centerx
        # 使得图片底部位置等于程序窗口底部位置
        self.rect.bottom = self.screen_rect.bottom
        # 在飞船属性center中存储小数值
        self.center = float(self.rect.centerx)
        # 定义移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        '''根据移动标志调整飞船位置'''
        if self.moving_right:
            self.center += self.ai_setting.ship_speed_factor
        elif self.moving_left:
            self.center -= self.ai_setting.ship_speed_factor
        # 根据self.center更新rect对象
        self.rect.centerx = self.center


    def blitme(self):
        '''将飞船呈现在屏幕上'''
        self.screen.blit(self.image, self.rect)
