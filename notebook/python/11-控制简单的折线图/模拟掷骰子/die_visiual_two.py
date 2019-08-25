import pygal
from die import Die

# 创建两个D6骰子
die_1 = Die()
die_2 = Die(10)

results = []
for roll_num in range(5000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# 分析结果
frequencies = []
x_axis = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result +1):
    frequency = results.count(value)
    frequencies.append(frequency)
    x_axis.append(str(value))

# 可视化结果
hist = pygal.Bar()

hist.title = "Results of Rolling Two D6 Dice 1000 Times"

hist.x_labels = x_axis
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D10+D6', frequencies)
hist.render_to_file('dice_D10_visiual.svg')



