# program to find whether the given string is palindrome or not by using function
#take input
def pal():
    wrd = str(input("Enter a word :"))
    if (wrd == wrd[::-1]):
        print(wrd, "is Palindrome")
    else:
        print(wrd, "is Not Palindrome")
#function to check whether the input word is a Palindrome or not

pal()