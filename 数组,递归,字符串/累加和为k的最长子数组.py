# 思路非常巧妙,可以理解为两数之和和子数组累加和问题的融合
# 用指针i遍历数组,遍历的时候用sum记录nums[i]的累加和,并把第一次出现的sum值和对于的位置存到map里面
# 其实就找两个点 第一个点的值为 sum-target,第二个点的值为sum,第一个点的位置为map[sum-target],第二个点的位置为i

def get_max_length_of_subarray_quuals_k(nums, target):
    sum, res = 0, 0
    map = {}
    for i in range(len(nums)):
        sum += nums[i]
        if sum == target:
            res = i + 1
        elif sum - target in map:
            res = max(res, i - map[sum - target])
        if sum not in map:
            map[sum] = i

    return res




print(get_max_length_of_subarray_quuals_k([1,2,3,4,5,6,7,8,9],10))
