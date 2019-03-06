#判断一个字符串是否为对称字符串（20分）用函数形式进行操作完成
def hanshu(str):
    if str ==str[::-1]:
        print("是对称字符串")
    else:
        print("不是对称字符串")
hanshu("abgba")