stor = []

lille = []

a = 0
for i in range(12):
    for x in range(12):
        lille.append(x * a)
    a += 1   
    stor.append([lille])



print(lille)
