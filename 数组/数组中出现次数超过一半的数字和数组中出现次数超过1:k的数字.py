# 数组中出现次数超过一半的数字和数组中出现次数超过1/k的数字

# 初始化第一个数为要找的数,如果后面遇到一样的,次数+1,不一样的时候,次数-1,
# 如果超过一半的他是可以幸存下来的,但是幸存下来的不一定是需要的
# 所以这个解法一定要在确保存在这样的数的前提下,不然就GG,老老实实哈希吧


def find_more_than_half(nums):
    if len(nums) == 0:
        return None
    res = nums[0]
    count = 1
    for pos in range(1, len(nums)):
        if count == 0:
            res = nums[pos]
            count += 1
        else:
            if res == nums[pos]:
                count += 1
            else:
                count -= 1

    return res


print(find_more_than_half([1, 2, 3, 4, 5, 5, 5, 5, 6]))

#
# 出现比率高于1/k也是一样的思路,用k个大小的篮子装,如果count = 0了踢出去
# 这样符合的会留下来,但是留下来的不一定是符合的

# python字典的过滤老老实实用filter
# a = {"a": "1", "b": "2"}
# f = filter(lambda i: i[0] != "b" , a.items())


def find_more_than_n_division_k(nums, k):
    assert k > 0

    if len(nums) == 0:
        return None

    if k == 1:
        for pos in range(len(nums)):
            if nums[pos] != nums[0]:
                return None
        return nums[0]
    res = {}

    for pos in range(len(nums)):
        if len(res) < k:
            if nums[pos] in res:
                res[nums[pos]] += 1
            else:
                res[nums[pos]] = 1
        else:
            for key, value in res.items():
                if key == nums[pos]:
                    res[key] += 1
                else:
                    res[key] -= 1
            res = dict(filter(lambda i: i[1] == 0 , res.items()))

    return res


print(find_more_than_n_division_k([1, 1, 1, 2, 2, 2, 2, 3], 2))
