import time

evenlyDivisible = False
num = 20
longestDivisible = []

start = time.time()

while evenlyDivisible == False:
    divisibleWith = []
    for i in range(1, 20):
        if num % i == 0:
            divisibleWith.append(i)
        else:
            break
    if len(divisibleWith) > len(longestDivisible):
        print(divisibleWith, num)
        longestDivisible = divisibleWith
    if len(divisibleWith) == 19:
        evenlyDivisible = True
    num += 20
    
end = time.time()

print(end-start)