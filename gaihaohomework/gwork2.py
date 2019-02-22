#判断101-200之间有多少个素数，并输出所有素数。
#程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，
# 如果能被整除，则表明此数不是素数，反之是素数。（30分）
import math
count=0
for i in range(101,200):
    b=0
    for j in range(2,math.sqrt(i)):
        if i % j ==0:
            b=1
            break
        if b == 0:
            count+=1
            print(i)
print("素数共有",count,"个")