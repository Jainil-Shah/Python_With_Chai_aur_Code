with open ("chapter 9\\file.txt", "r") as f:
    data = f.read()
    print(data)
    
    
with open ("chapter 9\\file.txt", "a") as f:
    f.write("\nThis is a new line using with statement")