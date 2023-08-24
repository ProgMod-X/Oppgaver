def fahrenheit_to_celsius(fahrenheit):
    celsius = (5/9) * (fahrenheit - 32)
    return round(celsius, 1)

try:
    fahrenheit = float(input("Skriv inn temperatur i grader Fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit} grader Fahrenheit tilsvarer {celsius} grader Celsius.")
except ValueError:
    print("Ugyldig inntasting. Skriv inn en gyldig temperatur i grader Fahrenheit.")
