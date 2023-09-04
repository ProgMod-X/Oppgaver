import random

valg = ["stein", "saks", "papir"]


while True:
    try:
        user_choice = input("stein, saks, papir?\n")
        
        if user_choice not in valg:
            raise ValueError
        
        user_choice = valg.index(user_choice)
        system_choice = random.randint(0,2)

        if user_choice == system_choice:
            print("Uavgjort, begge valgte", valg[user_choice])
        elif (user_choice + 1)%3 == system_choice:
            print("System vant, du valgte", valg[user_choice], "system valgte", valg[system_choice])
        else:
            print("Du vant, du valgte", valg[user_choice], "system valgte", valg[system_choice])
        
        break

    except ValueError:
        print("Gyldige input er 'stein', 'saks', 'papir'")