from 二叉树的深度和宽度 import get_deepth_unrecur
class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

# 计算一个二叉树的最大距离有两个情况：

# 情况A: 路径经过左子树的最深节点，通过根节点，再到右子树的最深节点。
# 情况B: 路径不穿过根节点，而是左子树或右子树的最大距离路径，取其大者
# 总结起来就是 Dis(x) = max(Dis(x->left), Dis(x->right), height(x->left)+height(x->right))



# 因为就要保存的值需要持续传递, 如果不改造二叉树的结构的话就需要max_distance这个全局变量
global max_distance 
max_distance = 0
def get_max_distance(head):
    global max_distance
    if head == None:
        return 0
    if head.left == None == head.right == None:
        return 0
    cur_distance = max(get_deepth_unrecur(head.left)+get_deepth_unrecur(head.right),get_max_distance(head.left),get_max_distance(head.right))

    if cur_distance > max_distance:
        cur_distance,max_distance = max_distance,cur_distance
    return max_distance


# 更简洁的写法

def hight(head):
    if head == None:
        return 0
    return max(hight(head.left),hight(head.right)) + 1

def get_max_distance1(head):
    if head == None:
        return 0

    left_max_distance = get_max_distance1(head.left)
    right_max_distance = get_max_distance1(head.right)

    left_hight = 0
    right_hight = 0

    if head.left != None:
        left_hight = hight(head.left)
    if head.right != None:
        right_hight = hight(head.right)

    return max(left_max_distance,right_max_distance,left_hight+right_hight)