# 输入两个版本号,第一个版本更高,返回1,第二个更高返回-1,相等返回0

# 本题其实考点是代码的健壮性
## 考虑到版本号没字母,没负数,还有1.0.0和1.0的比较

def version_compare(version1, version2):
    assert version1 != None
    assert version2 != None
    try:
        list1 = list(map(lambda x: int(x), version1.split(r'.')))
        list2 = list(map(lambda x: int(x), version2.split(r'.')))

        for item in list1:
            assert item >= 0
        for item in list2:
            assert item >= 0

        len1,len2 = len(list1), len(list2)
        min_len = min(len1,len2)
        for pos in range(min_len):
            if list1[pos] < list2[pos]:
                return -1
            elif list1[pos] < list2[pos]:
                return 1

        if len1 > len2:
            for pos in range(min_len,len1):
                if len1[pos] != 0:
                    return 1
        if len1 < len2:
            for pos in range(min_len,len1):
                if len1[pos] != 0:
                    return -1
        return 0
    except Exception as e:
        print('input err')

print(version_compare('10.1.1.1','10.1.1.1.0.0'))
