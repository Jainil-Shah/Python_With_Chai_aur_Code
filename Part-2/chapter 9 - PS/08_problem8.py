with open ("chapter 9 - PS\\this.txt") as f:
    data = f.read()
    
with open ("chapter 9 - PS\\copy_of_this.txt", "w") as f:
    f.write(data)