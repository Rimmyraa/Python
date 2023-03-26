# task_1

# clitent = [
#     ['White House', 'Іванов', 3],
#     ['Shelter', 'Іванова', 5],
#     ['Верховина', 'Іванова', 5],
#     ['Буковель', 'Іванова', 5]
# ]

# hotels = dict()

# for vouncher in clitent:
#     vouncher_hotel = vouncher[0]
#     vouncher_clients = vouncher_hotel[2]

#     if hotels.get(vouncher_hotel, 0) == 0:
#         hotels[vouncher_hotel] = vouncher_clients
#     else:
#         hotel_clients = hotels[vouncher_hotel]
#         hotels[vouncher_hotel] = hotel_clients + vouncher_clients

# for hotels, clients in hotels.items():
#     print(f'У готелі {hotels} наразі проживає {clients} клієнтів.')

# ------------------------------------------------

# функції -  это объект, принимающий аргументы и возвращающий значение

# функції - (оголошується з def(); то, что в скобках - это параметры )

# ------------------------------------------------

# def say_hello():
#     print('Hello, World <3')

# say_hello() # - это выводит, а принт просто оголошує

# ------------------------------------------------

# def say_hello():
#     print('Сергеева Римма')
#
# say_hello()

# ------------------------------------------------

# def print_sum():
#     a = 7
#     b = 9
#     print(a+b)
# print_sum()

# ------------------------------------------------

# def draw_box():
#     print('*' * 10)
#     for i in range(12):
#         print('*' + ' '*8 + '*' )
#     print('*' * 10)
#
# draw_box()

# ------------------------------------------------

# def draw_stairs():
#     for i in range(10):
#         i += 1
#         print('*' * i)
#
# draw_stairs()

# ------------------------------------------------

# def draw_stairs(x):
#     for i in range(x):
#         i += 1
#         print('*' * i)

# size_of_stairs = int(input())
# draw_stairs(size_of_stairs)

# draw_stairs(25) # - тут указываем до скольки * будет идти треугольгник

# ------------------------------------------------
#
# def print_max(a, b):
#     if a > b:
#         print(f'Max - {a}')
#     elif a == b:
#         print('They are equal')
#     else:
#         print(f'Max - {b}')


# x = 15    # - тут уже сами указываем что будет а и б, но только в другом варианте
# y = 7
# print_max(x, y)

# print_max(7, 5) # - тут указывает, где "а" и "б"

# ------------------------------------------------

# def student_name():
#     name = input('Введите своё имя: ')
#     print(f'Hello {name}')
#
# student_name()

# ------------------------------------------------

# return - возварщает значение из функции

# def plus(a, b):
#     result = a+b
#     return result

# #plus(3, 4) # - мы получим ничего, потому что функция ретёрн возвращает ЗНАЧЕНИЕ

# print(plus(3, 4)) # - а это уже выведет

# ------------------------------------------------

# def suma(a, b):
#     return a + b
#
# def subtraction(a, b):
#     return a - b
#
# def power(a, b):
#     return  a ** b
#
# def mytiply(a, b):
#     return a * b
#
# def calcultion(operand_A, operand_B, operator):
#     if operator not in ['+', '-', '*', '^']:
#         print('Invalid operator')
#     else:
#         match operator:
#             case '+':
#                 result = suma(operand_A, operand_B)
#             case '-':
#                 result = subtraction(operand_A, operand_B)
#             case '*':
#                 result = mytiply(operand_A, operand_B)
#             case '^':
#                 result = power(operand_A, operand_B)
#
#         print(operand_A, operator, operand_B, '=', result)
#
# a = float(input('Enter the first number: '))
# b = float(input('Enter the second number: '))
#
# print('Avialable operators - [+, -, *, ^]')
#
# operation = input('Enter the operation: ')
#
# calcultion(operand_A=a ,operand_B=b, operator=operation)


