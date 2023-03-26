# чтоб посчитать сколько слов без пробелов

# a = 'as sdf af '
# list_a = a.split()
# print(len(list_a))

# ------------------------------------------------

# currency = {
#      'USD': 36.42,
#      'EUR': 39.03,
#      'GBP': 43.84
# }
#
# currency['PNL'] = 7
# currency['USD'] = 39
# currency['EUR'] = 41
# currency['GBR'] = 44
# currency['CNY'] = 5.3
# currency['TRY'] = 1.93
#
# print(currency)
#
# currencies = input('Enter the currency you would like to exchange: ')
# amount = float(input('How much money you would like to exchange'))
#
# print(currency.values())
#
# if currencies not in currency not in currency.keys():
#     print('We don`t support such currency')
# else:
#     result = amount*currency[currencies]
#     print('Here is your {} UAH'.format(result))

# ------------------------------------------------

# numbers = {
#     1: 'one',
#     2: 'two',
#     3: 'three'
# }
# #
# for key in numbers:
#     print(key)
#
# for i in numbers.keys():
#     print(i)
#
# for i in numbers.values():
#     print(i)
#
# for key, value in numbers.items():
#     print(key, value)
#
# for key in numbers.keys():
#     numbers[key] = numbers[key]*2
#
# print(numbers)

# ------------------------------------------------

# transport = {
#     'AA1111AA': 'Іван Іванов',
#     'IVANOV': 'Іванов Іван',
#     'AA007AA': 'Іванов Іван'
# }
# transport['II6767A0'] = 'Петренко Петро'
# transport['CA8888CE'] = 'Ivan Олксій'
#
# car_plate = input('Enter the plate to find car owner: ')
# car_owners = transport.get(car_plate, 'Not found')
# print('Car owner of plate {} is {}'.format(car_plate, car_owners))
# for car_owner in transport.values():
#     if car_owners.get(owner, 0) == 0:
#         car_owners[owner] = 1
#     else:
#         auto_count = car_owners[owner]
