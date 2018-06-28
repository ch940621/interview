class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

def print_common_part(head1,head2):
    while head1 != None or head2 != None:
        if head1.value < head2.value:
            head1 = head1.next
        elif head1.value < head2.value:
            head2 = head2.value
        else:
            print(head1.value,',')
            head1 = head1.value
            head2 = head2.value