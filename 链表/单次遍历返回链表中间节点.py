class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

def get_middle_node(head):
    pos2 = pos1 = head
    while pos2:
        pos2 = pos2.next
        if pos2 != None:
            pos2 = pos2.next
            pos1 = pos1.next

    return pos1