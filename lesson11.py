# словники/словари

# словник - це контейнер,який зберігає пари "ключ" - "значення"
# dict = {x:x}

# a = dict     # можно оставить - {}
# print(type(a))

# ------------------------------------------------

# months = {1: 'January',
#           2: 'February',
#           3: 'March',
#           4: 'April',
#           5: 'May'
#          }
# print(' ')
# months[6] = 'June'
# months[7] = 'July'
# months[8] = 'August'
# months[9] = 'September'
# print(months)
#
# a3 = months.pop(3)
# print(a3)
#
# a4 = months.pop(4)
# a5 = months.pop(5)
# print(a4, a5)
#
# months.update({10: 'October', 11: 'November', 12: 'December'})
# print(months)
#
# print(months)

# ------------------------------------------------

# months = {1: 'January',
#           2: 'February',
#           3: 'March',
#           4: 'April',
#           5: 'May',
#           6: 'June',
#           7: 'July',
#           8: 'August',
#           9: 'September',
#           10: 'October',
#           11: 'November',
#           12: 'December'
#          }
#
# report_date = '21.06.2022'
#
# month = int(report_date[3:5])
#
# month_name = months.get(month)
#
# print('Report from', month_name)

# ------------------------------------------------

# currency = {
#      'USD': 36.42,
#      'EUR': 39.03,
#      'GBP': 43.84
# }
# print(currency)
# print(currency.get('PNL', 'Current currency doesn`t exist'))
# print(currency['USD'])

