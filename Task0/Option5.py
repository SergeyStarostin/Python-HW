'''
ЛАБОРАТОРНАЯ РАБОТА №1. Ветвящиеся вычислительные процессы
Вариант №5
'''
import math

def result(a, b):
    if b == 0:
        print('Деление на 0')
    elif a < -2:
        print('Корень из отрицательного числа')
    elif b < a:
        print('y1 = ', (a + b) / b ** 2 - a)
    elif b >= a > 0:
        print('y2 = ', math.sin(a) + math.cos(b))
    elif b >= a <= 0:
        print('y3 = ', math.sqrt(3 * a + b))
    else:
        print('Некорректный ввод данных')
a = int(input('Введите число a: '))
b = int(input('Введите число b: '))
result(a, b)