import pygame
import sys
from AlienGame.settings import Settings
from AlienGame.ship import Ship


def run_game():
    # 初始化游戏
    pygame.init()
    my_setting = Settings()
    screen = pygame.display.set_mode((my_setting.screen_width, my_setting.screen_height))
    ship = Ship(screen)
    # 设置屏幕Title
    pygame.display.set_caption('Alien Invasion')
    # 开始游戏主循环
    while True:
        # 循环监控键盘鼠标事件
        for event in pygame.event.get():
            # 如果事件为quit，就退出
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(my_setting.bg_color)
        ship.blitme()
        # 刷新屏幕，更新图形当前位置
        pygame.display.flip()


if __name__ == '__main__':
    run_game()
