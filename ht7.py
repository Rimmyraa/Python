# Домашнє завдання
# Дано рядок, який містить довільне речення, слова в якому розділені пробілами. З використанням зрізів знайти і вивести
# слово, як має найбільшу довжину.

string = input() + ' '
space = string.find(' ')
word = string[:space]
new_string = string[space+1:]

for i in range(string.count(' ')):
    space = new_string.find(' ')
    if len(new_string[:space]) >= len(word):
        word = new_string[:space]
    new_string = string[space + 1:]
print(f'The longest word is {word}')
