import matplotlib.pyplot as plt

file = open(r"Programmering\Filbehandling\2.8.1\temperatur.csv", "r")
file.readline()

times = []
weatherList = []
temps = []

for line in file:
    values = line.split(",")
    times.append(values[0])
    
    weatherList.append(values[1].strip("\""))
    
    temps.append(int(values[2]))

file.close()

for index in range(len(times)):
    if temps[index] < 0:
        plt.plot(times[index], temps[index], "o", color="blue")
    else:
        plt.plot(times[index], temps[index], "o", color="red")
        
dsCounter = 0
sCounter = 0
for index in range(len(times)):
    if weatherList[index] == "delvis skyet":
        dsCounter += 1
    elif weatherList[index] == "skyet":
        sCounter += 1
        
print(f"Prosent skyet: {sCounter/(sCounter+dsCounter)*100}%\tProsent delvis skyet: {dsCounter/(sCounter+dsCounter)*100}%")
    

plt.plot(times, temps, "--", color="black", label="Temperatur")
plt.grid()
plt.xlabel("Tid [timer]")
plt.ylabel("Temperatur [*C]")
plt.legend()
plt.show()