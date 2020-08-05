import sys 

def add (x, y): #addition
    return x + y
def subtract (x, y): #subtraction
    return x - y 
def multiply (x, y): #multiplication
    return x * y
def divide (x, y): #division
    return x / y

print("What operation would you like to use?")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Pick (1/2/3/4) ")

num1 = float(input("What's your first number? "))
num2 = float(input("What's your second number? "))

if choice == '1':
    print(num1, '+', num2, '=', add(num1, num2))
elif choice == '2':
    print(num1, '-', num2, '=', subtract(num1, num2))
elif choice == '3':
    print(num1, '*', num2, '=', multiply(num1, num2))
elif choice == '4':
    print(num1, '/', num2, '=', divide(num1, num2)) 
elif choice != '1' or '2' or '3' or '4':
    print("You did not pick a valid operation. Exiting.")
    sys.exit(0)
