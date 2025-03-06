# majl = "matous.holinka@gmail.com"
# print(majl)
# rozdeleny_majl = majl.split("@")
# print(rozdeleny_majl)
# print(rozdeleny_majl[0])
# jmeno = rozdeleny_majl[0]
# jmeno_upravene = jmeno.replace(".", " ")
# print(jmeno_upravene)
# print(jmeno_upravene.title())
# jmena = ["matous", "lukas"]
# jmena.insert(0, "Petr")
# print(jmena)
# zaznam = "Ota; Petr; Pavel"
# seznam_jmen = zaznam.split("; ")
# print(seznam_jmen)
# seznam_jmen.insert(0, "Johnny")
# print(seznam_jmen)
# seznam_jmen.append("Jane")
# print(seznam_jmen, sep="\n")

# mesta = ["Praha", "Viden", "Olomouc", "Svitavy", "Zlin", "Ostrava"]

# ceny = (150, 200, 120, 120, 100, 180)

# slevy = ("Olomouc", "Svitavy", "Ostrava")

# domeny = ("gmail.com", "seznam.cz", "email.cz")

# dvojita_cara = "=" * 35
# cara = "-" * 35

# nabidka = """
# 1 - Praha   | 150
# 2 - Viden   | 200
# 3 - Olomouc | 120
# 4 - Svitavy | 120
# 5 - Zlin    | 100
# 6 - Ostrava | 180
# """

# AKT_ROK = 2021
# print("VITEJTE U NASI APLIKACE DESTINATIO!")
# print(dvojita_cara, end="")
# print(nabidka, end="")
# print(dvojita_cara)
# destinace_cislo = int(input("vyber cislo destinace: "))
# if 1 <= destinace_cislo <= 6:
#     destinace_nazev = mesta[destinace_cislo - 1]
#     print("Destinace: " + destinace_nazev.upper())
# else:
#     print("Destinace cislo", str(destinace_cislo) + " NEEXISTUJE!")
# if destinace_nazev in slevy:
#     nova_cena = 0.75 * ceny[destinace_cislo - 1]
#     print("Ziskavate 25% slevu! Nova cena: " + str(nova_cena) + ",-")
# else:
#     nova_cena = ceny[destinace_cislo - 1]
#     print("Jizdenka bez slevy. Cena: " + str(nova_cena) + ",-")

# print(cara)
# cele_jmeno = input("Vaše celé jméno: ")
# krestni_jmeno = cele_jmeno.split()[0]
# if krestni_jmeno.isalpha():
#     print("Krestni jmeno: ", krestni_jmeno)
# else:
#     print("Neplatne jmeno!")
# print(cara)
# rok_narozeni = int(input("Váš rok narození: "))
# if rok_narozeni < 2006:
#     print("Přistup povolen...")
# else:
#     print("Jste příliš mladý na nákup jízdenek!")
#     print("Ukončuji program")
    
# print(cara)
# email = input("Zapis vasi e-mailovou adresu: ")
# if "@" in email and email.split("@")[1] in domeny:
#     print("Overeni e-mailu probehlo v poradku.")
# else:
#     print("Tento email je neplatny")
#     print("Ukoncuji program")
#     quit()
# print(dvojita_cara)
print(
 "Matous",
 "Marek",
 "Lukas",
# volitelný (také nepovinný) argument "sep"
sep="\n" 
)

*pismena, = "abcd"
print(pismena)

*pismena, = "abcd",
print(pismena)

var = 1,
var_1 = 2
*zbytek, = var, var_1
print(zbytek)