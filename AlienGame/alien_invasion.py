import pygame
from AlienGame.settings import Settings
from AlienGame.ship import Ship
import AlienGame.game_functions as gf


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
    # 开始游戏主循环
    while True:
        # 循环监控键盘鼠标事件
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_setting, screen, ship)


if __name__ == '__main__':
    run_game()
