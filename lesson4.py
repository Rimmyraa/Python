# цикл

# word = 'apple'
# for char in word:
#     print(char, sep='-')


# numbers = [int(i) for i in input().split()]           #список
# print(numbers)

# numbers = input().split()
# for number in numbers:
#     int(numbers)
# print(numbers)
# print(type(numbers))


# sum = 0
#
# for number in numbers:
#     print(number)
#     sum = sum + number
# print(sum)


# colors = ['red', 'green', 'blue', 'yellow']
# for color in colors:
#     print(color)

# colors = ['red', 'green', 'blue', 'yellow']
# for color in colors:
#     print(color)
# else:
#     print('Done!')


numbers = [1, 3, 2, 45, 22, 664]
for number in numbers:
    if number % 2 == 0:
        print(number)


# range = (start, end, step) - пример.
# for i in range(1, 7+1, 2):
#     print(i, end=' ')


# sum = 0
#
# for i in range(1, 7+1, 2):
#     print(i)
#     sum = sum + i
# print(sum)


for i in range(1, 11):
    for j in range(1, 11):
        print(i*j, end=' ')
    print('')


# max = int(input('Размер таблицы: '))
# for now in range(1, max+1):
#     for column in range(1, max+1):
#         print(column*row, end='\t')
#     print('')


# a = 1
# print(1)
# while a <= 5:
#     a += 1
#     print(a)


# while True:
#     name = input('Enter name: ')
#     if name == 'stop':
#         print('Stopped!')
#         break
#     print('Hello' name)

#
# a = 0
# while a < 6:
#     a = a + 1
#     if not a % 2:
#         continue
#     print(a)
# print(not 6 % 2)


# while True:
#     i = int(input())
#     if i > 100:
#         break
#     if i < 20:
#         continue
#     print(i)



