row = int(input("How many rows? "))

def pascal(row, place):
    if (row == place or place == 0):
        return 1
    else:
        return pascal(row - 1, place) + pascal(row - 1, place -1)
    
for i in range(row):
    print(" " * (row - i), end="")
    for j in range(i + 1):
        print(f"{pascal(i, j)} ", end="")
    print()