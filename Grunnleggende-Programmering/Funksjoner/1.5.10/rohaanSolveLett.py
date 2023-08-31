def multiplikasjon(multiplikand, multiplikator):
    sum = 0
    for i in range(multiplikand):
        sum += multiplikator
    return sum

print(multiplikasjon(5, 15))