file = open("notes.txt", "r")
content = file.read()
print(content)
file.close()

with open("notes.txt", "r") as file:
    content = file.read() 
print(content)

with open("notes.txt", "r")as file: 
    for line in file:
        print(line)
