def null_fill_triangle(table, upper):
    columns = len(table[0])
    rows = len(table)
    new_table = table
    
    if columns != rows:
        return []
    
    if upper:
        for row in range(0, rows-1):
            for column in range(row+1, columns):
                new_table[row][column] = 0
    else:
        for row in range(1, rows):
            for column in range(0, row):
                new_table[row][column] = 0
                
    return new_table

table = [[1,2,3,4,5],
         [1,2,3,4,5],
         [1,2,3,4,5],
         [1,2,3,4,5],
         [1,2,3,4,5],]

new_tab = null_fill_triangle(table, False)

for row in new_tab:
    print(row)