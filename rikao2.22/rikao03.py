#.将一个列表的数据复制到另一个列表中，并反向排序输出
import random
list=[]
list1=[]
for i in range(20):
    list.append(random.randint(1,100))
list1=list[:]
#list1=list.copy()
#list1=list(list)   工厂函数
list1.sort()
list1.reverse()
print("原列表",list)
print("新列表",list1)

