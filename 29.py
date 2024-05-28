# python code to read a text file, copy the contents to another file after removing the blank lines.

fh = open('Blank.txt','r')
h = open('BlankRemove.txt','w')
b = fh.readlines()
print('The file contents before removing the blank spaces is :\n')
for line in b :
    print(line,end = '')
for line in b :
    if(len(line)>0) :
        line = line.lstrip()
        h.write(line)
fh.close()
h.close()
h = open('BlankRemove.txt','r')
y = h.read()
print('\n\nThe file contents after removing the blank spaces is :\n')
print(y)
h.close()