#编写一个函数，判断一个字符串是否为回文，如果是回文返回整数1，否则返回返 回整数0（20分）
#	回文：就是前后对称。例如：”abba”，”evilolive”是回文，”abxd”和”efga”不是回文
def str_name(str):
    if len(str)%2 == 0:
        str1 = str[:len(str)//2]
        str2 = str[len(str)//2:]
        str1 = list(str1)
        str2 = list(str2)
        str2.reverse()
        if str2 == str1:
            return 1
        else:
            return 0
    elif len(str)%2 != 0:
        str3 = str[:len(str) // 2+1]
        str4 = str[len(str) // 2:]
        str3 = list(str3)
        str4 = list(str4)
        str4.reverse()
        if str4 == str3:
            return 1
        else:
            return 0
print(str_name('abcba'))