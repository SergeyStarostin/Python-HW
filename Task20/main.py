'''
Задача 20:
В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
В случае с английским алфавитом очки распределяются так:
A, E, I, O, U, L, N, S, T, R – 1 очко;
D, G – 2 очка;
B, C, M, P – 3 очка;
F, H, V, W, Y – 4 очка;
K – 5 очков;
J, X – 8 очков;
Q, Z – 10 очков.
А русские буквы оцениваются так:
А, В, Е, И, Н, О, Р, С, Т – 1 очко;
Д, К, Л, М, П, У – 2 очка;
Б, Г, Ё, Ь, Я – 3 очка;
Й, Ы – 4 очка;
Ж, З, Х, Ц, Ч – 5 очков;
Ш, Э, Ю – 8 очков;
Ф, Щ, Ъ – 10 очков.
Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать,
что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
Пример:
ноутбук
Sum = 12
'''
english_Scrabble = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: "K", 8: 'JX', 10: 'QZ'}
russian_Scrabble = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ', 4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФШЪ'}
user_input_word = input('Слово на русском или английском языке: ')

eng_sum_points = 0
for eng_char in user_input_word:
    for key, value in english_Scrabble.items():
        if eng_char.upper() in value:
            eng_sum_points += key

rus_sum_points = 0
for rus_char in user_input_word:
    for key, value in russian_Scrabble.items():
        if rus_char.upper() in value:
            rus_sum_points += key

if eng_sum_points != 0:
    print(f'Цена английского слова = {eng_sum_points}')
else:
    print(f'Цена русского слова = {rus_sum_points}')