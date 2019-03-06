# 2.	读入文件‘monday.txt’.统计文件中每个单词的数量并且进行输出。
# txt的文本文件为
# 然后再将下面一段文字加入到Monday.txt中然后进行输出
# ‘张三 18 99分
#  李四   23  97分
#  王小六 26   67分
#  二妮   37   45’
# 添加文字用函数进行添加
d = {}
f = open("D://monday.txt","r")
e = f.readlines()
e=str(e)
f.close()
q=e.replace("."," ")
q=e.split(" ")
for i in q:
    d[i] = q.count(i)
print(d)
#Python is easy.Python is easy.Python is easy.
str0 = "张三 18 99分,李四   23  97分,王小六 26   67分,二妮   37   45"
def line_name(str0):
    a = open("D://monday.txt","a+")
    a.writelines(str0)
line_name(str0)
print("添加成功")