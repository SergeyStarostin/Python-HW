"""
Задача 10:
На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной
и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
"""
import random
number_coins = int(input('Введите количество монеток: '))
number_tails = 0
number_eagles = 0
coins = [random.randint(0, 1) for i in range(number_coins)]
print(f"Монеты: {coins}")
for i in coins:
    if i == 0:
        number_tails += 1
    else:
        number_eagles += 1
if number_eagles > number_tails:
    print(f'Нужно перевернуть {number_tails} монет, лежащих решкой наверх')
else:
    print(f'Нужно перевернуть {number_eagles} монеты, лежащих орлом наверх')