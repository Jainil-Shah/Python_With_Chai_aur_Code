words = ["donky", "bad", "worst", "negative"]

def filter():
    with open ("chapter 9 - PS\\badwords.txt", "r+") as f:
        data = f.read()
        data = data.lower()
        for word in words:
            data = data.replace(word, len(word) * "#")  
        f.seek(0)
        f.write(data)
        f.truncate()

filter()