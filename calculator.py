# Python Calculator

operator = input(("Enter an operator (+ - * /): "))


first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

if operator == "+":
    result = first_number + second_number
    print(round(result))

elif operator == "-":
    result = first_number - second_number
    print(round(result))

elif operator == "*":
    result = first_number + second_number
    print(round(result))

elif operator == "/":
    result = first_number + second_number
    print(round(result))

else:
    print(f"{operator} is not a valid Operator")