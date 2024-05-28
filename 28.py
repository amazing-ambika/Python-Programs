# python program to illustrate exception handling

import sys
list = ['boy', 'cat', 0, 14.3]
for entry in list:

    try:
        print("the entry is:", entry)
        r = 1 / int(entry)
    except(ValueError):
        print("Hey a ValueError exception occured")
    except(ZeroDivisionError):
        print("Hey a ZeroDivisionError exception occured")
    except:
        print("some error occur")
print("the recipocal of the entry is ", r)
