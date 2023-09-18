import random

n = int(input("Table size: "))

table = []
curlist = []

for i in range(n):
    for j in range(n):
        curlist.append(random.randint(-9, 9))
    table.append(curlist)
    curlist = []
    
pos = 0

for i in range(n):
    if table[i][i] > 0:
        pos += 1
        
print(f"Positives on the diagonal: {pos}")