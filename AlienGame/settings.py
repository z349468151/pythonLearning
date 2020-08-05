class Settings(object):
    """游戏中所有设置"""

    def __init__(self):
        # 设置背景色
        self.bg_color = 230, 230, 230
        # 设置屏幕大小
        self.screen_height = 600
        self.screen_width = 800
        # 飞船的设置
        self.ship_limit = 3
        # 子弹的设置
        self.bullet_speed_factor = 1
        self.bullet_wide = 300
        self.bullet_height = 10
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        # 外星人的速度
        self.fleet_drop_speed = 5

        # 以什么样的速度加快游戏节奏
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行二变化的设置"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 0.4
        # fleet_direction为1表示右移，-1左移
        self.fleet_direction = 1
        # 计分
        self.alien_points = 50
        self.score_scale = 1.5

    def increase_speed(self):
        """提高速度设置和击杀外星人的分值"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
