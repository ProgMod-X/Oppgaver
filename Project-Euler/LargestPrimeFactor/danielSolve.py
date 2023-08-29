from sympy import factorint

num = 600851475143
prime_factors = factorint(num)
largest_prime_factor = max(prime_factors.keys())

print(largest_prime_factor)

# ULOVLIG LØSNING OBS OBS!!!!

# IKKE LOV Å BRUKE BIBLIOTEK