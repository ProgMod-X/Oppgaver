def potens(a ,b):
    try:
        if type(b) != int or b < 0:
            raise ValueError

        sum = a
        if b == 0:
            return 1
        else:
            for i in range(b - 1):
                sum *= a
            return sum
    except ValueError:
        print("Variabelen b er et ugyldig tall. Gyldige tall er alle positive heltall inkl. 0.")

print(potens(3, 0))