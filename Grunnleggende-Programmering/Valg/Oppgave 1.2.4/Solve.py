import random

valg = ["stein", "saks", "papir"]

while True:
    try:
        user_choice = input("stein, saks, papir?\n")
        
        if user_choice not in valg:
            raise ValueError
        
        user_choice = valg.index(user_choice)
        system_choice = random.randint(0,2)
        determinator = (user_choice - system_choice) % 3

        if determinator == 0:
            print("Uavgjort, begge valgte", valg[user_choice])
        elif determinator == 1:
            print("System vant, du valgte", valg[user_choice], "system valgte", valg[system_choice])
        elif determinator == 2:
            print("Du vant, du valgte", valg[user_choice], "system valgte", valg[system_choice])
        elif determinator == -1:
            print("Du vant, du valgte", valg[user_choice], "system valgte", valg[system_choice])
        elif determinator == -2:
            print("System vant, du valgte", valg[user_choice], "system valgte", valg[system_choice])
        
        break

    except ValueError:
        print("Gyldige input er 'stein', 'saks', 'sapir'")