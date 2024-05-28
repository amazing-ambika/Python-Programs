# Python Program for Bubble Sort

a = [] # # initialize the list
def bubblesort(a, number):
    for i in range(number -1):
        for j in range(number - i - 1):
            if(a[j] > a[j + 1]):
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp

number = int(input("Please Enter the Total Number of Elements : "))
for i in range(number):
    value = int(input("Please enter the %d Element of List1 : " %i))
    a.append(value) # append the value to the list
bubblesort(a, number)
print("The Sorted List in Ascending Order : ", a)
