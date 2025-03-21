f = open("chapter 9\\file.txt", "r")

line = f.readlines()
print(line, type(line))

line = f.readline() 
print(line) # this will print nothing, because the cursor is at the end of the file

# Note : User f.seek(0) to reset the cursor to the beginning of the file

f.close