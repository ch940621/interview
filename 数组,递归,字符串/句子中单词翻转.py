# 翻转单词顺序列
# 输入
# student. a am I
# 输出
# I am a student.

# 首先实现一个翻转字符串的函数


def reverse_str(str1):
    assert str1 != None
    if str1 == '':
        return ''
    str1 = list(str1)
    start = 0
    end = len(str1) - 1
    while start < end:
        str1[start], str1[end] = str1[end], str1[start]
        start += 1
        end -= 1

    return ''.join(str1)


print(reverse_str("gaogao"))


def reverse_sentence(sentence):
    sentence = reverse_str(sentence)
    sentence = sentence.strip().split(' ')
    sentence = [reverse_str(str1) for str1 in sentence]
    return ' '.join(sentence)


print(reverse_sentence("student. a am I"))

# 如果不让用split这个工具,用双指针也是可以的
# 遇到空格就算遇到一个单词,要注意最后一个单词是结尾,而不是空格标志的

def reverse_sentence1(sentence):
    sentence = reverse_str(sentence)
    length = len(sentence)
    left, right = 0, 0
 


if "1":
    print('1')
else:
    print("2")