class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

# 从根节点开始的
def get_max(head):
    path = []
    def search(head):
        if head.left == None and head.right == None:
            return head.value
        if head.left != None and head.right == None:
            path.append(head.left)
            return head.value + search(head.left)
        elif head.left == None and head.right != None:
            path.append(head.right)
            return head.value + search(head.right)
        elif head.left != None and head.right != None:
            left_max = search(head.left)
            right_max = search(head.right)

            if left_max > right_max:
                path.append(head.left)
                return head.value + left_max

    return path




