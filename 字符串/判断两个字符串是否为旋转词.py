# 一个str串全的前面任意部分挪到后面变成的串叫str的旋转词
# "abcd" 和 "cdab"就互为旋转词
# 用O(N)的复杂度判断两个词是否旋转词

# 思路: 把 cdab给double一下变成'cdabcdab' 如果 abcd是其double后的子串,满足条件

# 子串的查找可以使用KMP算法,KMP算法另外整理,这里面就用Python封装好的in来实现

#
def is_reserve_str(str1,str2):
    if len(str1) != len(str2):
        return False
    double_str2 = str2 + str2
    return str1 in double_str2


print(is_reserve_str("abcd","cdab"))

print(is_reserve_str("abcd","dacb"))