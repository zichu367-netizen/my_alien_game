class Settings:
    def __init__(self):
        # 屏幕尺寸
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (240, 240, 240)

        # 飞船速度
        self.ship_speed = 3

        # 子弹（玩家）
        self.bullet_speed = 7
        self.bullets_allowed = 5

        # 外星人
        self.alien_speed = 1
        self.fleet_drop_speed = 20
        self.fleet_direction = 1  # 1 = 右 ; -1 = 左

        # 外星人子弹
        self.alien_bullet_speed = 4
        self.alien_shoot_chance = 120  # 概率 1/n
