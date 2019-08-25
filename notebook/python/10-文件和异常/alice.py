import os
filename = '10-文件和异常/alice.tet'

print(os.getcwd())

try:
    with open(filename) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    # 失败是一声不吭
    pass
    # print("Sorry, the file does not exist.")
else:
    words = contents.split()
    num_words = len(words)

    print("The file " + filename + " has about " + str(num_words) + " words.")
    print(words)
