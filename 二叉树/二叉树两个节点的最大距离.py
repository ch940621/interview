from 二叉树的深度和宽度 import get_deepth_unrecur
class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
class Node1(object):
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
        self.max_distance_left = None
        self.max_distance_right = None
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