class Node(object):
    def __init__(self,value = None):
        self.value = value
        self.left = None
        self.right = None


def pre_order_recur(head):
    if head == None:
        return None

    print(head.value , '\n')
    pre_order_recur(head.left)
    pre_order_recur(head.roght)


def in_order_recur(head):
    if head == None:
        return None

    in_order_recur(head.left)
    print(head.value , '\n')
    in_order_recur(head.roght)


def pos_order_recur(head):
    if head == None:
        return None

    pos_order_recur(head.left)
    pos_order_recur(head.roght)
    print(head.value , '\n')
