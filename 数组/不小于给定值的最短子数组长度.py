# 这个题目要求子数组的和 >= k 。 求最小的子数组长度。
# 所有的数为正数

def get_min_length_of_subarray_greater_than_k(nums, target):
    length = len(nums)
    if length == 0:
        return None
    res = length + 1
    left, right = 0, 0
    sum = nums[0]
    while right <= length - 1:
        while sum < target and right <= length - 1:
            sum += nums[right]
            right += 1
        while sum >= target:
            res = min(res, right - left + 1)
            sum -= nums[left]
            left += 1

    return res if res != length + 1 else None



print(get_min_length_of_subarray_greater_than_k([1,1,3,1,1,1,1,1],6))
