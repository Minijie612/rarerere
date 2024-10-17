def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def devide(x, y):
    if == 0:
        return "Error division by zero."
    return x / y

def calculator():
    print("select operation:")
    print("1.add")
    print("2.subtract")
    print("3.multiply")
    print("4.devide")

while True:
    choice = input("Enter choice (1/2/3/4): ")
    
    if choice in ('1','2','3','4'):
        try:
            num1 = float(input("enter first number: "))
            num2 = float(input("enter second number: "))
        axcept ValueError
            print("invalid input! please enter numeric values.")
            cotinue

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        
        elif choice == '2'
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        
        
        elif choice == '3':
            print(f"{num1} * {num3} = {multiply(num1, num2)}")

       elif choice == '4':
            print(f"{num1} / {num3} = {devide(num1, num2)}")

        next_calculation = input("Do you want to perform a calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break

    else:
        print("invalid input")

if_name_ == "_main_":
    calculator()



