# Завдання_1
# Порахувати, яка літера найчастіше зустрічається у вашому прізвищі.

name = input('Напишите ваше имя и фамилию: ')
count = 1
for letter in name:
    symbol = name.count(letter)
    if symbol > count:
        count = symbol
        s = letter
print(f'Больше всего в имени встречается буква - {s}')

# Завдання_2
# Ввести рядок з клавіатури. Видалити з неї всі цифри.

my_string = input('Введите что угодно: ')
num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
for num in my_string:
    print(my_string.replace(num, ''))
print(my_string)
