#🏠 Домашнє завдання:
#-Дано словник, який містить «Прізвище»-«оцінка».
#На його основі створити новий словник, який буде містити лише учнів, які навчаються на 4 та 5.

grades = {
    'Dmytro': 2,
    'Anna': 5,
    'Mykyta': 3,
    'Andrii': 4
}

good_grades = dict()
for student_name, grade in grades.items():
    if grade >= 4:
        good_grades[student_name] = grade

print(good_grades)

# ------------------------------------------------

#Погода. У словнику збережено інформацію про температуру в різних містах: ключами є назви міст,
#значеннями - температура. Розрахуйте середню температуру за вказаними містами

forecast = {
    'Kyiv': 25,
    'Chercasy': 27,
    'Odessa': 30,
    'Donetsk': 26
}

total_temperture = 0
count = len(forecast)

for temp in forecast.values():
    total_temperture += temp
print(f'Avg of temperatures = {total_temperture/count}')