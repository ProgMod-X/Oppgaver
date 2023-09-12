# Algoritme som beskriver måten hanne vil løse probleme på:

# Oppgir lengde på sidene i rektangelet
# Mens den minste sidelengden er større enn 0:
#     Sett kvadrat-sidelengde til minste rektangel-sidelengde
#     Mens minste rektangel-sidelengde er større enn kvadrat-sidelengde:
#         Subtraher kvadrat-sidelengde fra rektangel-maks-sidelengde
# print ut siste verdi av kvadrat-sidelengde



rec = [int(input("Lengde på rektangel: ")), int(input("Bredde på rektangel: "))]

sq = 0

while min(rec) > 0:
    sq = min(rec)
    while min(rec) >= sq:
        rec[rec.index(max(rec))] = max(rec) - sq

print(f"Maksimal sidelengde på kvadratene er {sq}")