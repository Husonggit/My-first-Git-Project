
filename = "/Users/husong/Desktop/notebook/python/10-文件和异常/file_of_test"

with open(filename) as file_object:
    line = file_object.read()
    print("------first read------")
    print(line.strip())

with open(filename) as file_object:
    print("------Second read-----")
    line2 = file_object.readlines()
    for line in line2:
        print(line.strip())

word = ''
with open(filename) as file_object:
    line3 = file_object.readlines()

for line in line3:
    word += line.strip()

print("------Third read--------")
print(word)
