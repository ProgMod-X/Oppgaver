evenlyDivisible = False
num = 20
longestDivisible = []

while evenlyDivisible == False:
    divisibleWith = []
    for i in range(1, 21):
        if num % i == 0:
            divisibleWith.append(i)
        else:
            break
    if len(divisibleWith) > len(longestDivisible):
        print(divisibleWith, num)
        longestDivisible = divisibleWith
    if len(divisibleWith) == 20:
        evenlyDivisible = True
    num += 20