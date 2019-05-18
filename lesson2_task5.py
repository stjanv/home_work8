import random

a = ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 't', 'T',
     'y', 'Y', 'o', 'O', 'u', 'U', '1', '2', '3', '4', '5', '6',
     '7', '8', '9', '0', 'k', 'K', 'l', 'L', '@']


def enter_count():
    count_symbols_in_pass = None
    while count_symbols_in_pass is not int:
        try:
            print('Enter count of symbols in ur pass')
            count_symbols_in_pass = int(input())
            break
        except:
            print('u enter not a number')
            continue
    return count_symbols_in_pass


c = (enter_count())

b = ''
array = []
for i in range(c):
    j=str(random.choice(a))
    array.append(j)
b = b.join(array)
print(b)
