def partition(list1, start, end):
    tmp = list1[start]
    while start < end:
        while start < end and list1[end] >= tmp:
            end -= 1
        list1[start] = list1[end]
        while start < end and list1[start] <= tmp:
            start += 1
        list1[end] = list1[start]

    list1[start] = tmp
    return start


def quick_sort(list1, start, end):
    pos = partition(list1, start, end)
    quick_sort(list1, start, pos - 1)
    quick_sort(list1, pos + 1, end)


# 第K大的
def get_kth(list1, k):
    start = len(list1)
    end = len(list1) - 1
    pos = partition(list1, start, end)
    while pos != len(list1) - k:
        if pos > len(list1) - k:
            pos = partition(list1, start, pos - 1)
        else:
            pos = partition(list1, pos + 1, end)
    return list1[pos]