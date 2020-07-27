# 横着发子弹的飞机
import pygame
import sys
from pygame.sprite import Sprite, Group


class Ship(object):
    def __init__(self, screen):
        self.screen = screen
        # 把ship初始化进来
        self.ship_image = pygame.image.load('AlienGame/images/ship_horizontally.png')
        # 获取ship的外接矩形
        self.ship_rect = self.ship_image.get_rect()
        # 获取screen的外接矩形
        self.screen_rect = screen.get_rect()
        # ship放到屏幕Y轴中间，X为0
        self.ship_rect.centery = self.screen_rect.centery
        self.ship_rect.left = self.screen_rect.left

    def update(self, settings):
        if settings.move_up and self.ship_rect.top > 0:
            self.ship_rect.centery -= settings.ship_speed
        elif settings.move_down and self.ship_rect.bottom < self.screen_rect.bottom:
            self.ship_rect.centery += settings.ship_speed
        elif settings.move_left and self.ship_rect.left > 0:
            self.ship_rect.centerx -= settings.ship_speed
        elif settings.move_right and self.ship_rect.right < self.screen_rect.right:
            self.ship_rect.centerx += settings.ship_speed

    def ship_blit(self):
        # 把图片放到指定位置
        self.screen.blit(self.ship_image, self.ship_rect)


class Bullet(Sprite):
    def __init__(self, ship, settings):
        super().__init__()
        # 画一个矩形，Rect(left,top,width,height)
        self.bullet_rect = pygame.Rect(0, 0, 10, 3)
        # 子弹放到ship的中间
        self.bullet_rect.centery = ship.ship_rect.centery
        self.bullet_rect.right = ship.ship_rect.right
        self.color = (60, 60, 60)
        self.speed = settings.bullet_speed

    def update(self):
        self.bullet_rect.centerx += self.speed

    def draw_bullets(self, screen, color, rect):
        pygame.draw.rect(screen, color, rect)


class Settings(object):

    def __init__(self):
        # 键盘按键标记
        self.move_up = False
        self.move_down = False
        self.move_left = False
        self.move_right = False
        # 窗口大小
        self.screen_size = (800, 600)
        self.screen_color = (230, 230, 230)
        # 设置飞船速度
        self.ship_speed = 1.2
        # 设置子弹速度
        self.bullet_speed = 1
        # 设置同一屏幕内子弹最大数量
        self.bullet_allowed = 3


class GameFunctions(object):
    def __init__(self):
        pass

    def check_events(self, settings, bullets, ship):
        # 循环监控screen内的事件
        for self.event in pygame.event.get():
            # 设置关闭游戏
            if self.event.type == pygame.QUIT:
                sys.exit()
            # 监控键盘按下
            elif self.event.type == pygame.KEYDOWN:
                # 判断按的什么键，并对应处理图像
                self.check_key_down(self.event, settings, bullets, ship)
            elif self.event.type == pygame.KEYUP:
                # 判断弹起的什么键，并对应处理图像
                self.check_key_up(self.event, settings)

    def check_key_down(self, event, settings, bullets, ship):
        # 判断上下左右
        if event.key == pygame.K_UP:
            settings.move_up = True
        elif event.key == pygame.K_DOWN:
            settings.move_down = True
        elif event.key == pygame.K_LEFT:
            settings.move_left = True
        elif event.key == pygame.K_RIGHT:
            settings.move_right = True
        elif event.key == pygame.K_SPACE:
            if len(bullets) < settings.bullet_allowed:
                new_bullter = Bullet(ship, settings)
                bullets.add(new_bullter)

    def check_key_up(self, event, settings):
        # 判断上下左右
        if event.key == pygame.K_UP:
            settings.move_up = False
        elif event.key == pygame.K_DOWN:
            settings.move_down = False
        elif event.key == pygame.K_LEFT:
            settings.move_left = False
        elif event.key == pygame.K_RIGHT:
            settings.move_right = False

    def update_screen(self, screen, settings, bullets, ship):
        screen.fill(settings.screen_color)
        for bullet in bullets.sprites():
            bullet.draw_bullets(screen, bullet.color, bullet.bullet_rect)
        ship.ship_blit()
        pygame.display.flip()

    def update_bullets(self, bullets):
        bullets.update()
        for bullet in bullets.copy():
            if bullet.bullet_rect.left > 800:
                bullets.remove(bullet)


def run_game():
    # 初始化窗口
    pygame.init()
    # 初始化设置
    settings = Settings()
    # 初始化屏幕
    screen = pygame.display.set_mode(settings.screen_size)
    # 设置游戏名称
    pygame.display.set_caption('My ship')
    # 初始化飞船
    ship = Ship(screen)
    # 初始化子弹
    bullet = Bullet(ship, settings)
    bullets = Group()
    # 初始化游戏逻辑控制功能
    gf = GameFunctions()

    while True:
        # 循环监控屏幕内的事件
        gf.check_events(settings, bullets, ship)
        ship.update(settings)
        bullet.update()
        gf.update_bullets(bullets)
        gf.update_screen(screen, settings, bullets, ship)


if __name__ == '__main__':
    run_game()
