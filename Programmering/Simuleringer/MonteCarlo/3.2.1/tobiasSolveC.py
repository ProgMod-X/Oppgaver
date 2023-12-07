table = [([i+j for i in range(1, 7)]) for j in range(1, 7)]

for num in range(1,13):
    sum = 0
    for list in table:
        for val in list:
            if val == num:
                sum += 1
    print(f"Value: {num:2.0f} | Probability: {round(sum/36, 3)}")