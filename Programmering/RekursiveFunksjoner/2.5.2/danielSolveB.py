def a(n):
    if n == 1:
        return 3
    else: 
        return 5 + a(n-1)

i = 1
while a(i) < 503:
    i = i+1

print(i)
