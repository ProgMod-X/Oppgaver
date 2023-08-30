print("C:")
for i in range(1, 10):
    for j in range(10):
        for k in range(10):
            if i * j * k == i + j + k:
                print(i * 100 + j * 10 + k)