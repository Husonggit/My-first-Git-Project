class Dog():
    """ 一次模拟小狗的简单尝试 """

    def __init__(self, name, age):
        """初始化属性name和age """
        self.name = name
        self.age = age 

    def sit(self):
        """模拟小狗被命令 蹲下 """
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """模拟小狗被命令 打滚"""
        print(self.name.title() + " is now rolled over!")


my_dog = Dog('wille', 6)
your_dog = Dog('lucy', 3)

my_dog.sit()
my_dog.roll_over()
your_dog.sit()
your_dog.roll_over()


print("My dog name is " + my_dog.name.title() + ".")
print("Your dog name is " + your_dog.name.title() + ".")

print("My dog age is " + str(my_dog.age) + ".")
print("Your dog age is " + str(your_dog.age) + ".")