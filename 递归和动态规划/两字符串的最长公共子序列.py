# 是最长公共子串的变种,也是用dp来存遍历到dp[pos1][pos2]的时候最长公共子序列的长度
# 但dp数组的更新方式不一样了
# 如果两次遍历构造dp的时候str1[pos1] == str2[pos2]的时候代表有是连续的,取的结果不需要跳
# 如果str1[pos1] != str2[pos2]并不代表后续没有好的结果,需要继承上方或者左方较大的一个dp值
# 继承上方的表示取串的时候要跳过str1[pos1],继承左方的表示取串的时候要跳过str2[pso2]
# 为了正确地把子序列取出来这个dp数组的更新方向也是需要另外一个数组存好的

# "abcbdab", "bdcaba"为例,结果应该为bcba 和bdab
# 我打代码结果为bdab,网上的多为bcba

# [0, 0, 0, 1, 1, 1],
# [1, 1, 1, 1, 2, 2],
# [1, 1, 2, 2, 2, 2],
# [1, 1, 2, 2, 3, 3],
# [1, 2, 2, 2, 3, 3],
# [1, 2, 2, 3, 3, 4],
# [1, 2, 2, 3, 4, 4]


# [None, 'left', 'left', 'left_up', 'left', 'left_up'], 
# ['left_up', 'left', 'left', 'left', 'left_up', 'left'], 
# ['up', 'left', 'left_up', 'left', 'left', 'left'], 
# ['left_up', 'left', 'up', 'left', 'left_up', 'left'], 
# ['up', 'left_up', 'left', 'left', 'up', 'left'], 
# ['up', 'up', 'left', 'left_up', 'left', 'left_up'], 
# ['left_up', 'up', 'left', 'up', 'left_up', 'left']

# 要注意的是我这个例子其实有两个答案,但是在左和上的dp值一样的情况下,我们必须取一个,是取上,还是取左,子序列是不一样的,因为路径不一样,但是长度是一样的

def get_dp_of_subsequence_with_max_length_from_two_strs(str1, str2):
    res = ''
    if str1 == '' or str2 == '' or str1 == None or str2 == None:
        return res

    len1 = len(str1)
    len2 = len(str2)

    dp = [[0 for pos2 in range(len2)] for pos1 in range(len1)]
    flag = [[None for pos2 in range(len2)] for pos1 in range(len1)]

    for pos1 in range(len1):
        for pos2 in range(len2):
            if str1[pos1] == str2[pos2]:
                # 边界处理
                if pos1 == 0 or pos2 == 0:
                    dp[pos1][pos2] = 1
                else:
                    dp[pos1][pos2] += dp[pos1 - 1][pos2 - 1] + 1
                flag[pos1][pos2] = 'left_up'
            else:
                # 边界处理

                if pos1 != 0 and pos2 != 0:

                    if dp[pos1 - 1][pos2] > dp[pos1][pos2 - 1]:
                        dp[pos1][pos2] = dp[pos1 - 1][pos2]
                        flag[pos1][pos2] = 'up'
                    else:
                        dp[pos1][pos2] = dp[pos1][pos2 - 1]
                        flag[pos1][pos2] = 'left'
                        

                else:
                    if pos1 == 0 and pos2 != 0:
                        dp[pos1][pos2] = dp[pos1][pos2 - 1]
                        flag[pos1][pos2] = "left"
                    elif pos1 != 0 and pos2 == 0:
                        dp[pos1][pos2] = dp[pos1 - 1][pos2]
                        flag[pos1][pos2] = "up"

    return dp, flag


def get_subsequence_with_max_length_from_two_strs(str1, str2):
    dp, flag = get_dp_of_subsequence_with_max_length_from_two_strs(str1, str2)
    
    # 最长公共子序列的长度
    # print(dp[len(str1) - 1][len(str2) - 1])

    pos1 = len(str1) - 1
    pos2 = len(str2) - 1

    new_str1 = []
    new_str2 = []

    while pos1 != 0 and pos2 != 0:
        if flag[pos1][pos2] == "left":
            pos2 -= 1

        elif flag[pos1][pos2] == "up":
            pos1 -= 1
        else:
            new_str1.append(str1[pos1])
            new_str2.append(str2[pos2])
            pos1 -= 1
            pos2 -= 1
        

    if dp[pos1][pos2] == 1:
        new_str1.append(str1[pos1])
        new_str2.append(str2[pos2])

    new_str1 = ''.join(new_str1[::-1])
    new_str2 = ''.join(new_str2[::-1])

    return new_str1



print(get_subsequence_with_max_length_from_two_strs("abcbdab", "bdcaba"))
