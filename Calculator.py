##Calculator
##by raul_andres
##12.31.2015



num1 = float(input("num1: "))
num2 = float(input("num2: "))
x = 0

op = input("Select the operator (+, -, x, /) : ")

while op != '+' and op != '-' and op != 'x' and op != '/' :
    print("This is NOT a valid entry")
    x = x + 1
    op = input("Select the operator (+, -, x, /) : ")

if op == '+':
    result = num1 + num2
    print(result)

elif op == '-':
    result = num1 - num2
    print(result)

elif op == 'x':
    result = num1 * num2
    print(result)

elif op == '/':
    result = num1 / num2
    print(result)
