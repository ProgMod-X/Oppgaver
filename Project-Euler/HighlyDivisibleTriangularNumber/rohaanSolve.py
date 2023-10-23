def factors(num):
    for div in range(1, int(num**0.5) + 1):
        if num % div == 0:
            yield div
            other = num // div
            if other != div:
                yield other

def triangleNumber(n):
    return int((n*(n+1))/2)

for i in range(100000):
    facts = 0
    for value in factors(triangleNumber(i)):
        facts += 1
    if facts > 500:
        print(f"{i}\t{triangleNumber(i)}")
        break
    print(i)
