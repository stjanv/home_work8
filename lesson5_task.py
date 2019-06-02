from datetime import datetime
import functools
from functools import singledispatch
from functools import lru_cache
import numbers
# task 1.1

# def check_time(func):
#     def wrapper():
#         start = datetime.now()
#         res = func()
#         print(datetime.now() - start)
#         return res
#
#     return wrapper
#
#
# @check_time
# def generate():
#     l = [x for x in range(10000) if x % 2 == 0]
#     return l
#
#
# print(generate())
#

# task 1.3


# def recount(func):
#     def wrapper():
#         res = func()
#         wrapper.count += 1
#         # print('Func was called ',count, 'times')
#         return res
#
#     wrapper.count = 0
#
#     return wrapper
#
#
# @recount
# def generate():
#     l = [x for x in range(10000) if x % 2 == 0]
#     return l
#
#
# generate()
# generate()
# generate()
# print(generate.count)

# task 1.4


# def recount_once(func):
#     def wrapper():
#         res = func()
#         nonlocal count
#         count += 1
#         if count<=1:
#             return res
#         else:
#             s='Func was called once'
#             return s
#     count = 0
#
#     return wrapper
#
#
# @recount_once
# def generate():
#     l = [x for x in range(10000) if x % 2 == 0]
#     return l
#
#
# print(generate())
# print(generate())

# task 1.2


# def recount_once(func):
#     j = {0:0}
#     def wrapper(l):
#         nonlocal j
#         if l in j.keys():
#             print('From log')
#             return j.get(l)
#         else:
#             res = func(l)
#             other = (l,res)
#             j.update([other])
#             print(j,'from func')
#             return res
#     return wrapper
#
#
# @recount_once
# def generate(l):
#     l = l * 5
#     return l
#
#
# l = int(input())
# print(generate(l))
# l = int(input())
# print(generate(l))

#task 2.1


# def recount(func):
#     @functools.wraps(func)
#     def wrapper():
#         res = func()
#         wrapper.count += 1
#         return res
#
#     wrapper.count = 0
#
#     return wrapper
#
#
# @recount
# def generate():
#     l = [x for x in range(10000) if x % 2 == 0]
#     return l
#
# print(generate())

#tsk 2.2

# @singledispatch
# def func(n):
#     print('Mutnaya mut\'')
#     return n
#
# @func.register(int)
# def _(n):
#     n=n*5-1
#     return n
#
# @func.register(str)
# def _(n):
#     n=n[::-1]
#     return n
#
# n=func
# print(func(n))

#task 3

@lru_cache(maxsize=20)
def func(n):
    while n!=8:
        if n.isdigit():
            n=int(n)
            if n<8:
                print('Try once more, it\'s up')
            elif n>8:
                print('Try once more, it\'s down')
            elif n==8:
                print('U are right')
                break
        else:
            print('it\'s not a number')
        n = input()
    return
n=input()
func(n)
print(func.cache_info())
