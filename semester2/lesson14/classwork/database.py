import psycopg2

def add_to_database(item):
    try:       
        connection = psycopg2.connect(
            host='ep-restless-thunder-068432.us-east-2.aws.neon.tech',
            port='5432',
            database='neondb',
            user='rimmyraa',
            password='uvQA3gf4rNDR'
        )
        
        cursor = connection.cursor()
        
        
        columns = ', '.join(item.keys())
        print(columns)
        
        values = ', '.join(['%s'] * len(item))
        print(values)
        """
        INSERT INTO devices (column1, column2, column3) VALUES (%s, %s, %s)
        """
        
        insert_query = f"INSERT INTO devices ({columns}) VALUES ({values})"
        cursor.execute(insert_query, list(item.values()))
        connection.commit()

        print('Success')
    except Exception as e:
        print(e)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print('Connection close')
        
test = {'name': 'Смартфон Apple iPhone 14 Pro Max 1Tb Deep Purple', 'code': '2149521', 'old_price': 82999, 'current_price': 79999, 'reviews': 13}

add_to_database(test)