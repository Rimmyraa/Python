# import random
#
# b = ['Good morning', 'Good day', 'God afternoon']
#
# a = random.choice(b)
# random_number = random.randint(0, 20)
#
# print(random_number)
# print(a)

# ------------------------------------------------

# a = 5
#
# while a != 0:
#     print(a)
#     a -= 1

# /////////////////////////////////////////////////

# while True:
#     username = input('Enter your name: ')
#     if username == '0':
#         break
#     else:
#         print(username)

# ------------------------------------------------

# def greeting(name):
#     return f'hello {name}!'
#
# print(greeting('Rimma'))

# ------------------------------------------------

# *args - как список, но в квадратных скобках, только его нельзя изменять
# **kwargs - небольшие словники, которые имеют ключ - заначення, наприклад а = 7

# def greeting(name, number, *args, **kwargs):   #тут number забиает первое зачение, вот я указала как 1, оно идет после 'Rimma'
#     greetings_string = f'Hello {name}'
#     print('Args - ', args)
#     print('Kwargs - ', kwargs)
#     result = [greetings_string, number, sum(args), kwargs]
#     return result
#
# a = greeting('Rimma', 1,2,3,4,5,22,23,45,76, a=7, b='John', c=15)
# print(a)

# ------------------------------------------------

# numbers = [6, 2, 1, 8, 10]
#
# def func(list):
#     return {
#         'sum_max_min': max(list) + min(list),
#         'sum_rest': sum(list) - (max(list) + min(list))
#     }
#
# print(func(numbers))

# ------------------------------------------------

file = open('')

