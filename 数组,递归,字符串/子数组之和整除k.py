# 给定一个数组能寻找到一个子数组的长度至少为2的累加和能够被k整除的子数组,如果是返回真,找不到返回假
# 这里面用到了一个数学技巧,若数字a和b分别除以数字c，若得到的余数相同，那么(a-b)必定能够整除c
# 题目思路为在一个数组nums中,找到两个指针,pos1,pos2,使得sum[pos1] % k == sum[pos2] % k
# 用哈希表可以完成一次遍历就可以找到


# 要注意边界值处理,算好的pos1,pos2,咱们用pos2位置的累加和-pos1位置的累加和
# 其实得到的是(pos1,pos2]这段的也就是[pos1+1,pos2]
# 所以长度计算是 pos - (map[remainder] + 1) + 1
def exist_sum_of_subarray_division_k(nums, k):
    length = len(nums)

    if k == 0 or length == 0:
        return None
    map = {}
    sum = 0
    for pos in range(length):
        sum += nums[pos]
        remainder = sum % k
        if remainder in map:

            if pos - (map[remainder] + 1) + 1 >= 2:  # 题目的长度限制
                return True

        else:
            map[remainder] = pos

    return False

print(exist_sum_of_subarray_division_k([1, 2, 3, 4, 5, 6, 1, 12], 13))
