#gcd
def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

x = int(input("Enter First Number :"))
y = int(input("Enter Second Number :"))
print("GCD of ",x, " and ",y, " : ",gcd(x,y))

#way2
def gcd(x, y): # create function gcd()
    gcd = 1
    if x % y == 0:
        return y
    for k in range(int(y / 2), 0, -1): # for loop from y/2 to 0 increment -1
        if x % k == 0 and y % k == 0:
            gcd = k
            break
    return gcd
print(gcd(12, 17)) # print the gcd value
print(gcd(4, 6))
