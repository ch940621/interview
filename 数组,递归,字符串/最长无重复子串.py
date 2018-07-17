## python的ASCII和字符的转换
# Get the ASCII number of a character
#number = ord(char)
## Get the character given by an ASCII number
# char = chr(number)

# 获取一个字符串的最长无重复子串,返回长度
# 思路,遍历字符串把字符和对应的位置存入哈希表map,遍历的过程中如果哈希表已经有了,用新的覆盖掉老的
# 一个初始指针 start = 0 标志子串的开始,子串的长度cur_len = pos - start + 1 被不断被更新
# 如果遍历的过程中遇到了当前的东西已经在map里面了,需要把start 置到map[str1[pos]]的后一个位置,也就置成是哈希表记录的这个字符的最近一次出现的位置+1
# 需要这样放置的原因是要继续count的话,就要避免子数组的字符重复

def get_longest_subarray_with_no_repeat(str1):
    assert str1 != None
    if len(str1) == 0:
        return 0
    res = 0
    cur_len = 0
    start = 0
    map = {}

    for pos in range(len(str1)):
        if str1[pos] in map and map[str1[pos]] >= start:
            start = map[str1[pos]] + 1
        cur_len = pos - start + 1
        map[str1[pos]] = pos
        res = max(res, cur_len)

    return res

print(get_longest_subarray_with_no_repeat("12341256787"))