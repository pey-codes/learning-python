# Learning Python

My Python learning journey, from the basics to building AI-powered apps.

## Projects 
- **Number guessing game**: guess a random number
- **Contact book**: add and search contacts, saved to a file (built with Python classes)
- **To-do list**: add, view, delete and clear tasks, saved to a file
- **Calculators**: simple interest, rectangle, triangle and temperature converters

## Expense Tracker (Python + SQLite)

A command-line program that records what I spend and shows the total.

### What it does
- Asks for an item, an amount and a quantity
- Checks the input, and asks again if the amount or quantity is not a valid number
- Saves each expense in a SQLite database (`expenses.db`)
- Prints every saved expense and the total spent

### How to run it
```bash
python expense_tracker.py
```
The database file is created automatically the first time the script runs. It is not uploaded to GitHub.

### What I learned
- Connecting Python to a database with the built-in `sqlite3` library
- Creating a table and inserting rows from Python using `?` placeholders
- Reading rows with `fetchall()` and adding them up with SQL `SUM`
- Why every table needs an `id` primary key: it gives each row a unique number, so I can change or delete exactly one row
- Handling bad input with `try/except`