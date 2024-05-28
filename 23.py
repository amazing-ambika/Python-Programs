#python class to reverse a string word by word

# Python program to Reverse each word of a string word by word

def reverse_wrd(input_word): # function definition
    wrd = userinput.split(" ")
    # Splitting the string into a list of words
    # reversing each word and creating a new list of words
    nw = [i[::-1] for i in wrd]
    # Joining the new list of words to form a new string
    ns = " ".join(nw)
    return ns

userinput = input("Enter the string: ")
print(reverse_wrd(userinput))