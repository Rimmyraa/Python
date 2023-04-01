# file = open('D:/python/learning/Schoology/lesson23/classwork//text', 'w')
# file.write('Orange\n')
# file.write('Banana\n')
# file.close()
#
# file = open('D:/python/learning/Schoology/lesson23/classwork//text')
# a = open('D:/python/learning/Schoology/lesson23/classwork//file', 'w')
#
# while True:
#     symbol = file.read(1)
#     if len(symbol) == 0:
#         print('The end of the file.')
#         break
#     else:
#         a.write(f'{symbol}\n')
#
# a.close()
# file.close()

# ------------------------------------------------

# file = open("D:/python/learning/Schoology/lesson23/classwork//seek")
#
# try:
#     print(file.read(3))
# finally:
#     print('The end of the statement')
#     file.close()

# ------------------------------------------------

# try:     # призначення відловлювати помилки
#     file.open("D:/python/learning/Schoology/lesson23/classwork//seek")
# except Exception as e:
#     print('An Error has occured:', str(e))
#
# print('Some next code')

# ------------------------------------------------

# with - открівается файл, только в другом формате
# with open("D:/python/learning/Schoology/lesson23/classwork//seek") as file:
#     file.seek(2)
#     print(file.read(1))