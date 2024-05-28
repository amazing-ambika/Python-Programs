# program to create a histogram from a given list of integers by using for while loop

def histogram( items ): # create function
    for n in items: # for loop through values of n
        output = ''
        times = n
        while( times > 0 ): # check condition of counter
            output += '*'
            times -= 1 # decrement the counter
        print(output) # print the output
histogram([2, 3, 6, 5])