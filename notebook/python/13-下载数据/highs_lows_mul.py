# coding = utf-8

import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename = '/Users/hs/Desktop/My-first-Git-Project/notebook/python/13-下载数据/death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    head_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing date')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
        
    # print(dates)
    # print(highs)
    # 根据数据绘制图形
    fig  = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates, highs, c='red', alpha=0.5)
    plt.plot(dates, lows, c='blue', alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='yellow', alpha=0.1)

    # 设置图形绘制图形
    plt.title('Daily high templeratures, July 2014', fontsize=24)
    plt.xlabel('', fontsize=16)

    fig.autofmt_xdate()
    plt.ylabel('Temperature(F)', fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()