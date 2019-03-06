#1.	生成20个范围在1-200的整数，并且能够打印输出？
import random
list = []
for i in range(20):
    list.append(random.randint(1,200))
print(list)