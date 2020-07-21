import pygame
import sys


# 循环监控键盘鼠标事件
def check_events(ship):
    for event in pygame.event.get():
        # 如果事件为quit，就退出
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)


def check_keydown_event(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True


def check_keyup_event(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def update_screen(ai_setting, screen, ship):
    # 从设置里获取屏幕设置
    screen.fill(ai_setting.bg_color)
    # 从ship类里获取飞船
    ship.blitme()
    # 刷新屏幕，更新图形当前位置
    pygame.display.flip()
