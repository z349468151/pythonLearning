import pygame
import sys


# 循环监控键盘鼠标事件
def check_events(ship):
    for event in pygame.event.get():
        # 如果事件为quit，就退出
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.type == pygame.K_RIGHT:
                ship.moving_right = True
        elif event.type == pygame.KEYUP:
            if event.type == pygame.K_RIGHT:
                ship.moving_right = False


def update_screen(ai_setting, screen, ship):
    # 从设置里获取屏幕设置
    screen.fill(ai_setting.bg_color)
    # 从ship类里获取飞船
    ship.blitme()
    # 刷新屏幕，更新图形当前位置
    pygame.display.flip()
