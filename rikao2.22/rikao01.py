#通过用户输入数字，计算阶乘。（30分）
print("请输入一个数字")
num=int(input())
sum=0
f=1
for i in range(1,num+1):
    f=f*i
    sum+=f
print("阶乘为",sum)