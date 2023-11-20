file = open(r"Simulering datahåndtering og visualisering\Filbehandling\Datafiler\sang.txt", "r", encoding="utf8")

for line in file:
    words = line.strip("\n").split(" ")
    for word in words:
        print(word.strip(".,abcdefghijklmnopqrstuvwxyzJ"))
        

file.close()