import sqlite3

connection = sqlite3.connect("expenses.db")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses(
        id INTEGER PRIMARY KEY,
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
        print("Please enter a whole number.")

cursor.execute(
    "INSERT INTO expenses(item, amount, quantity) VALUES (?, ?, ?)",
    (item, amount, quantity)
)

cursor.execute("SELECT * FROM expenses")
rows = cursor.fetchall()
for row in rows:
    print(row[0], ":", row[1], row[2], "*", row[3])

cursor.execute("SELECT SUM(amount * quantity) FROM expenses")
total = cursor.fetchone()[0]
print("Total spent:", total)


connection.commit()
connection.close()