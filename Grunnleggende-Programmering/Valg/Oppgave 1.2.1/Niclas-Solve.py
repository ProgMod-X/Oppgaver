Tall = int(input("Skriv inn tallet her: "))

if Tall > 0:
    print("Her er absoluttverdien", "|", Tall, "|") #hvis tallet er positivt går det her, grunnet a > 0, a = |a|
else:
    Tall = Tall - Tall - Tall #her blir de negative tallene gjort om til positive, grunnet (-2) - (-2) - (-2) = 2, kan og gange med -1
    print("Her er absoluttverdien", "|", Tall, "|")