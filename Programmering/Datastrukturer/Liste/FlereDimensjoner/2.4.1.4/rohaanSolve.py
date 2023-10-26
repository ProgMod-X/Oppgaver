def null_fill_triangle(list, upper=True):
    columns = len(list[0])
    rows = len(list)
    newList = list

    if columns != rows:
        return []
    
    if upper:
        for y in range(0, rows):
            for x in range(y + 1, columns):
                newList[y][x] = 0
    else:
        for y in range(1, rows):
            for x in range(0, y):
                newList[y][x] = 0

    return newList

l = [
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1]
]

for row in l:
    print(row)

print("")

for row in null_fill_triangle(l):
    print(row)