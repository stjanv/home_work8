from datetime import datetime
import functools
from functools import singledispatch
from functools import lru_cache
import numbers
from collections import OrderedDict
import pprint
# task 1.1

def check_time(func):
    def wrapper():
        start = datetime.now()
        res = func()
        print(datetime.now() - start)
        return res

    return wrapper


@check_time
def generate():
    l = [x for x in range(10000) if x % 2 == 0]
    return l


print(generate())


#task 1.3


def recount(func):
    def wrapper():
        res = func()
        wrapper.count += 1
        # print('Func was called ',count, 'times')
        return res

    wrapper.count = 0

    return wrapper


@recount
def generate():
    l = [x for x in range(10000) if x % 2 == 0]
    return l


generate()
generate()
generate()
print(generate.count)

#task 1.4


def recount_once(func):
    def wrapper():
        res = func()
        nonlocal count
        count += 1
        if count<=1:
            return res
        else:
            s='Func was called once'
            return s
    count = 0

    return wrapper


@recount_once
def generate():
    l = [x for x in range(10000) if x % 2 == 0]
    return l


print(generate())
print(generate())

#task 1.2


def recount_once(func):
    j = {0:0}
    def wrapper(l):
        nonlocal j
        if l in j.keys():
            print('From log')
            return j.get(l)
        else:
            res = func(l)
            other = (l,res)
            j.update([other])
            print(j,'from func')
            return res
    return wrapper


@recount_once
def generate(l):
    l = l * 5
    return l


l = int(input())
print(generate(l))
l = int(input())
print(generate(l))

#task 2.1


def recount(func):
    @functools.wraps(func)
    def wrapper():
        res = func()
        wrapper.count += 1
        return res

    wrapper.count = 0

    return wrapper


@recount
def generate():
    l = [x for x in range(10000) if x % 2 == 0]
    return l

print(generate())

#tsk 2.2

@singledispatch
def func(n):
    print('Mutnaya mut\'')
    return n

@func.register(int)
def _(n):
    n=n*5-1
    return n

@func.register(str)
def _(n):
    n=n[::-1]
    return n

n=func
print(func(n))

#task 3

def make_key(*args,**kwargs):
    key=args
    for i in sorted(kwargs.items()):
        key+=i
    return key


def my_lru_cache(maxSize,ttl):
    def take_cahce(func):
        cache=OrderedDict()

        def wrapper(*args,**kwargs):
            current_time=datetime.datetime.now()

            def take_new():
                return { 'func_val': func(*args,**kwargs),'count_usage' : 0, 't_created' : current_time,'t_used' : current_time}
            cache_key=make_key(*args,**kwargs)
            val=None
            if cache_key in cache:
                val=cache.pop(cache_key)
                t1=current_time-val['t_created']
                if t1.total_seconds()>ttl:
                    val=take_new()
                else:
                    val['t_used']=current_time
                    val['count_usage']+=1
            else:
                val=take_new()
                if len(cache) +1>maxSize:
                    cache.popitem(last=False)
            cache[cache_key]=val
            return val['func_val']
        def cache_clear():
            cache.clear()

        def cache_info():
            pprint.pprint(cache)


        wrapper.cahce_clear= cache_clear
        wrapper.cache_info = cache_info
        return wrapper
    return take_cahce




@my_lru_cache(5,2)
def fucking_the_horse(n):

    return n**n

fucking_the_horse(5)
fucking_the_horse(2)
fucking_the_horse(4)
fucking_the_horse(5)
fucking_the_horse(4)
fucking_the_horse(3)
fucking_the_horse(4)
fucking_the_horse(2)
fucking_the_horse.cache_info()
