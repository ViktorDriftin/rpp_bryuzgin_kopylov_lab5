import sqlite3 # импортирует модуль, чтобы работать с базами данных SQLite
import pandas as pd # импортируем библиотеку для анализа данных


# определяем функцию для создания таблицы "users" в базе данных Sqlite
def create_table():
    conn = sqlite3.connect('users') # создаем соединение с базой данных "users"
    cursor = conn.cursor() # создаём курсор для выполнения SQL-запросов
    cursor.execute("""CREATE TABLE IF NOT EXISTS users
                   (id INTEGER NOT NULL,
                   name varchar (70), 
                   email varchar (70), 
                   PRIMARY KEY (id));""") # добавляем первичный ключ
    conn.commit() # сохраняем изменения в базе данных
    conn.close() # закрываем соединение с базой данных

#определяем функцию, которая принимает 3 аргумента, для добавления нового пользователя в таблицу
def insert_new_users(id, name, email):
    conn = sqlite3.connect('users') #создаем соединение с базой данных "users"
    cursor = conn.cursor() #создаём курсор для выполнения SQL-запросов
    #добавляем новых пользователей в таблицу "users" с помощью параметризованного запроса
    cursor.execute("""insert into users (id, name, email)
                   VALUES  (:id, :name, :email) """, {"id":id, "name":name, "email":email}) #значения для параметров id, name и email передаются в виде словаря.
    conn.commit() #сохраняем изменения в базе данных
    conn.close() #закрываем соединение с базой данных

# определяем функцию для получения всех пользователей
def select_all_users():
    conn = sqlite3.connect('users') # создаем соединение с базой данных "users"
    cursor = conn.cursor() # создаём курсор для выполнения SQL-запросов
    cursor.execute("""select * from users """) # выполняем запрос на выбор всех записей из таблицы "users"
    df = pd.DataFrame(cursor.fetchall(), columns = ['id', 'name', 'email']) # создаем объект DataFrame из результата запроса с указанием названий столбцов
    print(df) # выводим на экран DataFrame с выбранными данными
    conn.commit() # сохраняем изменения в базе данных
    conn.close() # закрываем соединение с базой данных

# определяем функцию, которая принимает аргумент, для получения пользователя по id
def select_users_id(id):
    conn = sqlite3.connect('users') # создаем соединение с базой данных "users"
    cursor = conn.cursor() # создаём курсор для выполнения SQL-запросов
    # выполняем запрос на выборку всех строк из таблицы "users", где значение поля "id" равно заданному параметру `id`
    cursor.execute("""select * from users
                  where id=:id""", {"id":id})
    print(cursor.fetchone()) #  печатаем результат запроса
    conn.commit() # сохраняем изменения в базе данных
    conn.close() # закрываем соединение с базой данных

# определяем функцию, которая принимает аргумент, для удаления пользователя по id
def delete_users_id(id):
    conn = sqlite3.connect('users') # создаем соединение с базой данных "users"
    cursor = conn.cursor() # создаём курсор для выполнения SQL-запросов
    # выполняем запрос на удаление пользователя с указанным id
    cursor.execute("""delete  from users
                   where id=:id""", {"id":id})
    conn.commit() # сохраняем изменения в базе данных
    conn.close() # закрываем соединение с базой данных

# определяем функцию, которая будет удалять таблицу "users" из базы данных
def drop_function():
    conn = sqlite3.connect('users') # создаем соединение с базой данных "users"
    cursor = conn.cursor() # создаём курсор для выполнения SQL-запросов
    cursor.execute("""drop table users""") # выполняем запрос на удаление таблицы "users"
    conn.commit() # сохраняем изменения в базе данных
    conn.close() # закрываем соединение с базой данных

# определяем функцию для последовательного выполнение всех функциий сверху
def main():
    create_table() #вызываем функцию для создания таблицы в базе данных
    insert_new_users(1, 'Кирилл', 'kirill.kopylov.01@mail.ru') # вызываем функцию для добавления новых записей пользователей в базу данных
    insert_new_users(2, 'Витя', 'Vityasuperrrr@mail.ru')
    insert_new_users(3, 'Керел', 'Kir4iK@mail.ru')
    insert_new_users(4, 'Виктор', 'Vityamba@mail.ru')
    select_all_users()  # вызываем функцию для получения всех пользователей из базы данных
    select_users_id(3)  # вызываем функцию для получения пользователя по id
    delete_users_id(4)  # вызываем функцию для удаления пользователя по id
    select_all_users()  # вызываем функцию для получения всех пользователей из базы данных (после удаления)
    #drop_function() - вызываем функцию для удаления таблицы в базе данных
main() # вызываем функцию main() для выполнения всего кода.