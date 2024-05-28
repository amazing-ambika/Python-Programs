#python program to copy content of a file to another file

#Input files for Read data
with open("input.txt" ,"r") as f:
    # Output file to copy content from input file
    with open("output.txt", "w") as f1:
#writes content from existing to new file
        for line in f:
            f1.write(line)
#display content of copying text
            print("Copy content text is : ",line)
#close files
f.close()
f1.close()