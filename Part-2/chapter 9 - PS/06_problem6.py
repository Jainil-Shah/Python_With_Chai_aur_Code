
with open ("chapter 9 - PS\\python.txt", "r") as f:
    data = f.read()
    data = data.lower()
    if "python" in data:
        print("python is present")
    else:
        print("python is not present")