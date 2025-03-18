
def generateTable(n):
    with open(f"chapter 9 - PS\\Tables\\table-{n}.txt", "w") as f:
        for i in range(1, 11):
            f.write(f"{n} x {i} = {n*i}\n")
            
for i in range(2, 21):
    generateTable(i)
    
    