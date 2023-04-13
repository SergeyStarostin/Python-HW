'''
Задача №12:
Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
'''
from math import sqrt
sum_numbers = int(input("Введите сумму чисел: "))
product_numbers = int(input("Введите произведение чисел: "))
disc = sum_numbers * sum_numbers - 4 * product_numbers
root = sqrt(disc)
x = (-sum_numbers + root) / (2 * (-1))
y = (-sum_numbers - root) / (2 * (-1))
print(f'Первое число = {int(x)}')
print(f'Второе число = {int(y)}')