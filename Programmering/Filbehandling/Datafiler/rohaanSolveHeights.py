import csv

path = r"Programmering\Filbehandling\Datafiler\heights.csv"

with open(path) as file:
    reader = csv.reader(file)
    for line in reader:
        print(line)