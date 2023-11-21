import random

file = open(r"Programmering\Filbehandling\Datafiler\tilfeldigTobias.csv", "w")

for i in range(100):
    x = round(random.random() * 320, 3)
    y = round(random.random() * 200, 3)
    
    line = str(x) + "," + str(y) + "\n"
    file.write(line)

file.close()