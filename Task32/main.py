'''
Задача 32:
Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
(т.е. не меньше заданного минимума и не больше заданного максимума).
'''
import random

print(my_list := [random.randint(-100, 100) for _ in range(20)])
min_value = int(input('Введите минимум диапазона: '))
max_value = int(input('Введите максимум диапазона: '))
print(element_index := [i for i in range(len(my_list)) if min_value <= my_list[i] <= max_value])