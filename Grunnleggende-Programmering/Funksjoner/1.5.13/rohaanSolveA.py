def congruent(a, b, modulus):
    if a % modulus == b % modulus:
        return True
    else:
        return False

print(congruent(27, 12, 5))