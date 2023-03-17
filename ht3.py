# Написати програму, яка буде підраховувати суму всіх непарних чисел від 1 до 100.

# sum = 0
# for number in range(1, 100+1):
#     if number % 2 != 0:
#         print(number)
#         sum += number
# print('sum: ', sum)

# Написати програму, яка приймає на вхід рядок, введений з клавіатури, і підраховує кількість входження в рядок першої
# літери, з якої починається цей рядок

string = input('Enter your string: ')
first_char = string[0]  #самый первый отсчёт чего либо в python начинается с 0 а заканчивается на -1
count = 0
for char in string:
    if char == first_char:
        count += 1
print(f'Amount of the first letter {first_char} if {count}')
