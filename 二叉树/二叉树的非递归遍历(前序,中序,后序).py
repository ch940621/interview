from collections import deque

class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

class Stack(object):
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def peek(self):
        return self.items[len(self.items) - 1]
    def size(self):
        return len(self.items)
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()

class Queue(object):
    def __init__(self):
        self.items = deque()
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        return self.items.popleft()
    def size(self):
        return len(self.items)
    def is_empty(self):
        return len(self.items) == 0
    def front(self):
        return self.items[0]

# 非递归前序遍历二叉树
# 思路就是用栈,栈先压入自己打印完毕弹出,然后在依次压孩子,先压右孩子再压左孩子,每个孩子自己打印完毕弹出后立即压他的两个孩子,没孩子可以压并且栈为空了遍历停止
def pre_order_unrecur(head):
    if head != None:
        stack = Stack()
        stack.push(head)
        while not stack.is_empty():
            head = stack.pop()
            print(head.value, '\n')
            if head.left != None:
                stack.push(head.left)
            if head.right != None:
                stack.push(head.right)

# 非递归中序遍历二叉树
# 首先一路左子树压栈压到底,然后没有左孩子了开始先把当前的弹出,相当于回到了父节点,然后开始进入这个节点的右节点
# 这个过程中如果新进入的节点有左孩子,继续义无反顾的压到底,没有的话打印这个当前节点弹出
def in_order_unrecur(head):
    if head != None:
        stack = Stack()
        while head != None or not stack.is_empty():
            if head != None:
                stack.push(head)
                head = head.left
            else:
                head = stack.pop()
                print(head.value, '\n')
                head = head.right


# 非递归后续遍历二叉树
# 思路一
# 后序遍历的非递归实现比前序、中序的非递归实现 要复杂一点。
# 需要一个标识来标记某结点是否第一次位于栈顶（该结点的左子树已经遍历完毕，从左子树返回准备遍历它的右子树）
# 对于后序遍历而言，结点的左右子树都遍历完成之后，才访问该结点。某结点会两次位于栈顶，第一次是该结点的左子树都遍历完了，
# 然后获取栈顶结点，切换到该结点的右孩子，准备遍历它的右子树，当该结点的右子树也都遍历完后，它就会第二次位于栈顶，此时将栈顶元素出栈。


# 新的数据结构
class Node1(object):
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
        self.first_visited = False


def pos_order_unrecur(head):
    stack = Stack()

    while head != None or not stack.is_empty():
        while head != None: # 玩命地左子树压倒底
            stack.push(head)
            head = head.left

        if not stack.is_empty():
            tmp = stack.peek() 

            if tmp.first_visited:
                # 左右子树已经访问过了
                tmp = stack.pop()
                print(tmp, '\n')
            else:
                # 还木有访问右子树呢,赶紧补上
                tmp.is_first_visit = True
                head = tmp.right

# 思路二用两个栈
# 一个S1栈实现类似[前序非递归的遍历]前序非递归的遍历,得到中,右,左
# S1出栈后,不直接打印,而是压入S2
# 待整个树遍历完,所有节点也都全部压入S2栈内,最后统一弹出,得到左,右,中

def pos_order_unrecur1(head):
    if head != None:
        stack1 = Stack()
        stack2 = Stack()
        stack1.push(head)
        while not stack1.is_empty():
            head = stack1.pop()
            # print(head.value, '\n')
            stack2.push(head.value)
            if head.right != None:
                stack1.push(head.right)
            if head.left != None:
                stack1.push(head.left)

    while not stack2.is_empty():
        print(stack2.pop().value,'\n')
# 思路三用一个栈
# 思路三比较麻烦,思路一和二足够应付面试了,而且思路一和二更好直观,面试推荐写思路一和思路二
# 一个栈实现,我们需要两个变量
# 一个记录当前节点cur,一个记录最近打印节点head,一开始就将根结点直接压入栈中

# 左右孩子节点入栈规则:若该节点有左孩子且head既不是其左孩子,又不是其右孩子,左孩子入栈.
# 若该节点有右孩子,且head不是其右孩子,右孩子入栈.

#栈顶节点出栈规则:从左孩子返回,则左子树遍历完毕,开始遍历右子树.从右孩子返回,则右子树遍历完毕,整颗子树遍历完毕,弹出栈顶元素,并打印节点

def pos_order_unrecur2(head):
    if head != None:
        stack = Stack()
        stack.push(head)
        while not stack.is_empty():
            cur = stack.pop()
            # 第一个if中的h != c->r判断必须要，如果不加，从右子树返回的节点会再一次压入栈中
            if cur.left != None and head != cur.left and head != cur.right:
                stack.push(cur.left)
            elif cur.left != None and head != cur.right:
                stack.push(cur.right)
            else:
                print(stack.pop().value)
                head = cur