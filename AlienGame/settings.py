class Settings(object):
    '''游戏中所有设置'''

    def __init__(self):
        # 设置背景色
        self.bg_color = 230, 230, 230
        # 设置屏幕大小
        self.screen_height = 600
        self.screen_width = 800
        # 飞船的设置
        self.ship_speed_factor = 1.5
        # 子弹的设置
        self.bullet_speed_factor = 1
        self.bullet_wide = 3
        self.bullet_hight = 10
        self.bullen_color = 60, 60, 60
        self.bullets_allowed = 3
        # 外星人的速度
        self.alien_speed_factor = 1
