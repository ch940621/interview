# 可以用dp,但是本题dp没有更快,不能为了dp而dp
# 中心思想扩散,找一个 core ,可以是 aa, 或者a 这种单字符或者双一样的字符,然后向外扩散,扩散的时候记录一下长度


def get_longest(str1):
    assert str1 != None
    if len(str1) in [0, 1]:
        return str1

    res = ''
    for pos in range(len(str1)):
        res = check_and_expand(str1, pos, pos,res)
        res = check_and_expand(str1,pos,pos+1,res)
    return res


def check_and_expand(str1, left, right, res):
    while left >= 0 and right <= len(str1) - 1:
        if str1[left] == str1[right]:
            if right - left + 1 > len(res):
                res = str1[left:right + 1]
        left -= 1
        right += 1
    return res


print(get_longest("abccbd"))


# 有更吊的解决办法,马拉夫算法,以后再说