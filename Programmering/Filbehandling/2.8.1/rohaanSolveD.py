import csv
import matplotlib.pyplot as plt

path = r'Simulering datahåndtering og visualisering\Filbehandling\3.1.1\temperatur.csv'

time, sky, temp = [], [], []
skyetCounter = 0
delvisSkyetCounter = 0

with open(path) as file:
    reader = csv.reader(file)
    for line in reader:
        if line[0] == 'klokkeslett':
            continue
        time.append(str(line[0]))
        sky.append(str(line[1]))
        temp.append(int(line[2]))

for type in sky:
    if type == "skyet":
        skyetCounter += 1
    elif type == "delvis skyet":
        delvisSkyetCounter += 1
    # else:
    #     delvisSkyetCounter += 1

print(f"I dag skal det være {round(skyetCounter/len(sky), 2)}% skyet og {round(delvisSkyetCounter/len(sky), 2)}% delvis skyet")