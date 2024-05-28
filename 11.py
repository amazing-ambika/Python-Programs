#LCM of two positive integers using if else and while
def lcm(x, y):
# define function
    if x > y:
        z = x
    else:
        z = y
    while(True):
        if((z % x == 0) and (z % y == 0)):
# check if both conditions are true
            lcm = z
            break
        z += 1
    return lcm
print(lcm(4, 6))
# print the lcm value
print(lcm(15, 17))
