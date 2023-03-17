# зрізи та множини

# ------------------------------------------------
# вывести все парные с помощью слайснингу

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_numbers = numbers[1:-1:2]     # двойка в конце, это через какой-то промежуток чисел, типа через 1 число
# odd_numbers = numbers[0:-1:2]      # двойка в конце, это через какой-то промежуток чисел, типа через 1 число
# some_numbers = numbers[2:-1:3]     # [3, 6, 9]

# print(even_numbers)
# print(odd_numbers)
# print(some_numbers)

# ------------------------------------------------

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# print(numbers[0:6])   #[1, 2, 3, 4, 5, 6]
# print(numbers[6:])    #[7, 8, 9, 10]
# print(numbers[:6])    #[1, 2, 3, 4, 5, 6]

#копирование списков
# b = numbers.copy()
# c = numbers[:]

# print(numbers[-2:])   #[9, 10]
# print(numbers[:-2])   #[1, 2, 3, 4, 5, 6, 7, 8]
# print(numbers[::-1])  #[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# ------------------------------------------------

# pip = 'Ivan Ivanov'
# delimiter = ' '
# space = pip.find(delimiter)
# print(space)
# name = pip[0:space]
# last_name = pip[space+1:]
# print(name, last_name)

# ------------------------------------------------

# phones = ['+380(067) 999-99-99', '+380(066) 999-99-99', '+380(067) 888-88-88', '+380(067) 777-77-77']
# kiivstar = ['067', '098', '068']
# count = 0
# for element in phones:
#     operator_code = element[4:7]
#     if operator_code in kiivstar:
#         count += 1
#
# print(count)

# ------------------------------------------------

# a = set('hello')
# b = {1, 2, 3, 4, 1, 1, 3, 3, 2, 2, 2}
#
# print(b)

# ------------------------------------------------

# c = {'067', '068', '099'}
# print(c)

# ------------------------------------------------

# numbers = {1, 2, 3}
# numbers.add(4)   # add добавляет = {1, 2, 3, 4}
# print(numbers)
#
# numbers = {1, 2, 3}
# numbers.remove(3)    #remove удаляет из списка, если то, что мы удаляет в сиске нет, выдаст ошибку
# print(numbers)
#
# numbers = {1, 2, 3}
# numbers.discard(5)    #discard удаляет из списка, если то, что мы удаляет в сиске нет, НЕ выдаёт ошибку
# print(numbers)

# ------------------------------------------------

# goods = {'banana', 'milk', 'apples', 'peach'}
# print(goods)
# goods.add('tomatoes')
# print(goods)
# goods.discard('banana')
# print(goods)

# ------------------------------------------------

# a = set('hello')
# b = set('hi there!')
# print(a)
# print(b)
# print(a ^ b)   # ^ - выдаёт разницу, например в первом сете нет ! а в другом есть
#
#
# a = set('hello')
# b = set('hi there!')
# print(a | b)  # | - выдасть все елементы что былм использованы в обоих сетах {'t', 'e', '!', 'h', 'l', 'i', 'o', ' ', 'r'}
#
#
# a = set('hello')
# b = set('hi there!')
# print(a.union(b))
#
#
# a = set('hello')
# b = set('hi there!')
# print(a & b)
#
#
# a = set('hello')
# b = set('hi there!')
# print(a.intersection(b))



