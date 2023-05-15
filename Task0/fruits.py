'''
1. Создать функцию dict_to_list, которая будет конвертировать словарь в список кортежей;
2. Функция должна принимать словарь, а возвращать список кортежей, в каждом кортеже
должны быть парыс(key, value) из словаря;
3. Если значение ключа - целое число, то его нужно умножить на 2 перед добавлением в кортеж.
'''
print(fruits := {'watermelon': 20, 'grape': 40.5, 'apple': 35})

def dict_to_list(fruits):
    for item in range(len(fruits)):
        for keys, values in fruits.items():
            if int(values) == values:
                print([(keys, values * 2)])
            elif int(values) != values:
                print([(keys, values)])
        return fruits
dict_to_list(fruits)