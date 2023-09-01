'''
- Lag en liste med navn person bestående av navnene på 5 personer du kjenner alderen til. Husk anførselstregn rundt tekst.

- Lag en liste med navn age bestående av alderen til de fem personene du la inn i sted. Pass på at rekkefølgen er den samme.

- Skriv ut følgende for alle personene ved hjelp av en løkke:
______ er __ år gammel.
'''

navn_list = ["Seth", "Ruth", "Tale","Harald", "Haakon"]

alder_list = ["17","13","19","86","50"]
for x in range(5):
    print(f"{navn_list[x]} er {alder_list[x]} år gammel.")


