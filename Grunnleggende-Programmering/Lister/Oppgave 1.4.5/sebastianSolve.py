'''
I et lotterispill trekkes det 5 hovedtall og 2 tilleggstall av totalt 42 tall. Får du 5 rette tall på én og samme rekke, vinner du førstepremiepotten.

Skriv et program som trekker totalt 7 ulike tall fra intervallet [1, 42]. De fem første skal i en liste hovedtall, og to siste i en liste tilleggstall. Listene skal til slutt sorteres før de skrives ut.

Du kan få bruk for: `if _value_ in _list_, .sort()`
''' 
import random as rd

hovedtall_list = []
tilleggstall_list = []

while len(hovedtall_list) < 5:
    x = rd.randint(1, 42)
    if x not in hovedtall_list:
        hovedtall_list.append(x)

while len(tilleggstall_list) < 2:
    x = rd.randint(1, 42)
    if x not in tilleggstall_list:
        tilleggstall_list.append(x)

hovedtall_list.sort()
tilleggstall_list.sort()

print("Hovedtall:",hovedtall_list,"Tilleggstall:", tilleggstall_list)