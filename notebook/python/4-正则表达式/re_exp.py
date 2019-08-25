import re

""" 正则表达式 介绍 及用法 """

a = 'ashdlf&(*2()fewqm,nafds~!Eaodfhhkaewpoi'

#匹配字母和数字
m = re.match('\w+', a)

print(m.group())

m = re.match('[a-zA-Z+', a)
print(m.group())

re.search()
re.findall()
re.split()





