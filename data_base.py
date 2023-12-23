# import psycopg2
# from psycopg2 import Error

# from config import DB


# def connect():
#     try:
#         connection = psycopg2.connect(DB)
#         return connection
#     except Exception as error:
#         print(error)


# def create_table_user():
#     try:
#         connection = connect()
#         cursor = connection.cursor()
#         create_table_query = """CREATE TABLE if NOT EXISTS users
#                                  (id SERIAL PRIMARY KEY,
#                                  user_id INT NOT NULL unique,
#                                  first_name VARCHAR,
#                                  last_name VARCHAR,
#                                  username VARCHAR NOT NULL,
#                                  chat_id INT NOT NULL,
#                                  vacancy VARCHAR);
#                                  """
#         cursor.execute(create_table_query)
#         connection.commit()
#     except (Exception, Error) as error:
#         print("Ошибка при работе с PostgreSQL", error)
#     finally:
#         if connection:
#             cursor.close()
#             connection.close()


# def create_table_vacation():
#     try:
#         connection = connect()
#         cursor = connection.cursor()
#         create_table_query = """CREATE TABLE if NOT EXISTS vacantion
#                                  (id SERIAL PRIMARY KEY,
#                                  user_id INT,
#                                  id_vacantion INT NOT NULL unique,
#                                  name VARCHAR NOT NULL,
#                                  url VARCHAR NOT NULL,
#                                  description VARCHAR,
#                                  date_published timestamptz,
#                                  salary VARCHAR,
#                                  is_showed BOOLEAN DEFAULT FALSE,
#                                  FOREIGN KEY(user_id)
#                                  REFERENCES users(user_id)
#                                  ON DELETE CASCADE);
#                                  """
#         cursor.execute(create_table_query)
#         connection.commit()
#     except (Exception, Error) as error:
#         print("Ошибка при работе с PostgreSQL", error)
#     finally:
#         if connection:
#             cursor.close()
#             connection.close()


# def create_user(effective_user, chat_id):
#     try:
#         connection = connect()
#         cursor = connection.cursor()

#         record_query = f"""INSERT INTO users(user_id, first_name, last_name, username, chat_id, vacancy)
#                         VALUES({effective_user.id}, '{effective_user.first_name}',
#                               '{effective_user.last_name}', '{effective_user.username}',
#                               {chat_id}, 'None');"""
#         cursor.execute(record_query)
#         connection.commit()
#     except (Exception, Error) as error:
#         print(error)
#     finally:
#         if connection:
#             cursor.close()
#             connection.close()


# def set_vacancy(effective_user, vacany_name):
#     connection = connect()
#     cursor = connection.cursor()
#     set_query = f"""UPDATE users
#                     SET vacancy = '{vacany_name}'
#                     WHERE user_id = {effective_user.id}"""
#     cursor.execute(set_query)
#     connection.commit()


# def find_record(id_vacation):
#     connection = connect()
#     cursor = connection.cursor()
#     find_query = f"""SELECT EXISTS(SELECT * FROM vacantion WHERE id_vacantion = {id_vacation})"""
#     cursor.execute(find_query)
#     result = list(cursor.fetchone())[0]
#     return result


# def is_user(user_id):
#     connection = connect()
#     cursor = connection.cursor()
#     find_query = f"""SELECT EXISTS(SELECT * FROM users WHERE user_id = {user_id})"""
#     cursor.execute(find_query)
#     result = list(cursor.fetchone())[0]
#     return result


# def find_vacancy_name(user_id):
#     connection = connect()
#     cursor = connection.cursor()
#     find_query = f"""SELECT vacancy FROM users WHERE user_id = {user_id}"""
#     cursor.execute(find_query)
#     result = list(cursor.fetchone())[0]
#     return result


# def record_vacation(id_vacation, name, url, descript, date, salary, user_id):
#     try:
#         if not find_record(id_vacation):
#             connection = connect()
#             cursor = connection.cursor()
#             record_query = f"""INSERT INTO vacantion(id_vacantion, name, url, description,
#                                                      date_published, salary, user_id)
#                             VALUES({id_vacation}, '{name}', '{url}', '{descript}',
#                                   '{date}', '{salary}', {user_id});"""
#             cursor.execute(record_query)
#             connection.commit()
#     except (Exception, Error) as error:
#         print(error)
#     finally:
#         if connection:
#             cursor.close()
#             connection.close()


# def read_vacantion(user_id):
#     try:
#         connection = connect()
#         cursor = connection.cursor()
#         read_query = f"""SELECT id, id_vacantion, name, description, salary, url
#                         FROM vacantion
#                         WHERE (is_showed = False AND user_id = {user_id})
#                         ORDER BY date_published
#                         LIMIT 1"""
#         cursor.execute(read_query)
#         try:
#             record = list((cursor.fetchall())[0])
#             id_vacation = record[0]
#             set_query = f"""UPDATE vacantion
#                         SET is_showed = TRUE
#                         WHERE id = {id_vacation}"""
#             cursor.execute(set_query)
#             connection.commit()
#             return ("*".join(record[2:]), record[1])
#         except IndexError:
#             pass
#     except (Exception, Error) as error:
#         print(error)
#     finally:
#         if connection:
#             cursor.close()
#             connection.close()


# if __name__ == "__main__":
#     create_table_user()
#     create_table_vacation()
