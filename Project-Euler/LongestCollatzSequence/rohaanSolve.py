mem = {1: 1}

count = 0
longest = (0, 0)

def f(n):
    global count

    if n in mem:
        count += mem[n]
        return
    elif n % 2 == 0:
        count += 1
        a = f(n / 2)
        return a
    else:
        count += 1
        a = f(3 * n + 1)
        return a

for i in range(1, 1000000):
    count = 0
    f(i)
    if count > longest[1]:
        longest = (i, count)
        mem[i] = count
    print(f"{i}\t{count}\t{longest[0]}\t{longest[1]}\t{len(mem)}")