
# my_string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam malesuada, est vitae suscipit vestibulum,"
# a = int(input('Введите число: '))
#
# if a > len(my_string):
#     print('Wrong input!')
# else:
#     new_string = my_string[a:]
#     print(new_string)

# ------------------------------------------------

# s = "I`m learning strings in Python. Some new methods got now"
# sentences = s.split('. ')
# sentences.pop(-1)
#
# print(sentences)

# ------------------------------------------------

# a = input('Введите что угодно: ')
# print(f'Символы - {len(a)}')
# b = a.split()
# print(b)
# print(f'Слов - {len(b)}')

# ------------------------------------------------

# s = ["I`m learning strings in Python. Some new methods got now"]
# text = '. '.join(s)
# print(text)

# ------------------------------------------------

# clean = '   spacious;   '.strip()
# print(clean)

# ------------------------------------------------

# dog_text = 'All dogs bark like dogs'
# print(dog_text)
# cat_text = dog_text.replace('dogs', 'cats')
# print(cat_text)

# ------------------------------------------------

# map = {ord('з'): 'z',
#        ord('ю'): 'u',
#        ord('a'): 'a'}

# translated = 'зюа'.translate(map)
# print(translated)

# ------------------------------------------------

# s = 'Мене звати %s. Мені %d років.' % ('Олег', 14)
# print(s)

# s = 'Мене звати {0}. Мені {1} років.'.format('Олег', 14)
# print(s)

# ------------------------------------------------

# print('pi: {:0.6}'.format(3.141526))     # тут идёт сокращение после 6 символа
#
# print(' "{}" "{:+}" "{:-}" "{: }" '.format(1, 2, -3, 4))

# print("|{:<10}|{:*^10}|{:>10}|".format('left', 'center', 'right'))

# ------------------------------------------------

# delimiter = '-' * 80
# goods = [['Апельсин', 6, 150], ['Лимон', 8, 90], ['Картопля', 123, 445]]
# total_sum = 0
# number = 0
#
# print(delimiter)
# print("|{:^5}|{:<40}|{:>15}| {:>14}|".format('#', 'Товар', "Кількість", "Вартість"))
# print(delimiter)
#
# for good in goods:
#     name = good[0]
#     amount = good[1]
#     money = good[2]
#     number += 1
#     total_sum += money
#     print("|{:^5}|{:<40}|{:>15}|{:>15}|".format(number, name, amount, money))
#
# print(delimiter)
# print("|{:<62}|{:>15}|".format(' Total:', total_sum))
# print(delimiter)
