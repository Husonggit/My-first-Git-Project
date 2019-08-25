import sys
""" 替换文件中的指定字符串 src dec """


if '-r' in sys.argv:
    rep_argv_pos = sys.argv.index('-r')
    find_str = sys.argv[rep_argv_pos + 1]
    print ('-->find str:', find_str)
    new_str = sys.argv[rep_argv_pos + 2]
    print ('-->new_str:', new_str)

f = open('passwd', 'r+')
while True:
    line = f.readline()
    if find_str in line:
        new_line = line.replace(find_str, new_str)
        new_pos = f.tell() - len(line)
        f.seek(new_pos)
        f.write(new_line)
        break

f.close()
print ('---The replace is over---')
        
