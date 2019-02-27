#2.	读入文件‘a.txt’.统计文件中每个单词的数量并且进行输出。
#txt的文本文件为
#a = "Every single time you access a website,you leave tracks.Tracks that others can access.If you don't like the idea,find out what software can help you cover them"
d = {}
count = 0
f = open("D://a.txt","r")
a = f.readlines()
a = str(a)
f.close()
print("文件中的字符串是：",a)
str0 = a.replace(","," ").replace("."," ")
q=str0.split(" ")
for i in q:
    d[i] = q.count(i)

print(d)