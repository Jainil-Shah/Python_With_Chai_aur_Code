
def filter():
    with open ("chapter 9 - PS\\donky.txt", "r+") as f:
        data = f.read()
        modified_data = data.lower().replace("donkey", "######")
        f.seek(0)
        f.write(modified_data)
        f.truncate()

filter()