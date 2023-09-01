max = int(input("Pyramidetall: "))

pyramidnum = 0

for n in range(1, max+1):
    pyramidnum += (n**2)
    
print(f"Pyramidetall for n = {max} er {pyramidnum}")