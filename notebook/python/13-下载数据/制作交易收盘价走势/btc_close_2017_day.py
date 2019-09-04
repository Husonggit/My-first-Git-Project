# coding=utf-8
import json
import pygal
import math


from itertools import groupby
def draw_line(x_date, y_data, title, y_legend):
    xy_map = []
    for x,y in groupby(sorted(zip(x_date, y_data), key=lambda _:_[0])):
        y_list = [v for _, v in y]
        xy_map.append([x, sum(y_list) / len(y_list)])
    x_unique, y_mean = [*zip(*xy_map)]
    line_chart = pygal.Line()
    line_chart.title = title
    line_chart.x_labels = x_unique
    line_chart.add(y_legend, y_mean)
    line_chart.render_to_file(title + '.svg')
    return line_chart

filename = 'btc_close_2017.json'
with open(filename) as f:
    btc_data = json.load(f)

    # 创建5个列表，存储日期和收价盘
    dates,months,weeks,weekdays,closes=[],[],[],[],[]
    # 以字典的形式将json中的数据拿出来
    for btc_dict in btc_data:
    
        dates.append(btc_dict['date'])
        months.append(int(btc_dict['month']))
        weeks.append(int(btc_dict['week']))
        weekdays.append(btc_dict['weekday'])
        closes.append(int(float(btc_dict['close'])))

idx_month = dates.index('2017-12-01')
print(type(months[:idx_month]))
print(type(closes[:idx_month]))
# line_chart_month = draw_line(months[:idx_month], closes[:idx_month], '收盘价月日均值（￥）', '月均值')
# line_chart_month