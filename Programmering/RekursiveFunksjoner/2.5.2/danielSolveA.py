def a(n):
    if n == 1:
        return 3
    else: 
        print(5 + a(n-1))
        return 5 + a(n-1)
      
print(a(5))
