score = 0

answer = input("What's the plural of dog? ").lower()

if answer == "dogs":
    score = score + 1

answer = input("What's the capital city of Kenya? ").lower()

if answer == "nairobi":
    score = score + 1

answer = input("How many main points does a compass direction have? ")

if answer == "4":
    score = score + 1

print("Your score:", score, "out of 3")



