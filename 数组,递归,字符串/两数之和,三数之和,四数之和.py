#两个数的和为0或者n，三个数的和为0或者n，四个数的和为0或者n

# 排过序的可以用剑指offer的两个指针的思路,没排序的用哈希表
def two_sum(nums, target):
    dict1 = {}
    res = []
    for num in nums:
        if target - num in dict1:
            res.append((num,target-num))
        dict1[num] = 1

    return res
        
print(two_sum([1,2,3,4,5,5,6,7,8,9,10],10))


# 先固定一个,剩下两个转化为towsum问题,用两个指针逼近的办法来扫

def three_sum(nums):
    ## O(n^2)
    res = []
    nums.sort()
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        target = 0 - nums[i]
        start, end = i + 1, len(nums) - 1
        while start < end:
            if nums[start] + nums[end] > target:
                end -= 1
            elif nums[start] + nums[end] < target:
                start += 1
            else:
                res.append((nums[i], nums[start], nums[end]))
                end -= 1
                start += 1
                while start < end and nums[end] == nums[end + 1]:
                    end -= 1
                while start < end and nums[start] == nums[start - 1]:
                    start += 1
    return res

print(three_sum([-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7]))

def four_sum(num, target):
    ## O(n^2)
    length, result_set, sum2index = len(num), set(), {}
    if length<4:
        return []
    num.sort()

    for p in range(length):
        for q in range(p+1, length):
            # record the pair sum
            if num[p]+num[q] not in sum2index:
                sum2index[num[p]+num[q]] = [(p, q)]
            else:
                sum2index[num[p]+num[q]].append((p, q))

    for i in range(length):
        for j in range(i+1, length-2):
            sum_remain = target-num[i]-num[j]
            if sum_remain in sum2index:
                # construct the result
                for pair in sum2index[sum_remain]:
                    if pair[0]>j:  # avoid duplicate
                        result_set.add(( num[i], num[j], num[pair[0]], num[pair[1]] ))

    return [list(i) for i in result_set]

print(four_sum([-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7],0))