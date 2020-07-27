import pygame
import sys
from AlienGame.bullet import Bullet


# 循环监控键盘鼠标事件
def check_events(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():
        # 如果事件为quit，就退出
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def update_screen(ai_settings, screen, ship, bullets):
    # 从设置里获取屏幕设置
    screen.fill(ai_settings.bg_color)
    # 在飞船和外星人后面重绘所有子弹：
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # 从ship类里获取飞船
    ship.blitme()
    # 刷新屏幕，更新图形当前位置
    pygame.display.flip()


def update_bullets(bullets):
    # 更新子弹的编组
    bullets.update()
    # 删除消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
