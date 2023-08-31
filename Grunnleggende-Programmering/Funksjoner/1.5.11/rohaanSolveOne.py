def factorial(n):
    sum = 1
    for i in range(1, n + 1):
        sum *= i
    return sum


def binomialkoeffisienten(n, k):
    a = []
    b = []
    for i in range(n, 0, -1):
        a.append(i)
    
    for i in range(k, 0, -1):
        b.append(i)
    
    if len(a) > len(b):
        a = a[:len(b)]
    elif len(a) < len(b):
        b = b[:len(a)]

    # print(f"{a}\n{b}")

    c, d = 1, 1

    for i in range(len(a)):
        c *= a[i]
        d *= b[i]
    
    return c/d

print(binomialkoeffisienten(15, 5))