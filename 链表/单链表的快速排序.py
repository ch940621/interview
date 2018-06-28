class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


def partion(start, end):
    if start == None or end == None or start == end:
        return None

    tmp = start  # 第一个点为基准点,这个值被定为mid
    mid = start # mid 为正在寻找的mid的位置
    pos = mid.next

    while pos != end:
        if pos.value < tmp:
            mid = mid.next
            mid.value, pos.value = pos.value, mid.value
        pos = pos.next

    mid.value, tmp.value = tmp.value, mid.value # mid 的值回到属于他的位置上
    return mid

def quick_sort(start, end):
    pos = partion(start, end)
    quick_sort(start, pos)
    quick_sort(pos.next, end)
