population = 20000


for i in range(3):
    population -= population*0.1
    
print(f"Antall rotter etter 3 år er {population}")

population = 20000
counter = 0
while population > 10000:
    population -= population * 0.1
    counter += 1
    
print(f"Det tar {counter} år før antall rotter er halvert, da er det {round(population)} rotter igjen")