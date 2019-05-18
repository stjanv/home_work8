from random import random

n = 20
array = []
for i in range(n):
    array.append(int(random() * 100))
array.sort()
print(array)
print('input ur number')
number_for_looking = int(input())
low = 0
high = n - 1
while low <= high:
    mid = low + high // 2
    if number_for_looking < array[mid]:
        high = mid - 1
    elif number_for_looking > array[mid]:
        low = mid + 1
    elif number_for_looking == array[mid]:
        print('id=', mid)
        break
    else:
        break
else:
    print('ur number is under the list')
