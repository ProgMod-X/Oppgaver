def h(x):
    if x <= 1:
        return x**2 + 2 * x + 3
    else:
        return -x + 7

print("x\t|\ty\n")
for i in range(-4, 5):
    print(f"{i}\t|\th(x) = {h(i)}")