# 子数组最大和的变种
# 
# 用两个dp数组，其中dp_max[i]表示子数组[0, i]范围内的最大子数组乘积
# dp_min[i]表示子数组[0, i]范围内的最小子数组乘积
# 
# 最大的乘积比如出现在 dp_max[i-1]*nums[i]，dp_min[i-1]*nums[i]，和nums[i]中
# 状态更新方程为
# dp_max[i] = max(max(dp_max[i - 1] * nums[i], dp_min[i - 1] * nums[i]), nums[i])
# dp_min[i] = min(min(dp_max[i - 1] * nums[i], dp_min[i - 1] * nums[i]), nums[i])


def get_max_product_of_subarray(nums):
    if len(nums) == 0:
        return None
    dp_max,dp_min = [0]*len(nums),[0]*len(nums)
    dp_max[0],dp_min[0] = nums[0],nums[0]
    res = dp_max[0]
    for i in range(1,len(nums)):
        dp_max[i] = max(max(dp_max[i - 1] * nums[i], dp_min[i - 1] * nums[i]), nums[i])
        dp_min[i] = min(min(dp_max[i - 1] * nums[i], dp_min[i - 1] * nums[i]), nums[i]) 

        res = max(res,dp_max[i])

    return res

print(get_max_product_of_subarray([1,2,3,4,5,6,-7,-8]))