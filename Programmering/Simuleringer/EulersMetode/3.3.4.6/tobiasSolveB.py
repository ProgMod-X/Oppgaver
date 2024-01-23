def deltaY(k, y, w):
    return (k * y) + w

factor = -0.25
change = 20
inBody = 0

while inBody > 60:
    inBody = 0
    change -= 0.01
    for i in range(1000):
        inBody += deltaY(factor, inBody, change)

    
print(f"Hun må ta tabletter på {}")