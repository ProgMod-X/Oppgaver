mem = {1: 1}

count = 0
longest = (0, 0)

def f(n):
    global count
    count += 1

    if n in mem:
        return mem[n]
    elif n % 2 == 0:
        a = f(n / 2)
        mem[n] = a
        return a
    else:
        a = f(3 * n + 1)
        mem[n] = a
        return a
    
for i in range(1, 1000000):
    count = 0
    f(i)
    if count > longest[1]:
        longest = (i, count)
    print(f"{i}\t{longest[0]}\t{longest[1]}")