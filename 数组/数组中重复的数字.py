# 一个长度为n的数组里的所有数字都在0到n-1的范围内,数组中某些数字是重复的
# 但不知道有几个数字是重复的,也不知道每个数字重复几次,找出任意一个重复的数字

# 对于输入nums,用pos遍历,遍历的过程中
# 对每个元素,若nums[pos]不等于pos,交换nums[pos] 和nums[nums[pos]],也就是把当前指针指向的数放到他们自己的应该呆位置上去
# 交换完毕后当前送走的数字正确归位了,送来的老佛爷咱们继续判断该不该也给送到他的位置上
# 如此循环.知道咱们遇到送走的老佛爷之后来的老佛爷就该呆在这,那指针后移
# 当然遍历的时候如果发现咱们要送走的老佛爷的位置上坐着一个正确的老佛爷,这代表位置不够分啊
# 会陷入江局,那说明有重复的,返回duplication

# 以[4,7,3,5,1,6,5,0]为例,每轮的pos的位置和nums的情况如下
# [1, 7, 3, 5, 4, 6, 5, 0] 0
# [7, 1, 3, 5, 4, 6, 5, 0] 0
# [0, 1, 3, 5, 4, 6, 5, 7] 0
# [0, 1, 5, 3, 4, 6, 5, 7] 2
# [0, 1, 6, 3, 4, 5, 5, 7] 2
# [0, 1, 5, 3, 4, 5, 6, 7] 2
# 到这一步要继续按照咱们的逻辑下去就是死循环nums[2] = nums[nums[2]]


def duplicate(nums):
    for pos in range(len(nums)):
        while pos != nums[pos]:  # 咱们只挪位置不对劲的
            if nums[pos] == nums[nums[pos]]:
                res = nums[pos]
                return True, res
            else:
                tmp = nums[nums[pos]]
                nums[nums[pos]] = nums[pos]
                nums[pos] = tmp
    return False, None


print(duplicate([4, 7, 3, 5, 1, 6, 5, 0])[1])
