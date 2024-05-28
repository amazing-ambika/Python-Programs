# python program to add, subtract, multiply and divide given two numbers by using arithmetic operators.
choice = int(input("Enter Your Choice - 1 For Addition, 2 For Subtraction, 3 For Multiplication, 4 For Division : "))
if (choice != 1 and choice != 2 and choice != 3 and choice != 4):
    print("Invalid Input")
    exit()
else:
    num1 = int(input("Enter First Number "))
    num2 = int(input("Enter Second Number "))
if choice == 1: # perform addition if 1
    res = num1 + num2
    print("Result = ", res)
elif choice == 2: # perform subtraction if 2
    res = num1 - num2
    print("Result = ", res)
elif choice == 3: # perform multiplication if 3
    res = num1 * num2
    print("Result = ", res)
elif choice == 4: # perform division if 4
    res = num1 / num2
    print("Result = ", res)
else:
    exit() # exit if invalid input