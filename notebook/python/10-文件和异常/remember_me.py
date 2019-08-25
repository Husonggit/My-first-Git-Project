import json

def greet_user():
    """ 问候用户，并指出其名字 """
    
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        username = json.load(f_obj)

    return username

filename = 'name.json'
user_name = input("What's you name: ")

with open(filename, 'w') as f_obj:
    json.dump(user_name, f_obj)

#方式一：调用函数
name = greet_user()
print ('hello ' + name + ' nice to meet you!')

#方式二：直接使用
with open(filename) as f_obj:
    number2 = json.load(f_obj)
    print('hello, ' + number2)