import pickle

""" 数据类型序列化:持久化的储存数据 """

dic1 = {'name':'husong',
        'age':123,
        'bronth':1992
}

# f = open('ID.pkl', 'w')  # 写入时是以二进制格式写入的，若以’w'的形式写入的话会报错


#a = {"name": "Tom", "age": "40"}
file = open('ID.pkl', 'wb')  
pickle.dump(dic1, file)

file.close()

file2 = open('ID.pkl', 'rb')
b = pickle.load(file2)

print(type(b))
print(b)

file2.close()
