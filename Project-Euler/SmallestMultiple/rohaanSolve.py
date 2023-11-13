checks = 0
for i in range(20, 250000000, 20):
    for j in range(1, 20):
        if i % j == 0:
            checks += 1
    if checks == 19:
        print("success", i)
        break
    else:
        checks = 0