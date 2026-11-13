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

item = input("Item: ")
while True:
    try:
        amount = float(input("Amount: "))
        break
    except ValueError:
        print("Please enter a number.")
while True:     
    try:   
        quantity = int(input("Quantity: "))
        break
    except ValueError:
        print("Please enter a number.")

cursor.execute(
    "INSERT INTO expenses(item, amount, quantity) VALUES (?, ?, ?)",
    (item, amount, quantity)
)

cursor.execute("SELECT * FROM expenses")
rows = cursor.fetchall()
for row in rows:
    print(row[0], ":", row[1], "*", row[2])


connection.commit()
connection.close()