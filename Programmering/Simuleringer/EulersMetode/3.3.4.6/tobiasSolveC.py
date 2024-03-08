def deltaY(k, y, w):
    return (k * y) + w

factor = -0.5
change = 10
inBody = 0

for i in range(1000):
    inBody += deltaY(factor, inBody, change)
    
print(f"Virkestoff rett etter daglig tablett: {inBody}")