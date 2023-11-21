file = open(r"Programmering\Filbehandling\2.8.1\temperatur.csv", "r")
file.readline()

times = []
weatherList = []
temps = []

for line in file:
    values = line.split(",")
    times.append(values[0])
    
    weatherList.append(values[1].strip("\""))
    
    temps.append(values[2])
    
for i in times:
    print(f"{times[i]}\t{weatherlist[i]}\t{temps[i]}")

file.close()