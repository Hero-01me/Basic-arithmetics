#Python Basic Arithmetic Operations between two variables (x and y) using (+ - * /) operators

operator = input("Enter an operator (+ - * /): ")

valid_operator = ["+", "-", "*", "/"]

x = float(input("Enter the first number:" ))
y = float(input("Enter the second number:" ))

if operator == "+":
    result = x + y
    print(round(result, 4))
elif operator == "-":
    result = x - y
    print(round(result, 4))
elif operator == "*":
    result = x * y
    print(round(result, 4))
elif operator == "/":
    result = x / y
    print(round(result, 4))
elif operator not in valid_operator:
    print(f"{operator} is not valid operator!")

    exit()
