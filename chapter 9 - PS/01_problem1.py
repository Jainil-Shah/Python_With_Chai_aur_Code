with open ("chapter 9 - PS\\poem.txt", "r") as f:
    data = f.read()
    if "twinkle" in data.lower():
        print("twinkle is present")
    else:
        print("twinkle is not present")