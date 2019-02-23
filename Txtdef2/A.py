#在一个py文件中写读写文件的代码，在另一个py文件中调用
def txt_line(linename,writename):
    with open(linename,"a+") as f:
        f.seek(0)
        str=f.read()
        print(str)
    with open(writename,"w") as e:
        e.seek(0)
        e.write(str)