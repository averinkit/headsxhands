from random import random
from random import randint
p = 0
q = 999
n = int(input())
array_sizes = []
array_list = []

def func(num):
    for i in range (num):
        size = randint(1,q)
        while size in array_sizes[:]:
            size = randint(1,q)
        array_sizes.append(size)
        
        array = [randint(p,q) for _ in range(size)]
        array.sort()
        
        if (i+1)%2:
            array_list.append(array)
        else:
            array_list.append(array[::-1])
            
func(n)
print(array_list)
