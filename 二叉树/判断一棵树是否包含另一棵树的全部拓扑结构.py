class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
# head1 是否包含 head2 全部拓扑结构

# hea1和head2开头的是否满足要求
def search(head1,head2):
    if head2 == None:
        return True
    if head1 == None or head1.value != head2.value:
        return False

    return search(head1.left,head2.left) and search(head1.right,head2.right)

# 在head1开头的所有子树里面搜索,是否有满足要求的
def is_contain(head1,head2):
    return search(head1,head2) or is_contain(head1.left,head2) or is_contain(head1.right,head2)
