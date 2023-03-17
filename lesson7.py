# строки/string

# a = 'My_awesome_string'
# b = "My_awesome_string"
# c = '''grgegegg
# rgegrgergeg
# egee'''
# print(b)
# print(c)

# ------------------------------------------------

# one_line_text = 'вот когда екст идёт одной строкой и оно длинное и короче слэш' \
#                 'переносит где хочешь, короче enter нажать и всё'
# print(one_line_text)

# ------------------------------------------------

# s = str(15)
# print(type(s))
#
# s = str([12, 1])
# print(type(s))

# ------------------------------------------------

# s = 'ABCDEFHG'
# firs_element = s[0]
# last_element = s[-1]
# e = s[4]
# print(firs_element)
# print(last_element)
# print(e)

# ------------------------------------------------

# a = 'Ivan Ivanov'
#
# first_element_of_the_name = a[0]
# first_element_of_the_surname = a[-4]
#
# if first_element_of_the_name == first_element_of_the_surname:
#     print('Первая буква имени совпадает с первом буквой фамилии')
# else:
#     print('Первая буква имени не совпадает с первом буквой фамилии')

# ------------------------------------------------

# s = 'ABCDEFHGHJKLMNOP'
# print(s[3:5])       #тоесть нам надо какой-то кусочек и выдадст DE

# print(s[:5])        #выведет всё, что было до 5 элемента  и выдадст ABCDE

# print(s[5:])        #тут будет всё с 5 элемента и выведет HGHJKLMNOP

# print(s[::-1])      #перевёртыш

# print(s[:-5])       #все символы от А до K тобиш ABCDEFHGHJK

# print(s[-1:-6:-2])  #PNL от -1 до -6, этот кусочек, а -2 это то число из этого кусочка

# ------------------------------------------------

# my_list = [1, 2, 3]
# my_list[0] = 4
# print(my_list)

# ------------------------------------------------

# a = 'Hello, '
# b = 'World'
#
# print(a+b)
#
# delimiter = '-' * 150
# print(len(delimiter))

# ------------------------------------------------

# a = 'Jingle bells, jingle bells \nJingle all the way \nOh, what fun it is to ride \nIn a one horse pen sleigh'
# print(a)

# ------------------------------------------------

# a = 'Jingle bells, jingle bells Jingle all the way Oh, what fun it is to ride In a one horse pen sleigh'
# for char in a:
#     print(char)     # char делает по букве на строку

# ------------------------------------------------

# a = 'Hello World'
# print(a.lower())    #lower будут писаться  с маленькой буквы/нижний регистр  hello world
#
# a = 'Hello World'
# print(a.upper())     #  upper HELLO WORLD
#
#
# a = 'Hello World'
# print(a.capitalize())  #  capitalize Hello world
#
#
# a = 'Hello World'
# print(a.swapcase())   #  swapcase hELLO wORLD
#
#
# a = 'hellO worlD'
# print(a.title())     #  title из уродца делает норм и выходит Hello World

# ------------------------------------------------

# s = 'Hi there!'
# start = 0
# end = 5
#
# print(s.find('er', 0, 7))     # тут аходит нужный символ под индексом где оно находиться
# print(s.find('i'))

# ------------------------------------------------

# e = 'Big, Bigger, Biggest'
# x = e.rfind('Big')
# print(x)

# ------------------------------------------------

# stop_words = ['купити', 'продати', 'реклама']
# user_string = input()
# for stop_word in stop_words:
#     if user_string.find(stop_word) != -1:
#         print('It\'s spam message')
#         break
# else:
#     print('It\'s not spam')

