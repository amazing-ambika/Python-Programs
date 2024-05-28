# program in python to create a list containing 5 integer values. Calculate the average of all the values and print the result.

list = [1, 2, 3, 4, 5]
print(list)
sum = 0
for i in list:
    sum += list[i-1]
avg = sum/len(list)
print(avg)

