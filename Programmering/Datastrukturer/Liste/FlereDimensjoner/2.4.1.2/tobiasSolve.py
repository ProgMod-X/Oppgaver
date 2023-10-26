cube = []
table = []
curlist = []

for i in range(0, 13):
    for j in range(0, 13):
        for k in range(0, 13):
            curlist.append(i*j*k)
        table.append(curlist)
        curlist = []
    cube.append(table)
    table = []
    
print(cube[3][5][3])