def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(40))


"""
Days              : 0
Hours             : 0
Minutes           : 0
Seconds           : 25
Milliseconds      : 282
Ticks             : 252825879
TotalDays         : 0,000292622545138889
TotalHours        : 0,00702294108333333
TotalMinutes      : 0,421376465
TotalSeconds      : 25,2825879
TotalMilliseconds : 25282,5879
"""