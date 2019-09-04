import json
import pygal
import math

filename = 'btc_close_2017.json'
with open(filename) as f:
    btc_data = json.load(f)

# 创建5个列表，存储日期和收价盘
dates,months,weeks,weekdays,closes=[],[],[],[],[]
# 以字典的形式将json中的数据拿出来
for btc_dict in btc_data:
    # date = btc_dict['date']
    # month = int(btc_dict['month'])
    # week = int(btc_dict['week'])
    # weekday = btc_dict['weekday']
    # close = int(float(btc_dict['close']))
    # 打印每一天的信息
    # print("{} is month {} week {}, {}, the close price is {} RMB.".format(date, month, week, weekday, close))

    dates.append(btc_dict['date'])
    months.append(int(btc_dict['month']))
    weeks.append(int(btc_dict['week']))
    weekdays.append(btc_dict['weekday'])
    closes.append(int(float(btc_dict['close'])))


line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
line_chart.title = '收盘价（￥）'
line_chart.x_labels = dates
N = 20
line_chart.x_labels_major = dates[::N]
line_chart.add('收盘价', closes)
line_chart.render_to_file('收盘价折线图（￥）.svg')

# 发现趋势，周期性，噪声，先消除非线性的趋势，进行对数变换
line_chart2 = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
line_chart2.title = '收盘价对数变换（￥）'
line_chart2.x_labels = dates
line_chart2.x_labels_major = dates[::N]
close_log = [math.log10(_) for _ in closes]
line_chart2.add('log收盘价', close_log)
line_chart2.render_to_file('收盘价对数变换折线图（￥）.svg')