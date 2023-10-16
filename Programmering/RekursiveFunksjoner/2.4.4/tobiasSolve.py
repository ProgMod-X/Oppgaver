def pascal(row, place):
    
    if place == 0 or place == row:
        return 1
    else:
        return (pascal(row - 1, place - 1) + pascal(row - 1, place))
    
    
triangle = []
rows = int(input("Rows: "))

for row in range(rows):
    new_row = []
    for n in range(row+1):
        new_row.append(pascal(row, n))
    triangle.append(new_row)
    
for row in triangle:
    print(row)