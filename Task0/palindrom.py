'''
Написать программу для проверки, является ли число падиндромом.
'''
number = int(input('Введите число: '))
temporary = number
reverse = 0
while number > 0:
    division = number % 10
    reverse = reverse * 10 + division
    number = number // 10
if temporary == reverse:
    print('Число является палиндромом')
else:
    print('Число не является палиндромом')

