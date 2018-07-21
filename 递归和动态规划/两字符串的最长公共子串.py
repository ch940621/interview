# dp[i][j]表示串str1的前i个字符组成的串和串str2的前j个字符组成的串的最大公共子串的长度


# 两层for循环遍历构造dp数组,每次dp在两个指针对于的字母相等的时候更新,等于斜上方的值+1,如果没有斜上方就赋值为1

# 以"abcabcfgabc", "aabcfgh"为例子,数组如下
# [1, 1, 0, 0, 0, 0, 0]
# [0, 0, 2, 0, 0, 0, 0]
# [0, 0, 0, 3, 0, 0, 0]
# [1, 1, 0, 0, 0, 0, 0]
# [0, 0, 2, 0, 0, 0, 0]
# [0, 0, 0, 3, 0, 0, 0]
# [0, 0, 0, 0, 4, 0, 0]
# [0, 0, 0, 0, 0, 5, 0]
# [1, 1, 0, 0, 0, 0, 0]
# [0, 0, 2, 0, 0, 0, 0]
# [0, 0, 0, 3, 0, 0, 0]

def get_substr_with_max_length_form_two_strs(str1, str2):
    res = ''
    if str1 == '' or str2 == '' or str1 == None or str2 == None:
        return res

    len1 = len(str1)
    len2 = len(str2)
    len_max = 0
    dp = [[0 for pos2 in range(len2)] for pos1 in range(len1)]
    for pos1 in range(len1):
        for pos2 in range(len2):
            if str1[pos1] == str2[pos2]:
                # 边界处理
                if pos1 == 0 or pos2 == 0:
                    dp[pos1][pos2] = 1
                else:
                    dp[pos1][pos2] += dp[pos1 - 1][pos2 - 1] + 1
                if dp[pos1][pos2] > len_max:
                    len_max = dp[pos1][pos2]
                    res = str2[pos2 - dp[pos1][pos2] + 1:pos2 + 1]
    print(dp)
    return res


print(get_substr_with_max_length_form_two_strs("abcabcfgabc", "aabcfgh"))
