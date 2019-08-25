# 在固定文件中可以用于替换等长字符串

f = open('passwd', 'r+')
find_str = 'nobody'
new_str = 'husong'

isflag = True
i = 1

while isflag:
    line = f.readline() 
    print (i, line)
    if find_str in line:
        isflag = False
        print (i, line, sep='-->')
        new_line = line.replace(find_str, 'husong')
        print('the new line: ', new_line)
        new_pos = f.tell() - len(line)
        f.seek(new_pos)
        f.write(new_line)  

print ('this is close', f.tell())    
f.close()


