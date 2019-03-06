#生成一个有10个数的随机数组，判断每个数字出现的次数
import random
a = []
d = {}
for i in range(10):
    a.append(random.randint(1,50))
for i in a:
    d[i] = a.count(i)
print(d)