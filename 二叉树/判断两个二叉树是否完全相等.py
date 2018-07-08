class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


def is_same_recur(head1,head2):
    if head1 == None and head2 == None:
        return True
    if head1 == None or head2 == None:
        return False

    if head1.value != head2.value:
        return False
    
    return is_same_recur(head1.left,head2.left) and is_same_recur(head1.right,head2.right)


# 非递归的思路就是同时遍历遇到不一样的就是不同