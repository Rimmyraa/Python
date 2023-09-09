import psycopg2

def replace(email: str):
    try:
        connection = psycopg2.connect(
                user='rimmyraa',
                database='neondp',
                password='uvQA3gf4rNDR',
                host='ep-restless-thunder-068432.us-east-2.aws.neon.tech',
                port='5432'
        )

        cursor = connection.cursor()

        query = 'SELECT * FROM students WHERE email = %s'
        cursor.execute(query, (email))

        user = cursor.fetchone()

        if user:
            user_id = user[0]
            update_query = 'UPDATE students WHERE id = %s'
            cursor.execute(update_query, (user_id))
            connection.commit()
            print('Користувач був знайдений')
        else:
            print('Данного користувача не знайдено')

        cursor.close()
        connection.close()

    except Exception as error:
        print('Виникла помилка при вході в систему:', error)


if __name__ == "__main__":
    email = input('Email: ')
    replace(email)
