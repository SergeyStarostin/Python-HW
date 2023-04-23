'''
Задача 22:
Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке
возрастания все те числа, которые встречаются в обоих наборах. Пользователь вводит 2 числа. n — кол-во
элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
'''
def add_elements_list (my_list):
    number_elements = int(input("Введите число n элементов: "))
    count = 0
    for i in range(number_elements):
        count += 1
        elements_set = int(input(f'Введите {count} элемент множества: '))
        my_list.append(elements_set)
    return my_list

number_list_1 = []
add_elements_list(number_list_1)
print(number_list_1)

number_list_2 = []
add_elements_list(number_list_2)
print(number_list_2)

print(f'Отсортированные числа: ', *sorted(set(number_list_1) & set(number_list_2), key=int))