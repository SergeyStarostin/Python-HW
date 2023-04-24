'''
Задача 26:
Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
Пример:
A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8
'''
def exponentiation(base, degree):
    if degree == 1:
        return base
    if degree != 1:
        return base * exponentiation(base, degree - 1)
base = int(input('Введите число: '))
degree = int(input('Введите степень: '))
print(f'{base} в степени {degree} = ', exponentiation(base, degree))