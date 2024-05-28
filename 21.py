#  python program to find factorial using function
# Function name using recursion_function(n)
def recur_fact(n):
    if n == 1:
        return n
    else:
        return n*recur_fact(n-1)
num = int(input('\n Enter your factorial number :'))
# input for factorial
if num < 0:
    print("Sorry, factorial does not exist its negative numbers")
# checked if the number is negative then checked for 0 and positive
elif num == 0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of", num, "is", recur_fact(num))
