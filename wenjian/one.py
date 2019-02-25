#rb以二进制格式打开一个文件，用于只读
#rb+类似于rb但是可以读写

f=open("mo.png",'rb')
a=f.read()
f.close()
k=open("mo_o.png",'wb')
k.write(a)
k.close()
print("成功")
