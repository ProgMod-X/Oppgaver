checks = 0
for i in range(1, 250000000):
    for j in range(1, 21):
        if i/j == int(i/j):
            # print(f"{i}\t{j}")
            checks += 1
    if checks == 20:
        print("success", i)
        break
    else:
        checks = 0