def pascal(row, place):
    
    if place == 0 or place == row:
        return 1
    else:
        return (pascal(row - 1, place - 1) + pascal(row - 1, place))
    
    
rows = int(input("Rows: "))
    
for i in range(rows):
    print(" " * (rows - i), end="")
    for j in range(i + 1):
        print(f"{pascal(i, j)} ", end="")
    print()