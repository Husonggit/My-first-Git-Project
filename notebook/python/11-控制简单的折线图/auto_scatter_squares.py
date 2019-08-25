import matplotlib.pyplot as plt

x_value = list(range(0, 1001))
y_value = [x**2 for x in x_value]

# edgecolor 表示是否打印轮廓颜色，c表示RGB颜色模式，越接近1颜色越浅，越接近0颜色越深
# plt.scatter(x_value, y_value, c=(0.5,0.9,0.8), edgecolor='none', s=40)

#使用颜色映射 cmp 指定是什么颜色映射
plt.scatter(x_value, y_value, c=y_value, cmap=plt.cm.Reds, edgecolor='none', s=40)


#设置图表标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of value", fontsize=14)

#设置坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])

#设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()

#自动保存图表，文件名+是否保存旁边多余的空白区域
#plt.savefig('husong.png'， , bbox_inches='tight')