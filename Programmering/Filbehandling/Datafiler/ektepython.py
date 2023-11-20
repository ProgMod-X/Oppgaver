file = open("sang.txt", "r", encoding="utf8")

for line in file:
    words = line.strip("\n").split(" ")
    for word in words:
        print(word.strip(".,"))
file.close()