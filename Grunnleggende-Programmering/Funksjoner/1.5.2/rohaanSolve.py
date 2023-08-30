def f(x0, x1):
    return x0 * x1

for i in range(10):
    print(f"{i}\t{i**2}\t{f(i, i**2)}")