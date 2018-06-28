class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

def remove_node(head,k):
    if head == None:
        return None
    pre_head = Node(0)
    pre_head.next = head
    pre = pre_head
    cur = head

    while cur != None:
        if cur.value == k:
            pre.next = cur.next
        
