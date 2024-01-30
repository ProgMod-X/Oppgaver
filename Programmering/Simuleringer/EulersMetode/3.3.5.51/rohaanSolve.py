import matplotlib.pyplot as plt

non_sick = 12000
sick = 100
days = 0
k = 1E-6

target_days = 10 * 7
target_sick = 4000

second_target_sick = 12000 / 2

while sick < target_sick:
    sick = 100
    non_sick = 12000
    days = 0
    while days < target_days:
        non_sick = non_sick - sick
        sick += k * non_sick
        days += 1
    print(days, sick, non_sick, k)

    k += 1E-6

while sick < second_target_sick:
    non_sick -= sick
    sick += k * non_sick
    days += 1

print(days, sick, non_sick)