# -*- coding=utf-8 -*-
# 这个例子是Python版本的单链表

class Node(object):
    def __init__(self, value, next=0):
        self.value = value
        self.next = next  # 指针


class LinkedList(object):
    # 链表的数据结构
    def __init__(self):
        self.head = 0  # 头部

    def __getitem__(self, key):
        if self.is_empty():
            print ('Linked list is empty.')
            return
        elif key < 0 or key > self.get_length():
            print ('The given key is wrong.')
            return
        else:
            return self.get_elem(key)

    def __setitem__(self, key, value):
        if self.is_empty():
            print ('Linked list is empty.')
            return
        elif key < 0 or key > self.get_length():
            print ('The given key is wrong.')
            return
        else:
            return self.set_elem(key, value)

    def init_list(self, data):  # 按列表给出 data
        self.head = Node(data[0])
        p = self.head  # 指针指向头结点
        print (p, self.head)
        for i in data[1:]:
            p.next = Node(i)  # 确定指针指向下一个结点
            p = p.next  # 指针滑动向下一个位置
        print (self.head.next.next)

    def get_length(self):
        length = 0
        p = self.head
        while p != 0:  # 0 值就是Node结点中默认的 0 值，表示下一个结点没有了，即没有为其赋值
            length += 1
            p = p.next
        return length

    def is_empty(self):
        if self.head == 0:
            return True
        else:
            return False

    def insert_node(self, index, value):
        if index < 0 or index > self.get_length():
            print ('Can not insert node into the linked list.')
        elif index == 0:
            temp = self.head
            self.head = Node(value, temp)
        else:
            p, post = self.head, self.head
            for i in xrange(index):
                post = p
                p = p.next
            temp = p
            post.next = Node(value, temp)

    def delete_node(self, index):
        if index < 0 or index > self.get_length()-1:
            print ("Wrong index number to delete any node.")
        elif self.is_empty():
            print ("No node can be deleted.")
        elif index == 0:
            temp = self.head
            self.head = temp.next
        elif index == self.get_length():
            p = self.head
            for i in xrange(self.get_length()-2):
                p = p.next
            p.next = 0
        else:
            p = self.head
            for i in xrange(index-1):
                p = p.next
            p.next = p.next.next

    def show_linked_list(self):  # 打印链表中的所有元素
        if self.is_empty():
            print ('This is an empty linked list.')
        else:
            p, container = self.head, []
            for _ in xrange(self.get_length()-1):
                container.append(p.value)
                p = p.next
            container.append(p.value)
            print (container)

    def clear_linked_list(self):  # 将链表置空
        self.head = 0

    def get_elem(self, index):
        if self.is_empty():
            print ("The linked list is empty. Can not get element.")
        elif index < 0 or index > self.get_length()-1:
            print ("Wrong index number to get any element.")
        else:
            p = self.head
            for _ in range(index):
                p = p.next
            return p.value

    def set_elem(self, index, value):
        if self.is_empty():
            print ("The linked list is empty. Can not set element.")
        elif index < 0 or index > self.get_length()-1:
            print ("Wrong index number to set element.")
        else:
            p = self.head
            for _ in range(index):
                p = p.next
            p.value = value

    def get_index(self, value):
        p = self.head
        for i in range(self.get_length()):
            if p.value == value:
                return i
            else:
                p = p.next
        return -1
