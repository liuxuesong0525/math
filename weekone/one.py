#1.	生成100个范围在0-20的整数，并且能够打印输出
import random
list=[]
for i in range(100):
    list.append(random.randint(1,20))
print(list)