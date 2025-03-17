def add_numbers(*args):
    for arg in args:
        print(f'arg: {arg}\n')
    # return sum(args)

print(add_numbers(1, 2, "hello", 4, 5)) # 15