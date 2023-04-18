'''
Задача 18:
Требуется найти в списке A[1..N] самый близкий по величине элемент к заданному числу X.
Пользователь в первой строке вводит натуральное число N – количество элементов в списке.
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X.
Пример:
N: 5
[3, 0, 1, 1, 4]
X: 8
Минимальный соседний элемент: 4
'''
import random
number_N = int(input('Введите число элементов списка: '))
list_input = [random.randint(0, number_N) for i in range(number_N)]
print(list_input)
search_element = int(input('Введите число, соседний элемент которого нужно найти: '))
nearest_max_element = search_element + 1
nearest_min_element = search_element - 1
validation = True
while validation:
    for item in list_input:
        if item == nearest_max_element:
            print(f'Максимальный соседний элемент: {item}')
            validation = False
            break
    nearest_max_element += 1
    for item in list_input:
        if item == nearest_min_element:
            print(f'Минимальный соседний элемент: {item}')
            validation = False
            break
    nearest_min_element -= 1