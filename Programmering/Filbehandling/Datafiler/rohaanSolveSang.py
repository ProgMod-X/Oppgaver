path = r"Programmering\Filbehandling\Datafiler\sang.txt"

with open(path, encoding="utf8") as file:
    for line in file:
        print(line)