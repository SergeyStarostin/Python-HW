'''
1. Создать функцию dict_to_list, которая будет конвертировать словарь в список кортежей;
2. Функция должна принимать словарь, а возвращать список кортежей, в каждом кортеже
должны быть пары(key, value) из словаря;
3. Если значение ключа - целое число, то его нужно умножить на 2 перед добавлением в кортеж.
'''
print(fruits := {'watermelon': 'fresh', 'grape': 40.1, 'apple': 35})

def dict_to_list(dictionary: dict) -> list:
    return [(keys, (values * 2) if isinstance(values, int) else values) for keys, values in dictionary.items()]

print(dict_to_list(fruits))