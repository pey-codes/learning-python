try:
    age = int(input("Enter you age: "))
    print("Next year you will be", age + 1)
except ValueError:
    print("That wasn't a number!")