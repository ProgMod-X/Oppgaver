import matplotlib.pyplot as plt

def f(kropp, substanceAmount):
    return kropp * 0.75 + substanceAmount

kroppMax = 60
kropp = 61
substanceAmount = 20

while kropp > kroppMax:
    kropp = 0
    for i in range(40):
        kropp = f(kropp, substanceAmount)
    substanceAmount -= 0.0001

print(f"Marit kan ha tabletter med maks {round(substanceAmount, 3)} mg virkestoff i seg.")