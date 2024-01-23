def deltaY(k, y, w):
    return (k * y) + w

factor = -0.25
change = 20
inBody = 80

while inBody > 60:
    inBody = 0
    change -= 0.0001
    for i in range(100):
        inBody += deltaY(factor, inBody, change)

    
print(f"Hun må ta tabletter på litt mindre enn {round(change)} mg for å ikke få for mye i seg")