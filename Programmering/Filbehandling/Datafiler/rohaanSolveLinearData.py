import csv

path = r"Programmering\Filbehandling\Datafiler\linear_data.csv"

with open(path) as file:
    reader = csv.reader(file)
    for line in reader:
        print(line)