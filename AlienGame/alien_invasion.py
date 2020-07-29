import pygame
from AlienGame.settings import Settings
from AlienGame.ship import Ship
import AlienGame.game_functions as gf
from pygame.sprite import Group
from AlienGame.alien import Alien


def run_game():
    # 初始化游戏
    pygame.init()
    # 初始化设置
    ai_setting = Settings()
    # 初始化屏幕
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
    # 初始化飞船
    ship = Ship(screen, ai_setting)
    # 设置屏幕Title
    pygame.display.set_caption('Alien Invasion')
    # 创建一个用于存储子弹的编组
    bullets = Group()
    # 创建一个外星人
    alien = Alien(ai_setting, screen)

    # 开始游戏主循环
    while True:
        # 循环监控键盘鼠标事件
        gf.check_events(ai_setting, screen, ship, bullets)
        # 更新飞船位置
        ship.update()
        # 更新子弹的位置，删除消失的子弹
        gf.update_bullets(bullets)
        # 整体刷新屏幕
        gf.update_screen(ai_setting, screen, ship, alien, bullets)


if __name__ == '__main__':
    run_game()
