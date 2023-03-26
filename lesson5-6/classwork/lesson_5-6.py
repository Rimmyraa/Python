import random


# список
# чтоб назвать список надо написать list. for ex: my_list

# my_list = [1, 4, 'hello', [1, 24, 5]]
# print(my_list)

# task_1
# abc = ['a', 'b', 'c']
# print(abc)

# task_2
# my_list = list(('1', '2', '3'))
# print(my_list)

# task_3
# my_list = ['Ivan', 'Ivanovich', '15']
# print(f'{my_list}')

# iterable = list('Python')
# firts_element =  iterable[0]
# second_element = iterable[1]
# last_element = iterable[-1]
# print(iterable)
# print(firts_element)
# print(second_element)
# print(last_element)


# my_list = [1, 4, 9, 6, 5]
# last_element_of_second = my_list[2][-1][0]        #тобиш надо вызвать цифру 5
# print(last_element_of_second)


# my_list = [1, 4, 9, 6, 5]
# my_list.append('lalal')                #append добалвяет что либо в конец списка
# print(my_list)


# my_list = [1, 4, 9, 6, 5]
# print(my_list)
# my_list.clear()                   #clear убирает абсолютно всё что было
# print(my_list)


# my_list = [1, 4, 9, 6, 5]
# print(my_list)
# my_list.remove(4)                    #remove убирает конкретно что-то из списка
# print(my_list)


# my_list = [1, 4, 9, 6, 5]
# print(my_list)
# my_list.pop(1)                     #pop убирает по номеру, например -1; 0  и т.д.
# print(my_list)


# my_list = [1, 4, 9, 6, 5]
# extension = [[4, 6, 8, 9]]
# my_list.extend(extension)        #extend добавляет в print-e список в список и выходит [1, 4, 9, 6, 5, [4, 6, 8, 9]]
# print(my_list)

#
# my_list = [1, 4, 9, 6, 5]
# print(my_list)
# my_list.insert(1, 2)                #insert первое число указывается номер, потом что надо добавить, после чего именно
# print(my_list)


# my_list = [1, 4, 9, 6, 5]
# print(my_list)
# my_list.sort(reverse=True)       #sort от меньшего до большего, а reverse=True от большего до маньшего
# print(my_list)


# my_list = [1, 4, 9, 6, 5]
# print(my_list)
# print(len(my_list))                 #len пишет сколько чисел входит в спискок


# my_list = [1, 4, 9, 6, 5]
# print(my_list)
# copy_list = my_list.copy()           #copy скопирует список
# print(copy_list)


my_list = [1, 4, 9, 6, 5]
if 111 in my_list:              #тут в коде главная цель есть ли в моём списке например 111, и вывод соотв. ответ
    print('Okey')
else:
    print('Bad')

# my_list = [1, 4, 9, 6, 5]
# for element in sorted(my_list):        #sorted выведет всё в столбик
#     print(element)


# my_list = [1, 66, 8, 30, 2, 2, 2]
# sum = 0
# for element in my_list:            # тут идёт сумма всех чисел
#     sum += element
# print(sum)


# my_list = [1, 66, 8, 30, 2, 2, 2]
# max = 0
# for element in my_list:
#     if element > max:
#         max = element             #max - большее число в списке
# print(max)


# my_list = [1, 66, 8, 30, 2, 2, 2]
# max = 66
# for element in my_list:
#     if element < max:
#         max = element             #тут ищем самое меньшее число
# print(max)


# my_list = ['abc', 'xyz', 'aba', '1221']
# count = 0
# for element in my_list:
#     if len(element) >= 2 and element[0] == element[-1]:
#         print(element)
#         count += 1
# print(count)


# list1 = ['1','2','3','4','5']
# list2 = ['5','6','7','8']
# result = False
# for i in list1:
#     for j in list2:
#         if i == j:
#             result = True         #тут ищем есть ли одиннаковое число в обоих списках
#             break
# print(result)


# color_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# color_list.remove('Green')
# color_list.remove('Black')
# print(color_list)


# number_list = [7, 8, 120, 44, 20, 27]
# for num in number_list:
#     if num % 2 != 0:
#         number_list.remove(num)
# print(number_list)


# while True:
#     name = input('Введите своё имя: ')
#     if name:
#         break
#     else:
#         print('Имя не введено')


# random_number = random.randint(1, 10)
# while True:
#     guess = int(input('Угадайте число от 1 до 10: '))
#     if guess == random_number:
#         print('Вы угадали')
#         break
#     else:
#         print('Попытайтесь заново')


# name = input('Введите своё имя: ')
# surname = input('Введите свою фамилию: ')
# a = 0
# b = 0
# for elem in name:
#     a += 1
# for sur in surname:
#     b += 1
# print(f'name: {a}')
# print(f'surname: {b}')
# print(f'both: {a+b}')


my_list = [1, 2, [3, 4, 7, 3, 1, 3, 6, 8, 0]]
for element in my_list:
    if type(element) == list:
        element.sort()
print(my_list)

tmp = my_list[-1]
my_list.pop(-1)

my_list.sort()











# task_4

# goods = ['Bananas']
# sold_goods = []
# while True:
#     match = input('Вітаю в системі магазину! \n\nДля показу всіх товарів натисніть 1. \nДля постачяння товарів натисніть 2.\n'
# 'Для продажу товарів натисніть 3 \nДля виводу проданих товарів за день натисніть 4. \nДля перегляду '
# 'історіі продажів натисніть 5. \nДля виходу натисніть 0:')
#     if match == '0':
#         print('спасибо вам!')
#         break
#     elif match == '1':
#         for good in goods:
#             print(good)
#     elif match == '2':
#         print('Продукты куплены')
#         product = input('Введите продукты какие бы вы хотели купить: ')
#         goods.append(product)
#     elif match == '3':
#         print('Проданніе товары')
#         product = input('Введите продукты какие бы вы хотели купить: ')
#         sold_goods.append(product)
#         goods.remove(product)
#     elif match == '4':
#         for good in sold_goods:
#             print(good)
#     elif match == '5':
#         for good in sold_goods.reverse():
#             print(good)




