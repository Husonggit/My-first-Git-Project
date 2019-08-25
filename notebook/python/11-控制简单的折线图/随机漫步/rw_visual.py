import matplotlib.pyplot as plt

from random_walk import RandomWalk


#只要程序处于活跃状态就不断的模拟随机漫步
while True:
    #创建一个RandomWalk的实例，并将其包含的点都绘制出来
    rw = RandomWalk(50000)
    rw.fill_walk()

    # 设置绘制窗口的尺寸，如果知道系统分辨率可以加上dpi=128
    plt.figure(figsize=(20, 12))
    # 绘制点并将图形显示出来
    point_numbers = list(range(rw.num_points))
    # 加上颜色映射
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Reds, edgecolor='none', s=1)

    #加上起点和终点，并突出显示其颜色
    plt.scatter(0, 0, c='Orange', edgecolors=None, s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='Green', edgecolors=None, s=50)

    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()

    
    keep_running = input('Make another walk? (y/n): ')
    if keep_running == 'n':
        break
