def a(n):
    if n == 1:
        return 1/2
    else:
        return a(n - 1) * 1/2