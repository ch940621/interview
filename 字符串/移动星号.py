# 一个字符串只包含 * 和数字，请把它的 * 都放在开头

# 1 * 2 * 4 * 3 => * * * 1 2 4 3
# 从后到前操作思路
# 还是要注意边界值


def move_star_char(str1):
    assert str1 != None
    str1 = list(str1)
    if len(str1) == 0:
        return None
    new_pos = len(str1) - 1
    for pos in range(len(str1)):
        pos = (len(str1) - 1) - pos
        if str1[pos] != "*":
            str1[new_pos] = str1[pos]
            new_pos -= 1

    if new_pos != 0:
        str1[:new_pos+1] = "*" * (new_pos - 0 + 1)

    return "".join(str1)


print(move_star_char("1*2*4*3"))
