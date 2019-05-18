a = 'Hello World!'


def reverseStr(s):
    b = ''
    return b.join([x[::-1] for x in s.split(' ')])


print(reverseStr(a))
