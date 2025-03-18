with open ("chapter 9 - PS\\log.txt", "r") as f:
    lines = f.readlines()
    
lineno = 1

for line in lines:
    if "python" in line.lower():
        print(f"Yes python is present. Line no: {lineno}")
    lineno += 1