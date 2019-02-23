def read_line(linename,writename):
    with open(linename,'r') as f:#a+  用seek（0）
        #f.seek(0) #开头位置
        str=f.read()
        print(str)
    with open(writename,'w') as e:
       # e.seek(0) #开头位置
        e.write(str)
#read_line("D://hello.txt")
