# 必须要为k个,如果大于k个不去掉
# 注意两个边界值,一个是 确定了已经是k个了,要修改的子串的pos 和start的位置确定好,子串长度确定好
# 第二个是最后的一段符合要求的子串如果是在字符串结尾,那么无法被确定,需要再判断一次,这个时候的边界位置就不一样了哦


def remove_k_0_from_str(str1, k):
    assert str1 != None
    assert k > 0
    start = -1
    count = 0
    str1 = list(str1)
    for pos in range(len(str1)):
        if str1[pos] == '0':
            start = pos if start == -1 else start
            count += 1

        else:
            if count == k:
                str1[start:pos] = "*" * (pos - start)
            start = -1
            count = 0

    if count == k:
        str1[start:] = "*" * (pos - start + 1)

    # 删除所有的'*'
    new_pos = 0
    new_len = 0
    for pos in range(len(str1)):
        if str1[pos] != '*':
            new_len += 1
            str1[new_pos] = str1[pos]
            new_pos += 1    
    str1 = str1[:new_len]



    return ''.join(str1)


print(remove_k_0_from_str("000A00B000AB000", 3))
