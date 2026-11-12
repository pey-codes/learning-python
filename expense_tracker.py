import sqlite3

connection = sqlite3.connect("expenses.db")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses(
        item TEXT,
        amount FLOAT,
        quantity INTEGER
    )
""")


connection.commit()
connection.close()