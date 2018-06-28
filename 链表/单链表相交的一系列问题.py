class Node(object):
    def __init__(self, value, next=0):
        self.value = value
        self.next = next  # 指针

# 判断一个单链表是否有环
# 思路,快慢指针,慢指针一次走一步,快指针一次走两步,如果有环一定会相交的
def exit_loop(head):
    fast = slow = head
    while slow != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


# 若有环,找出环的入口点.
# 思路,通过数学方程化简可以得到,链表head到环入口点和两个指针相遇点到环入口点的距离相等
def find_loop_start(head):
    fast = slow = head
    while slow != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    if slow == None or fast.next == None:
        return None

    start = head
    meet = slow
    while start != meet:
        start = start.next
        meet = meet.next
    return meet


# 判断两个链表是否相交


# 如果不考虑环的情况,一个思路就是把两个链表都遍历到最后一个节点,如果这两个节点是同一个则相交否则不相交
def exit_intersect1(head1, head2):
    while head1:
        pre1 = head1
        head1 = head1.next
    while head2:
        pre2 = head2
        head2 = head2.next

    if pre1 == pre2:
        return True
    else:
        return False


# 不考虑环的情况,思路二可以把链表1的尾指针指向链表1的头,链表相交的问题便转化为链表是否有环的问有环就相交,没环就不相交
def exit_intersect2(head1, head2):
    while head1:
        pre1 = head1
        head1 = head1.next
    pre1.next = head2
    return exit_loop(head1)


# 还有一种通用的思路就是构造hash,吧第一个链表的节点存入hash,然后遍历第二个链表的时候,如果遇到了说明有相同的节点
# 但这种思路空间复杂度不符合要求,一般不采用

# 考虑环的情况
# 如果两个链表都没有环,上面的exit_intersect1和exit_intersect2即为后续的解题思路
# 如果两个链表一个有环,一个没环,则他们必然不相交
# 如果两个链表都有环,则需要继续分析
# 分别返回两个链表的find_loop_start的点,如果两个点一样那必然相交


def exit_intersect(head1, head2):
    if exit_loop(head1) and exit_loop(head2):
        loop_start1 = find_loop_start(head1)
        loop_start2 = find_loop_start(head2)
        if loop_start1 == loop_start2:
            return True
        else:
            cur = loop_start1.next
            while cur != loop_start1:
                if cur == loop_start2:
                    return True
                cur = cur.next
            return False
    elif (exit_loop(head1) and not exit_loop(head2)) or (not exit_loop(head1)
                                                         and exit_loop(head2)):
        return False
    else:
        # 即两个链表都无环
        return exit_intersect1(head1, head2)
