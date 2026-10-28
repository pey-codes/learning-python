while True:
    try:
        number = int(input("Enter a number: "))
        print("Thanks!")
        break
    except ValueError:
        print("That's not a number!")