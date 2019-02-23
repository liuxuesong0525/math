#在一个py文件中写函数实现文件的复制，在另个py文件中调用
def txt_line(linename,writename):
    with open(linename,"r") as f:
        str=f.read()
        print(str)
    with open(writename,"w") as e:
        e.write()
