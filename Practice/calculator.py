def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

while True:
    print("This is a calculator program. Please enter your numbers and select the operation.")
    num1 = float(input("Please input the first number: "))
    num2 = float(input("Please input the second number: "))
    operation = input("Please enter the operation (+, -, *, or /), or type 'stop' to quit: ")
    
    if operation == "+":
        print("{:.2f} + {:.2f} = {:.2f}".format(num1, num2, add(num1, num2)))
    elif operation == "-":
        print("{:.2f} - {:.2f} = {:.2f}".format(num1, num2, subtract(num1, num2)))
    elif operation == "*":
        print("{:.2f} * {:.2f} = {:.2f}".format(num1, num2, multiply(num1, num2)))
    elif operation == "/":
        print("{:.2f} / {:.2f} = {:.2f}".format(num1, num2, divide(num1, num2)))
    elif operation.lower() == "stop":
        break
    else:
        print("Invalid operation. Please enter a valid operation (+, -, *, or /).")

print("Exiting calculator program.")
