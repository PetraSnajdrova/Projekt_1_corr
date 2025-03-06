'''print("Ahoj")
zamestnanci = [
    'František', 'Bruno',
    'Anna', 'Jakub',
    'Klára', 'Anežka',
    'Anežka', 'Anežka'
]
posledni_index = len(zamestnanci) -1
print("Na indexu 2 je: ", zamestnanci[2])
print("Na",posledni_index, "indexu je: ", zamestnanci[-1])
print("V intervalu od 2 do 5 je:", zamestnanci[2:6])
print("Každý třetí člen je:", zamestnanci[ : : 3])
jmeno = "Martin"
vaha = 80
vyska = 2
bmi = vaha / vyska **2
if bmi > 40:
    kategorie = "Těžká obezita"
elif bmi > 30:
    kategorie = "Obezita"
elif bmi > 25:
    kategorie = "Mírná nadváha"
elif bmi > 18.5:
    kategorie = "Zdravá váha"
else:
    kategorie = "podvýživa"
print(jmeno, "tvé BMI je ", bmi, ", což spadá do kategorie ",kategorie)
zamestnanci_1 = ["František", "Anna", "Jakub", "Klára"]
print("Zamestananci na zacatku:", zamestnanci_1)
zamestnanci_a = zamestnanci_1.copy()
zamestnanci_a.append("Bruno")
zamestnanci_a.append("Anežka")
print("Nová jména přidána:", zamestnanci_a)
zamestnanci_b = zamestnanci_1.copy()
zamestnanci_b.insert(1, "Bruno")
print("Nová jména vložena:", zamestnanci_b)
vstupni_cisla = [1, 2, 3, 4, 5, 6, 7]
vstupni_pismena = ["p", "ú", "s", "č", "p", "s", "n"]
tyden = ('pondělí', 'úterý', 'středa', 'čtvrtek', 'pátek', 'sobota', 'neděle')
cislo_dne = 9
if cislo_dne in vstupni_cisla:
    print("Správná vstupní hodnota")
    den_tydne = tyden[cislo_dne -1]
    if den_tydne.startswith(vstupni_pismena[cislo_dne -1]):
        print("správné písmeno")
    else:
        print("špatné písmeno")
else:
    print("Špatná vstupní hodnota")
treti_slovnik = {"jmeno": "Marek", "vek": 20}
print(treti_slovnik)
print(treti_slovnik["jmeno"])
muj_slovnik = {}
muj_slovnik["jmeno"] = "Matous"
print(muj_slovnik)
muj_slovnik["jmeno"] = "Lukas"
print(muj_slovnik)
muj_slovnik_1 = {}
kontakty = {"mobil": 1234, "email": "hu@hu.hu"}
muj_slovnik_1 ["kontakt"] = kontakty
print(muj_slovnik_1)
print(muj_slovnik_1["kontakt"])
print(muj_slovnik_1["kontakt"]["email"])
print(muj_slovnik_1.items())
print(muj_slovnik.get("jmeno"))
print(muj_slovnik.get("adresa", "Klič neexistuje"))
print(muj_slovnik.get("adresa"))
set_a = {"zena", "ruze", "kost"}
set_a.add("pisen")
set_a.update(("Matous", "Lucie"))
print(set_a)
fr_set_a = frozenset({"zena", "ruze", "kost", "pisen", "Lucie", "Matous"})
fr_set_b = frozenset({"zena", "ruze", "kost", "pisen", "Lukas"})
print(fr_set_a.isdisjoint(fr_set_b))
user_1 = {}
user_1 ["name"] = "Marek"
user_1 ["surname"] = "Parek"
user_mail = {"email": "marek.parek@gmail.com"}
user_1.update(user_mail)
print("User #01", user_1)
jmeno = 'Marek'
heslo = '1234'
uzivatel = {'Marek': '1234'}
if uzivatel.get(jmeno) == heslo:
    print("Ahoj Marek vítej v aplikaci! Pokračuj...")
else:
    print("Uživatelské jméno nebo heslo nejsou v pořádku")
cisla_1 = (1, 1, 2, 3, 4)
cisla_2 = (5, 6, 7, 7, 8)
sjednocene_hodnoty = set(cisla_1) | set(cisla_2)
print("sjednocené hodnoty ze zadání", sjednocene_hodnoty)
cisla_3 = {1, 2, 3, 4}
cisla_4 = {3, 4, 5, 6}
rozdil_cisel = cisla_3.difference(cisla_4)
print("Rozdílné hodnoty první hosetu oproti druhému:", rozdil_cisel)'''


#CVIČENÍ PO PÁTÉ LEKCI

#slova = set()
#while len(slova) != 3:
#    slovo = input ("zadej slovo ze čtyř písmen: ".upper())
#    if slovo in slova:
#        print(f"Slovo {slovo} už je uložené")
#    elif len(slovo) == 4:
#        slova.add(slovo)
#    else:
#        print("Slovo nemá 4 znaky")
#else:
#    print("Už mám uložena 3 slova")

#ovoce = {"jablko", "banan", "citron", "pomeranc"}
#print("Dostupné ovoce:", ", ".join(ovoce))

#while True:
#    vyber = input("Vyber z dostupného ovoce: ".upper())
#    if vyber not in ovoce:
#        print("Ovoce není v nabídce")
#    else:
#        print("Bazva, toto ovoce je v nabídce")
#        break


# Zapiš nekonečnou smyčku pomocí proměnné `mod`
while True:

    # Zapiš výběr operace, kterou kalkulačka disponuje
    operation = input('''
Sčítání:    "+",
Odčítání:   "-",
----------------------
Vyber si operaci: '''
                )

    # Ověř zda uživatel zvolil platný operátor
    if operation not in ('+','-'):
        print('Nezadali jste platný operátor, zkuste to znovu.')
        continue

    # Získej čísla pro výpočet od uživatele
    number_1 = int(input('Zadej první číslo: '))
    number_2 = int(input('Zadej druhé číslo: '))

    # Dle operátoru proveď výpočet a vypiš ho
    if operation == '+':
        print(f'{number_1} + {number_2} = {number_1 + 
number_2}')
    elif operation == '-':
        print(f'{number_1} - {number_2} = {number_1 - number_2}')

    # Ověř zda chce uživatel pokračovat nebo chce program ukončit
    again = input('Chcete provést další operaci?(a pro ano, jakákoliv jiná klávesa pro ne): ')

    if again == 'a':
        continue
    else:
        print('Ukončuji...')
        break

pismena = ["a", "a", "b", "c", "d", "a", "e", "g", "m"]
while pismena:
    print(", ".join(pismena))
    
    zadani = input("ktere písmeno chceš vyhodit?")
    
    if zadani not in pismena:
        print(zadani + " není součástí písmen!")
    else:
        pismena.remove(zadani)

else:
    print("Konec hry!")