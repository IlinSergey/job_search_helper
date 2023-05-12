import psycopg2
from config import DB
from psycopg2 import Error


def connect():
    try:
        connection = psycopg2.connect(DB)
        return connection
    except Exception as error:
        print(error)


def create_table():
    try:
        connection = connect()
        cursor = connection.cursor()
        create_table_query = '''CREATE TABLE if NOT EXISTS vacantion
                                 (id SERIAL PRIMARY KEY,
                                 id_vacantion INT NOT NULL unique,
                                 name VARCHAR NOT NULL,
                                 url VARCHAR NOT NULL,
                                 description VARCHAR,
                                 date_published timestamptz,
                                 salary VARCHAR,
                                 is_showed BOOLEAN DEFAULT FALSE);
                                 '''
        cursor.execute(create_table_query)
        connection.commit()
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()


def record_vacation(id_vacation, name, url, descript, date, salary):
    try:
        connection = connect()
        cursor = connection.cursor()
        record_query = f'''INSERT INTO vacantion(id_vacantion, name, url, description, date_published, salary)
                        VALUES({id_vacation}, '{name}', '{url}', '{descript}', '{date}', '{salary}');'''
        cursor.execute(record_query)
        connection.commit()
    except (Exception, Error) as error:
        print(error)
    finally:
        if connection:
            cursor.close()
            connection.close()


def read_vacantion():
    try:
        connection = connect()
        cursor = connection.cursor()
        read_query = '''SELECT id, name, description, salary, url
                        FROM vacantion
                        WHERE is_showed = False
                        ORDER BY date_published
                        LIMIT 1'''
        cursor.execute(read_query)
        record = list((cursor.fetchall())[0])
        id_vacation = record[0]
        set_query = f'''UPDATE vacantion
                       SET is_showed = TRUE
                       WHERE id = {id_vacation}'''
        cursor.execute(set_query)
        connection.commit()
        return ("*".join(record[1:]))
    except (Exception, Error) as error:
        print(error)
    finally:
        if connection:
            cursor.close()
            connection.close()
