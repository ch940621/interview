class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

# 两个是否镜像
def is_mirror_recur(head1,head2):
    if head1 == None and head2 == None:
        return True
    elif head1 == None or head2 == None:
        return False
    
    if head1.value != head2.value:
        return False

    return is_mirror_recur(head1.left,head2.right) and is_mirror_recur(head1.right,head2.left)


# 一个是否对称

def is_symmetry(head):
    if head == None:
        return True
    return is_mirror_recur(head.left,head.right)


# 如果面试官问是否有非递归的思路,是否有别的思路求解一颗二叉树是否对称
# 可以用非递归中序遍历下,看看中序遍历完毕的序列是不是回文的
# 或者用 左根右和右根左都遍历一遍,检查是否一致