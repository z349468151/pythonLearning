import matplotlib.pyplot as plt
from matplotlibTest.random_walk import RandomWalk

while True:
    # 创建一个RW实例，并将其包含的点都绘制出来
    rw = RandomWalk(5000)
    rw.fill_walk()
    point_numbers = list(range(rw.num_points))
    # 突出显示起点终点
    # plt.scatter(0, 0, c='red', edgecolors='none', s=100)
    # plt.scatter(rw.x_value[-1], rw.y_value[-1], c='red', edgecolors='none', s=100)
    # plt.scatter(rw.x_value, rw.y_value, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)
    plt.plot(rw.x_value, rw.y_value, linewidth=15)
    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()
    keep_running = input("Make another walk?(y/n):")
    if keep_running == 'n':
        break
