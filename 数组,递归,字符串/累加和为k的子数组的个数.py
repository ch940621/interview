# 给一个k值,求出数组中存在的子数组的累加和为k的子数组的个数

# 和子数组之和整除k的思路很像
# map里面存 sum出现的次数,
# 然后遍历的时候去查map,如果能在map中找到sum-taget的值,说明当时每次能map[sum] += 1的位置和当前表遍历的位置组成的子数组符合要求
# res += map[sum - target]就可以了
def count_of_sum_of_subarray_equal_k(nums, target):
    length = len(nums)
    if length == 0:
        return 0
    map = {0:1}  # 初始化
    sum, res = 0, 0

    for pos in range(length):
        sum += nums[pos]
        if sum - target in map:
            res += map[sum - target]
        if sum not in map:
            map[sum] = 1
        else:
            map[sum] += 1

    return res


print(count_of_sum_of_subarray_equal_k([1,2,3,4,5,6,7,8,9,10],10))
