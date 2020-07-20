import pygame


class Ship(object):
    def __init__(self, screen):
        '''初始化飞船并设置其初始位置'''
        self.screen = screen

        # 加载飞船，获取其外接矩形
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        self.screen.blit(self.image,self.rect)
