#_*_coding:utf-8_*_

product = [
    ['apple', 5000],
    ['ipad', 3000],
    ['huawei', 4000],
    ['xiaomi', 2999],
    ['cat', 2000],
    ['coffee', 35],
    ['shoes', 300],
    ['wallet', 100]
]

salary = 10000
shops = []

while True:
    for index,p in enumerate(product):
        print (index, p[0], p[1])
    choice = input('请选择你需要的商品：')
    if choice.isdigit():
        choice = int(choice)
        if choice >= 8 or choice < 0:
            print('选择的商品不存在，请重新选择！')
            continue
        else:
            salary -= product[choice][1]
            if salary < 0:
                print('你钱包没钱了，请充值后再来！')
                break
            else:
                print('你的钱包剩余：\033[31;1m%s\033[0m' %(salary))
                print('你选择的商品' + product[choice][0] + '已经加入购物车。')

            shops.append(product[choice])
            print('你的购物车里有：', shops)
    elif choice == 'quit':
        print('欢迎下次再来！')
        break
    else:
        print ('你选择的是无效，重新选择！')

    


