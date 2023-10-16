import csv

path = r'Simulering datahåndtering og visualisering\Filbehandling\3.1.1\temperatur.csv'

time, sky, temp = [], [], []

with open(path) as file:
    reader = csv.reader(file)
    for line in reader:
        if line[0] == 'klokkeslett':
            continue
        time.append(str(line[0]))
        sky.append(str(line[1]))
        temp.append(int(line[2]))