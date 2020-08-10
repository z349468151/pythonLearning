from random import choice


class RandomWalk(object):
    """生成一个随机漫步数据的类"""

    def __init__(self, num_points=5000):
        """初始化随机漫步的属性"""
        self.num_points = num_points

        # 所有随机漫步都始于（0，0）
        self.x_value = [0]
        self.y_value = [0]

    def fill_walk(self):
        """计算随机漫步包含的所有点"""
        # 不断漫步，直到列表达到指定的长度
        while len(self.x_value) < self.num_points:
            x_step, y_step = self.get_step()
            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            # 计算下一个点的x,y值
            next_x = self.x_value[-1] + x_step
            next_y = self.y_value[-1] + y_step
            self.x_value.append(next_x)
            self.y_value.append(next_y)

    def get_step(self):
        # 决定前进方向以及沿这个方向前进的距离
        x_direction = choice([1, -1])
        x_distance = choice([x for x in range(1, 9)])
        x_step = x_direction * x_distance
        y_direction = choice([1, -1])
        y_distance = choice([y for y in range(1, 9)])
        y_step = y_direction * y_distance
        return x_step, y_step
