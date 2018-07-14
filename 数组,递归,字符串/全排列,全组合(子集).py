##全组合(子集)问题
'''
方法一:位运算
求1,2,3,4的全部子集我们可以对每一位编码,0000,0001,0010,0011...分别代表[],[1],[2],[1,2]...
生成编码后,一位一位地取商和余数,商参加下一轮接计算,余数为1即代表该二进制位代表的元素要取,为0代表不取
'''


def subset1(elements):
    length = len(elements)
    ress = []
    for num in range(0, 2**length):
        res = []
        for pos in range(0, length):
            yushu = num % 2
            num = num // 2
            if yushu != 0:
                res.append(elements[pos])
        ress.append(res)
    return ress


print(subset1([1, 2, 3, 4]))
print(len(subset1([1, 2, 3, 4])))
print('1' * 66)
'''
方法二:DFS
求1,2,3,4的全部子集,我们可以先求{2,3,4}的全部子集,这些子集是结果的一部分,这些子集并上{1}是结果的另外一个部分,问题就转化为为求{2,2,3}的子集了
求{2,3,4}的子集可以同样转化为{3,4}的子集,以及{3,4}的所以子集并上{2},这两部分结果就是所求问题的解
这样依次递归,直到子集的元素只有一个
这个时候输出结果即为全组合

S(1,2,3,4) = 1+S(2,3,4) + S(2,3,4)
S(2,3,4) = 2+S(3,4) + S(3,4)
S(3,4) = 3+S(4) +S(4)
'''


def subset2(elements):
    if elements is None:
        return []
    res = []
    dfs(elements, 0, [], res)
    return res


def dfs(elements, start, sub, res):
    res.append(sub)
    for pos in range(start, len(elements)):
        dfs(elements, pos + 1, sub + [elements[pos]], res)


print(subset2([1, 2, 3, 4]))
print(len(subset2([1, 2, 3, 4])))
print('2' * 66)

## 全排列问题
'''
方法一:DFS
子问题可以如下拆解
P(1,2,3,4)= 1+P(2,3,4) + 2+P(1,3,4) + 3+P(1,2,4) +4+P(1,2,3)
P(2,3,4) = 2+P(3,4) + 3+P(2,3) + 4+P(2,3)
P(3,4) = 3+P(4) + 4+P(3)
'''


def perm1(elements):
    start = 0
    end = len(elements) - 1
    return dfs1(elements, start, end, [])


def dfs1(elements, start, end, res):
    if start == end:
        str1 = ''.join(list(map(lambda x: str(x),elements)))
        res.append(str1)
    else:
        pos = start
        while pos <= end:
            elements[pos], elements[start] = elements[start], elements[pos]
            dfs1(elements, start + 1, end, res)
            elements[pos], elements[start] = elements[start], elements[pos]
            pos += 1
    return res

print(perm1([1, 2, 3, 4]))
print('3' * 66)
