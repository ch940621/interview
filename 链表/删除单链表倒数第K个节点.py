class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


def remove_Kth_from_end(head, k):
    # 定义一个节点指向head,防止head指向的链表只有一个元素,移除完毕后为空
    root = Node(0)
    root.next = head
    fast, slow, tmp = root, root, root
    while k - 1:
        fast = fast.next
        k -= 1

    while fast.next:
        fast = fast.next
        tmp = slow
        slow = slow.next
    tmp.next = slow.next  # 跳过定位到的倒数第K个节点
    return root.next
