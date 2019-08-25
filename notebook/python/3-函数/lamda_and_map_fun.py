#_*_coding:utf-8_*_
from functools import reduce


#01 lambda函数 == 匿名函数
add = lambda x,y : x+y
print (add(2, 4))

g = lambda x, y=2, z=4 : x*y+z
print(g(8))

#02 lambda表达式常用来编写跳转表（jump table），就是行为的列表或字典。

L = [(lambda x: x**2),  
    (lambda x: x**3),  
    (lambda x: x**4)]  
print (L[0](2),L[1](2),L[2](2))
  
D = {'f1':(lambda: 2+3),  
    'f2':(lambda: 2*3),  
    'f3':(lambda: 2**3)}  
print (D['f1'](),D['f2'](),D['f3']())

#03 嵌套使用 --函数编程 
# Python中，也有几个定义好的全局函数方便使用的，例如 map、reduce、filter、sorted这些函数都支持函数作为参数
foo = [2,18,22,31,42,81,9,80,33]
print("filter-->")
print(list(filter(lambda x : x % 3 == 0, foo)))

print("map-->")
print(list(map(lambda x : x**2, foo)))

print("reduce-->")
print(reduce(lambda x, y : x+y, foo))

#按key值排序
dic1 = {
    1:2,
    33:22,
    9:12
}
print(sorted(dic1.items(), key=lambda x : x[0]))


#04 闭包
def my_add(n):
    return lambda x : x + n

add_3 = my_add(3)
print(add_3(12))


#05 复杂函数
f = lambda x: [[y for j, y in enumerate(set(x)) if (i >> j) & 1] for i in range(2 ** len(set(x)))]
print(f('husong'))
