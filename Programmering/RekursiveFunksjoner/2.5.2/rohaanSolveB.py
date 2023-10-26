def a(n):
    if n == 1:
        return 3
    else:
        return a(n - 1) + 5

i = 1

while a(i) < 503:
    i += 1

print(f"{i}\t{a(i)}")