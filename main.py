#1. feladat:
filepath = "valaszok.txt"
fileobject = open(filepath, "r")

#2. feladat:
count_rows = 0
for line in fileobject:
    count_rows += 1
print("A sorok száma: ", count_rows-1)

#3. feladat:
jo_mego = fileobject.readline()
versenyzo_valasz = []
input_versenyzo = input("Kérem adja meg a versenyző azonítóját: ")
valasz = ""
for i in range(count_rows):
    if(versenyzo_valasz[i][0:5] == input_versenyzo):
        valasz=versenyzo_valasz[i][6:20]
        print(valasz)
    else:
        print("Ilyen kóddal nem indult versenyző.")


#4. feladat:
print("A helyes megoldás: ")
print(jo_mego)
jo_valasz = ""
for i in range(14):
    if(valasz[i] == jo_mego[i]):
        jo_valasz = jo_valasz + '+'
    else:
        jo_valasz = jo_valasz + ' '
print(jo_valasz)

#5.feladat
sorszam_input = input("Kérem adja meg a feladat sorszámát: ")
try:
    jo_db = 0
    sorszam = int(sorszam_input)
    sorszam_i = sorszam - 1
    for i in range(count_rows):
            if(jo_mego[sorszam_i] == versenyzo_valasz[i][sorszam_i+6]):
                jo_db += 1
    jo_szazalek = (jo_db / count_rows) * 100
    print("A válaszra fő, a versenyzők %-a adott helyes választ.", jo_db, jo_szazalek)

except ValueError:
    print("Hibás sorszám")



print("A versenyzők pontszámának a meghatározása.")
pontszamok = []
#for i in range(count_rows):
 #   pontszamok.append(0)

