
def find_more_than_half(nums):
    if len(nums) == 0:
        return None
    res = nums[0]
    count = 1
    for pos in range(1,len(nums)):
        if count == 0:
            res = nums[pos]
            count += 1
        else:
            if res == nums[pos]:
                count += 1
            else:
                count -= 1
    if count >= len(nums) // 2:
        return res
    else:
        return None


print(find_more_than_half([1,2,3,4,5,5,5,5,6]))