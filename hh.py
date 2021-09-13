from random import random
from random import randint
p = 0
q = 999
n = int(input())
array_sizes = []
array_list = []

def func(num):
    for i in range (num):
        size = randint(1,q)                                 #генерируется размер массивов
        while size in array_sizes[:]:                       #если массив такого размера существует,
            size = randint(1,q)                             #то генерируется новый размер
        array_sizes.append(size)
        
        array = [randint(p,q) for _ in range(size)]         #массив заполняется случайными числами
        array.sort()                                        #и сортируется по возрастанию
        
        if (i+1)%2:                                         
            array_list.append(array)
        else:
            array_list.append(array[::-1])                  #если номер массива нечётный, то его элементы записываются в обратном порядке
            
func(n)
print(array_list)
input()
