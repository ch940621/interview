class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

def remove_repeat(head):
    if head == None:
        return None
    node_map = set({})
    pre = head
    cur = head.next

    while cur != None:
        if cur.value in node_map:
            pre.next = cur.next
        else:
            node_map.add(cur.value)
