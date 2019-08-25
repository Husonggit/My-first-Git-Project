#_*_coding:utf-8_*_

def auth(function):
    def wrapper(name):
        user = input("input passwd: ").strip()
        if user == 'husong':
            print("----Welcome login---")
            function(name)
        else:
            print("----Wrong passwd, assess denied---")
        
    return wrapper

@auth

def task(name):
    print("do something....." + name)
def task2():
    print("do something.....2")
def task3():
    print("do something.....3")

#方式一：
# task = auth(task)
# task()

#方式二：
task('run python')
#task2()
#task3()
