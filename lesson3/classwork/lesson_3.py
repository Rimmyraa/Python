# num = float(input("Введите число: "))
# if num % 1 == 0:
#     print('Целое число')
# else:
#     print('Не целое')


# num = int(input("Введите число: "))
# if num % 5 == 0 or num % 10 == 0:
#     print('Ваше число делить на 5/10')
# else:
#     print('Ваше число не делиться на 5/10')


# num1 = int(input("Введите первую сторону: "))
# num2 = int(input("Введите вторую сторону: "))
# if num1 == num2:
#     print("Это квадрат")
# else:
#     measurement
#     print('Это прямогульник')
# else:
#     print('Введите заново')


# month = int(input('Введите месяц своего рождения (цифра): '))
# day = int(input('Введите день своего рождения: '))
# if month > 12 or day > 31:
#     print('Введите заново')
# else:
#     print(f'Ваше др {month} {day} ')

# month = int(input('Введите месяц своего рождения (цифра): '))
# day = int(input('Введите день своего рождения: '))
# print('Ok') if month <= 12 and day <= 31 else print('Wrong input')     #тернарный оператор


# week_day = int(input('Day: '))
# if week_day == 1:
#     print('Monday')
# elif week_day == 2:
#     print('Tuesday')
# elif week_day == 3:
#     print('Wednesday')
# elif week_day == 4:
#     print('Thursday')
# elif week_day == 5:
#     print('Friday')
# elif week_day == 6:
#     print('Saturday')
# elif week_day == 7:
#     print('Sunday')
# else:
#     print('wrong input!')


# week_day = int(input('Day: '))
# match week_day:
#     case 1:
#         print('Monday')
#     case 2:
#         print('Tuesday')
#     case 3:
#         print('Wednesday')
#     case 4:
#         print('Thursday')
#     case 5:
#         print('Friday')
#     case 6:
#         print('Saturday')
#     case 7:
#         print('Sunday')
#     case _:
#         print('wrong input!')


# num1 = int(input("Введите первое число: "))
# num2 = int(input("Введите второе число: "))
# x = num1 + num2
# print(num1 + num2)
# print(str(num1) + str(num2))


# name = input('Введите свое имя: ')                #написать без использования f
# city = input('Введите город в котором вы живете: ')
# hello = 'Привет '
# town = ' из города '
# print(hello + name + town + city )


# name = input('Введите своё имя: ')
# if not name:
#     print('Вы не ввели имя, поэтому не получите скидку')
# elif name == 'Андрей':
#     print('Вы получаете скидку 25%')
# else:
#     print('Вы получаете скидку 15%')


# num = int(input('Введите число: '))
# print('Парное') if num % 2 == 0 else print('Не парное')     #тернарный оператор


# angle1 = int(input('Введите первый угол: '))
# angle2 = int(input('Введите второй угол: '))
# angle3 = int(input('Введите третий угол: '))
# if angle1 + angle2 + angle3 == 180:
#     print('Это правильный треугольник')
# else:
#     print('Это не правильный треугольник')