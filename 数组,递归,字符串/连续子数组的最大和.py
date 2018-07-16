# 首先明确下概念,子数字必须连续

# 动态规划
# 用nums代表输入,dp[i]表示nums[i]为结尾的最大和
# dp[i+1] = max(dp[i]+nums[i+1],nums[i+1])
def get_max_sum_of_subarray(list1):
    if len(list1) == 0:
        return None
    max_sum = list1[0]
    cur_sum = list1[0]
    for i in range(1,len(list1)):
        cur_sum = max(cur_sum + list1[i],list1[i])
        max_sum = max(cur_sum,max_sum)

    return max_sum

print(get_max_sum_of_subarray([-10,-11]))

# -float('inf')为最小的数
def get_max_sum_of_subarray1(list1):
    if len(list1) == 0:
        return None
    min_int = -float('inf')
    max_sum = min_int
    cur_sum = min_int
    for i in range(0,len(list1)):
        cur_sum = max(cur_sum + list1[i],list1[i])
        max_sum = max(cur_sum,max_sum)

    return max_sum

print(get_max_sum_of_subarray1([-10,-11]))

