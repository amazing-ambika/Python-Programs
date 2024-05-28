# python program to find the frequency of words in a file

#import counter for read data
from collections import Counter
def word_count(fname):
#Open a file and read text
    with open(fname) as f:
#Separating a text word by word using split()
        return Counter(f.read().split())
print("Number of words in the file :",word_count("output.txt"))