import random

wheel = [5, 10, "slutt"]
N = 10000000
sum_of_rewards = 0

for i in range(N):
    stop = False
    while not stop:
        choice = random.choice(wheel)
        if choice == "slutt":
            stop = True
            continue
        else:
            sum_of_rewards += choice

print(f"Gjennosnitlig størrelse på gevinst er {round(sum_of_rewards/N)}")