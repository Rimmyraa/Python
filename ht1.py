# Написати коротку інформацію про себе: ім'я, місто, вік, зріст, чи маєш домашнього улюбленця та ін.,
#використовуючи окрему змінну для кожного пункту інформації та якомога більше типів даних. Результат вивести в консоль.

name = input('Введите своё имя: ')
last_name = input('Введите вашу фамилию: ')
city = input('Введите город, страну в которой вы живете: ')
street = input('Введите улицу на которой вы живёте: ')
age = input('Введите ваш возраст: ')
height = input('Введите ваш рост: ')
pet = input('Вы имеете животных? Если да, то каких?: ')
hobby = input('Каким хобби вы занимаетесь: ')
music = input('Какую музыку вы слушаете: ')
print('Благодаря данным вопросам можно собрать ваш образ')
print(f'Вот что удалось о вас узнать. Вас зовут {name} {last_name}, вы проживаете в {city} на улице {street}. Вам {age}'
      f'лет, вы роста {height}. У вас есть {pet} и ваше хобби это {hobby}, также, вы предпочитаете слушать {music} музыку. ')

