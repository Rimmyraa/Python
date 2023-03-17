# 🏠 Домашнє завдання:
# Вивести на екран три найпоширеніші символи в рядку (пробіл за символ не вважаємо).

text = input('Введите слово: ')

chars_counter = dict()

for char in text:
    if char != ' ':
        if char not in chars_counter:
            chars_counter[char] = text.count(char)

print(chars_counter)


counter_list = sorted(list(chars_counter.items()), key=lambda x: x[1])
counter_list.reverse()
print(counter_list)
for element in counter_list[:3]:
    print(f'{element[0]} - {element[1]}')


# bubble sort

# counter_list = list(chars_counter.items())
# for i in range(len(counter_list)-1):
#     for element in range(len(counter_list)-i):
#         if counter_list[element][1] > counter_list[element+1][1]:
#             counter_list[element], counter_list[element+1][1] = counter_list[element+1][1], counter_list[element]


# lambda - пример
# f = lambda a: a**2
# print(f(9))
