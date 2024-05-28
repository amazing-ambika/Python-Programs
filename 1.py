# sort (ascending and descending) a dictionary by value
import operator
dict = {0:0, 1: 2, 4: 5, 8: 9, 12: 13}
print('Original Dictionary : ',dict)
sorted_dict = sorted(dict.items(), key=operator.itemgetter(0))
print('Dictionary in ascending order by value : ',sorted_dict)
sorted_dict = sorted(dict.items(), key=operator.itemgetter(0),reverse=True)
print('Dictionary in descending order by value : ',sorted_dict)