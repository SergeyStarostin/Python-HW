'''
Написать программу для проверки, является ли число падиндромом.
'''
# проверка числа на палиндром

number = int(input('Введите число: '))
temporary = number
reverse = 0
while number > 0:
    division = number % 10
    reverse = reverse * 10 + division
    number = number // 10
print('Число является палиндромом' if temporary == reverse else 'Число не является палиндромом')

# проверка слова или числа на палиндром

word = str(input('Введите слово: '))
print('Слово является палиндромом' if word == word[::-1] else 'Слово не является палиндромом')