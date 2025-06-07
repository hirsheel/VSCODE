#this is my 1st PROGRAM
num1 = input("Enter Your First Number: ")
num2 = input("Enter Your Second Number: ")

# Check if both inputs are digits (basic way to check valid numbers)
if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)
    op = input("Enter Your Operation (+, -, /, *, **[1st raised to power of 2nd]): ")

    if op == "+":  #performs the operation here
        print("Result:", num1 + num2)
    elif op == "-":
        print("Result:", num1 - num2)
    elif op == "/":
        if num2 == 0:
            print("Cannot divide by zero, bruh!")
        else:
            print("Result:", num1 / num2)
    elif op == "*":
        print("Result:", num1 * num2)
    elif op == "**":
        print("Result:", num1**num2)
    else:
        print("Please enter a valid operation, bruh!")
else:
    print("Give a valid number, bruh!!")
