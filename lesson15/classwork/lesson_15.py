# x = 50
# def func():
#     x = 2
#     print('Changing local x on', x)
#
# func()
# print(x)

# ------------------------------------------------

# x = 50
# a = 1
# def func():
#     global x, a    #global -  используется для объявления глобальной переменной внутри функции.
#     print('Now x is', x)
#     x = 2
#     print('Changing local x on', x)
#
# func()
# print(x)

# ------------------------------------------------

# def func(a, b=2, c=3):
#     print(f'a - {a}, c = {c}, b = {b}')

#func(5) #тут вместо оголошения  а=5 можно просто написать 5


# ------------------------------------------------

# def say(message, times=1):
#     message = message + ' '
#     print(message * times) #тут к одной строчке добавляем другую
#
# say('Hello')
# say('World', 5)

# ------------------------------------------------

# def total(a=5, *numbers, **phone_book):
#    print(f'a = {a}')
#    print(f'Args - {numbers}')
#    for single_item in numbers:
#        print(f'Single item - {single_item}')
#     for first_part, second_part in phone_book.items():
#         print(first_part, second_part)
# total(10, 1, 2, 3, 4, 5, Jack=233, Alice=2332, Jhon=1111)

# ------------------------------------------------

# аргумент с одной звезой "*" - кортеж
# аргумент с двумя звёздами "**" - якісь значення з'єднує в словник

# ------------------------------------------------

# subscribes_news = []
# subscribes_whats_news = []
# subscribes_ads = []
#
# def subscribe(email, is_news=True, is_whats_new=True, is_ads=True):
#     global subscribes_ads, subscribes_whats_news, subscribes_news
#     if is_news:
#         subscribes_news.append(email)
#     if is_whats_new:
#         subscribes_whats_news.append(email)
#     if is_ads:
#         subscribes_ads.append(email)
#
# def get_subscribers(subscribes_list, list_name):
#     delimeter = '-'*25
#     print(f'На розслику {list_name} підписалося {len(subscribes_list)} користувачів.')
#     print(user)
#     print(delimeter)
#     print()
#
# subscribe('test@gmail.com')
# subscribe('ivanov@ukr.net', True, False, True)
# subscribe('ivanova@ukr.net', False, True, True)
# get_subscribers(subscribes_news, 'News')
# get_subscribers(subscribes_ads, 'Advertisement')
# get_subscribers(subscribes_news, 'Whats new')
