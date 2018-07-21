# 两个由字母组成的字符串,问前一个串的字母是不是都出现在后一个中

# 直观的思路是哈希,但是不符合面试官的要求,空间很浪费,而且没有利用好字母组成的那个条件

# 哈希大法
def string_contains(str_cur,str_target):
    char_set = {str_target}
    for char in str_cur:
        if char not in str_target:
            return False
    return True

print(string_contains('abcdz','abcdefg'))

# ## python的ASCII和字符的转换
# Get the ASCII number of a character
#number = ord(char)
## Get the character given by an ASCII number
# char = chr(number)

# 哈希虽好但是浪费空间,用一个数来表示哈希表,用位运算来更新哈希表
def string_contains1(str_cur,str_target):
    length_cur = len(str_cur)
    length_target = len(str_target)

    hash_num = 0
    for pos in range(length_target):
        hash_num |= 1 << (ord(str_target[pos]) - ord('A'))
    for pos in range(length_cur):
        if hash_num & (1 << (ord(str_cur[pos]) - ord('A'))) == 0:
            return False
    return True

print(string_contains1('abcd','abcdefg'))
