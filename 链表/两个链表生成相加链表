from 翻转单链表 import reverse_linklist1

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

def add_list(head1,head2):
    if head1 == None:
        return head2
    if head2 == None:
        return head1
    if head1 == None and head2 == None:
        return None
    
    head1 = reverse_linklist1(head1)
    head2 = reverse_linklist1(head2)
    sun_head = Node((head1.value + head2.value) % 10)

    cur1 = head1.next
    cur2 = head2.next
    cur3 = sun_head

    carry = (head1.value + head2.value) // 10
    while cur1 and cur2:
        cur3.next = Node((cur1.value + cur2.value + carry) % 10)
        carry = (cur1.value + cur2.value + carry) // 10
        cur1 = cur1.next
        cur2 = cur2.next
        cur3 = cur3.next

    while cur1:
        cur3.next = Node((cur1.value + carry) % 10)
        carry = (cur1.value + carry) // 10
        cur1 = cur1.next
        cur3 = cur3.next

    while cur2:
        cur3.next = Node((cur2.value + carry) % 10)
        carry = (cur2.value + carry) // 10
        cur2 = cur2.next
        cur3 = cur3.next

    while carry:
        cur3.next = Node(carry)
    
    reverse_linklist1(head1)
    reverse_linklist1(head2)
    return reverse_linklist1(sun_head)

        

        
        