file = open(r"Simulering datahåndtering og visualisering\Filbehandling\Datafiler\heights.csv", "r", encoding="utf8")

file.readline()

names = []
sum_heights = 0
number_of_heights = 0

for line in file:
    l = (line.strip("\n")).split(",")
    names.append(l[0].strip("\""))
    sum_heights += float(l[1])
    number_of_heights += 1
    
avg_height = sum_heights/number_of_heights

print(avg_height)
print(names.strip)
file.close()