def even_generator(limit):
    for i in range(2, limit+1, 2):
        yield i
        
for num in even_generator(10):
    print(num)

gen = even_generator(10)

print("-------------------")
print(next(gen))
print(next(gen))

