class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
# 二叉搜索树的中序遍历是递增的序列,左子树节点最大值绝对小于根小于右子树节点最大值
# 搜索的递归
def search_BST_recur(head,input_value):
    if head == None:
        return False
    if input_value == head.value:
        return True
    elif input_value < head.value:
        return search_BST_recur(head.left,input_value)
    elif input_value > head.value:
        return search_BST_recur(head.right,input_value)
# 搜索的非递归
def search_BST_unrecur(head,input_value):
    if head == None:
        return None
    while head != None:
        if input_value == head.value:
            return True
        elif input_value < head.value:
            head = head.left
        elif input_value > head.value:
            head = head.right
    return False


# 插入的递归
# 要保证树里面木有要插入的值

def insert_BST_recur(head,input_value):
    if head == None:
        head = Node(input_value)
    elif input_value < head.value:
        insert_BST_recur(head.left,input_value)
    elif input_value > head.value:
        insert_BST_recur(head.right,input_value)


def insert_BST_unrecur(head,input_value):
    if head == None:
        head = Node(input_value)
    
    else:
        cur = head
        while head != None:
            if input_value < head.value:
                pre = cur
                cur = cur.left
            elif input_value > head.value:
                pre = cur
                cur = cur.right
        if input_value < pre.value:
            pre.right = Node(input_value)
        elif input_value > pre.value:
            pre.left = Node(input_value)

# 删除比较麻烦以后再说吧