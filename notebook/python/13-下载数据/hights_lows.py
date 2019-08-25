import csv
from matplotlib import pyplot as plt


filename = '/Users/hs/Desktop/notebook/python/13-下载数据/sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)
    
    # 从文件中读取最高温
    highs = []
    for row in reader:
        highs.append(int(row[1]))
    
    print(highs)
    fg = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(highs, c='red')

    #设置图形的格式
    plt.title("Daily High temperatures, July 2014", fontsize=24)
    plt.xlabel("", fontsize=16)
    plt.ylabel("Temperature(F)", fontsize=16)

    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()

    """ for index, high_temp in enumerate(highs):
        print(index, high_temp) """
# 使用枚举获取每个元素的索引及其值    
""" for index, column_header in enumerate(header_row):
    print(index, column_header) """

