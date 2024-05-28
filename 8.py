# program to find whether a given number (accept from the user) is even or odd by using if else command

num = int(input("Enter a number to check for even and odd: ")) # taking input from user
rem = num % 2 # extracting the remainder of input number
if rem == 0:
     print(num,": Even Number")
else:
     print(num,": Odd Number")