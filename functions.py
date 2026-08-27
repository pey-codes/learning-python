def add(a, b):
    return a + b
answer = add(10, 65)
print(answer)

def subtract(a, b):
    return a - b
answer = subtract(10, 65)
print(answer)

def multiply(a, b):
    return a * b
answer = multiply(10, 65)
print(answer)

def divide(a, b):
    return a / b
answer = divide(10, 65)
print(answer)

num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
operation = input("Choose an operation(+, -, *, /):")

if operation == "+":
    answer = add(num1, num2)
elif operation == "-":
    answer = subtract(num1, num2)
elif operation == "*":
    answer = multiply(num1, num2)
elif operation == "/":
    answer = divide(num1, num2)
else:
    print("Invalid operation")

print(answer)
