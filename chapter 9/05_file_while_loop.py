
f = open("chapter 9\\file.txt", "r")

line = f.readline()
while line != "":
    print(line)
    line = f.readline()

f.close