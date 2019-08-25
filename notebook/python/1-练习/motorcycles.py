
motorcyles = ['honda', 'yamaha', 'suzuki']
print("motorcyles = ", motorcyles)

#添加列表
#motorcyles[0] = 'ducati'
motorcyles.append('ducati')
print("motorcyles = ", motorcyles)

motorcyles2 = []
for i in range(4):
    motorcyles2.append(motorcyles[i].title())

print("motorcyles2 = ", motorcyles2)

#删除列表
del motorcyles2[0]
print("motorcyles2 = ", motorcyles2)

#弹出列表，并且可以接着使用值
popped_motorcyles = motorcyles.pop()
print("motorcyles = ", motorcyles)
print("popped_motorcyles = ", popped_motorcyles)

popped_motorcyles = motorcyles.pop()
print("motorcyles = ", motorcyles)
print("popped_motorcyles = ", popped_motorcyles)