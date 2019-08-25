filename = "/Users/husong/Desktop/notebook/python/10-文件和异常/file_of_test"

# with open(filename, 'w') as file_object:
#     file_object.write("I love you, and you? ")

write_line = ''
with open(filename, 'a') as file_object:
    write_line = input("Please your name!")
    file_object.write(write_line)
    file_object.write('\n')
    
    
with open(filename) as file_object:    
    lines = file_object.readlines()
    for line in lines:
        print(line)
        if line.strip() == 'Dawei':
            print("There is Dawei!")
        else:
            print("There isn't Dawei!")
