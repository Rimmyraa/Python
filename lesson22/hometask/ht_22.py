# ДЗ:
# Створити програму, яка запитує імена користувачів, та дозаписує їх у файл,
# допоки користувач не введе "q" (цикл обривається)

file = open('D:\python\learning\Schoology\lesson22\hometask\ht.txt', 'w')

while True:
    name = input('Введите имя: ')
    if name == 'q':
        break
    else:
        file.write(f'{name}')

file.close()

# не выходит записать имя в файл, записываеться только q