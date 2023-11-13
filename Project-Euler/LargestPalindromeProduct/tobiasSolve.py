palindrome_list = []

for i in range(100**2, 999**2):
    front = []
    reverse = []
    for j in range(len(str(i))):
        front.append(str(i)[j-1])
        reverse.append(str(i)[-j])
    if front == reverse:
        for j in range(100, 999):
            if (i % j) == 0 and (i / j) > 100 and (i / j) < 999:
                print(f"{j} * {i/j} = {i}")