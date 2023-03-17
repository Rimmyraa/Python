# Потрібна функція яка може перетворити число у рядок.

# def number_to_string():
#     number = int(input('Введите число: '))
#     return str(number)
#
# number_to_string()

# ------------------------------------------------

# Заповніть метод, який отримує логічне значення і повертає рядок "Yes" для true, або рядок "No" для false

# def False_True(val):
#     yes = 'Yes'
#     no = 'No'
#     if val == 'True':
#         return yes
#     else:
#         return no
#
# print(False_True('True'))

# ------------------------------------------------

#перетворити число в обернений масив цифр
#35231 => [1, 2, 3, 4, 5]

# def numbers(num):
#     a_list = list(num)
#     return a_list.reverse()
#
# print(numbers(1325))

# ------------------------------------------------

def game(player1, player2):
    scissors = 'scissors'
    paper = 'paper'
    rock = 'rock'
    print(f'Possible characters - {scissors}, {paper}, {rock}')
    player1 = input('Choose your character: ')
    player2 = input('Choose your character: ')
    if player1 == player2:
        print('Draw!')
    elif player1 == scissors or player1 == rock and player2 == paper:
        print('Player1 won!')
    elif player2 == scissors or player2 == rock and player1 == paper:
        print('Player2 won!')

game('rock', 'paper')