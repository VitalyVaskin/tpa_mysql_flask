import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO defects (number, equipment, description, user_start) VALUES (?, ?, ?, ?)",
            (15, 'Загрузчик', 'Отказ', 'Иванов')
            )
cur.execute("INSERT INTO defects (number, equipment, description, user_start) VALUES (?, ?, ?, ?)",
            (4, 'ТПА', 'Сбилось сопло', 'Петров')
            )


connection.commit()
connection.close()