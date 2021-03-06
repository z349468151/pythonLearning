import pygame
from AlienGame.settings import Settings
from AlienGame.ship import Ship
import AlienGame.game_functions as gf
from pygame.sprite import Group
from AlienGame.game_stats import GameStats
from AlienGame.button import Button
from AlienGame.scoreboard import Socreboard


def run_game():
    # 初始化游戏
    pygame.init()
    # 初始化设置
    ai_settings = Settings()
    # 初始化屏幕
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    # 初始化飞船
    ship = Ship(ai_settings, screen)
    # 设置屏幕Title
    pygame.display.set_caption('Alien Invasion')
    # 创建一个开始按钮
    play_button = Button(ai_settings, screen, 'Play')
    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)
    # 创建一个记分牌
    sb = Socreboard(ai_settings, screen, stats)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    # 创建一个外星人编组
    aliens = Group()
    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏主循环
    while True:
        # 循环监控键盘鼠标事件
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            # 更新飞船位置
            ship.update()
            # 更新子弹的位置，删除消失的子弹
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            # 更新外星人的位置
            gf.update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets)
        # 整体刷新屏幕
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)


if __name__ == '__main__':
    run_game()
