# Користувач має ввести 3 сторони трикутника. Перевірити чи трикутник може існувати.
# Підказка: Трикутник існує, якщо сума двох сторін буде більшою за третю сторону

angle1 = int(input('Введите первый угол: '))
angle2 = int(input('Введите второй угол: '))
angle3 = int(input('Введите третий угол: '))
sum = angle1 + angle2
if sum > angle3:
    print('Треугольник с данными параметрами существует')
else:
    print('Треугольник с данными параметрами не существует')