# Generate a 2d list of 12*12 cells
tabell = [[0 for i in range(13)] for j in range(13)]

for i in range(13):
    for j in range(13):
        tabell[i][j] = i * j

print(tabell[3][5])