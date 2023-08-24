def absoluttverdi(number):
    if number < 0:
        absolute_value = -number
    else:
        absolute_value = number
    return absolute_value

try:
    number = float(input("Skriv inn et tall: "))
    absolute_value = absoluttverdi(number)
    print(f"Absoluttverdien av {number} er {absolute_value}")
except ValueError:
    print("Ugyldig inntasting. Skriv inn et gyldig tall.")
