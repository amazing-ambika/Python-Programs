#  program using a flag to validate if the input given by the user is an integer.#Datatype check.

#Declare a variable validInt which is also considered as flag and set it to false
validInt = False
#Consider the while condition to be true and prompt the user to enter the input
while not validInt:
 #The user is prompted to enter the input
    age1 = input('Please enter your age ')
#The input entered by the user is checked to see if it’s a digit or a number
    if age1.isdigit():
 #The flag is set to true if the if condition is true
        validInt = True
    else:
        print('The input is not a valid number')
 #This statement is printed if the input entered by the user is a number
print('The entered input is a number and that is ' + str(age1))
