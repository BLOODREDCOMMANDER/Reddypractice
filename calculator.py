a = int(input("enter a number"));
operation = input("enter the operation you want to perform (+, -, *, /): ");
b = int(input("enter another number"));
if operation == "+":
    print(a+b);
elif operation == "-":
    print(a-b);
elif operation == "*":
    print(a*b);
elif operation == "/":
    if b != 0:
        print(a/b);
    else:
        print("Error: Division by zero is not allowed.");
#it's a calculator program
