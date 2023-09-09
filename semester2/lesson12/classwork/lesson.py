import psycopg2


def registration():
    try:
        connection = psycopg2.connect(
            host='ep-restless-thunder-068432.us-east-2.aws.neon.tech',
            port='5432',
            database='neondb',
            user='rimmyraa',
            password='uvQA3gf4rNDR'
        )

        cursor = connection.cursor()

        query = 'INSERT INTO students (name, age, email) VALUES (%s, %s, %s)'
        cursor.execute(query, ('Kolya', '16', 'kolya@mail.com'))
        cursor.execute(query, ('Danil', '17', 'dania@mail.com'))
        cursor.execute(query, ('Artem', '16', 'tema@mail.com'))
        connection.commit()

        print('Student successfully registered!')
    except Exception as error:
        print('An error occurred while registering user: ', error)
    finally:
        if connection:
            connection.close()
            cursor.close()


registration()