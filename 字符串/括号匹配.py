# leetcode20
# 有{}[]()这三种挂号,判断输入的字符串的括号是不是合法的
# 三步走:
# 1）遇到左括号就直接压入栈
# 2）遇到右括号就弹出，如果弹出的符号和当前不匹配或者栈已经为空，则错误。
# 3）如果已经遍历完以后，栈还不为空，则错误

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

## 忽略非括号符号的版本
def is_legal(str1):
    stack = Stack()

    for pos in range(len(str1)):
        cur_char = str1[pos]

        if cur_char in ['(','[','{']:
            stack.push(cur_char)
        elif cur_char in [')',']','}']:
            if stack.is_empty():
                return False
            else:
                if cur_char == '}' and stack.peek() == '{' or cur_char == ']' and stack.peek() == '[' or cur_char == ')' and stack.peek() == '(':
                    stack.pop()
                else:
                    return False
        else:
            return False

    return True if stack.is_empty() else False



print(is_legal("((())){{{}}}{[]}"))
    