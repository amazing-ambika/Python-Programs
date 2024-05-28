#program to find Fibonacci Series
terms = int(input("Enter number of terms : "))
n1 = 0
n2 = 1
count = 0
if terms <= 0:
    print("Please enter a positive number")
elif terms == 1:
    print("Fibonacci sequence upto",terms,":")
    print(n1)
else:
    print("Fibonacci sequence upto",terms,":")
    while count < terms:
        print(n1,end='\n')
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
