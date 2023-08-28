sum = 0
iteration = 0
term = 0

for i in range(3, 6, 2):
    term = 0
    iteration = 0
    while term < 1000:
        term = i * iteration
        if term >= 1000:
            continue
        # print(f"{i}\t{iteration}\t{term}")
        sum += term
        iteration += 1

print(sum)