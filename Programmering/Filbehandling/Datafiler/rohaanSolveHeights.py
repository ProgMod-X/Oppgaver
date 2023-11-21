import csv

path = r"Programmering\Filbehandling\Datafiler\heights.csv"

totalHeight = 0
totalHumans = 0

with open(path) as file:
    reader = csv.reader(file)
    for line in reader:
        if line[0] == "name":
            continue
        totalHeight += int(line[1])
        totalHumans += 1
    print(totalHeight/totalHumans)