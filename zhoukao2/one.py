#1.	生成50个范围在0-80的整数，并且能够打印输出？
import random
list=[]
for i in range(50):
    list.append(random.randint(0,80))
print(list)