for cislo in [1, 2, 3, 4, 5]:
    print(cislo)
for pismeno in ["a", "b", "c", "d"]:
    print(pismeno)
suda_cisla = list()
for cislo in (1, 2, 3, 4, 5):
    if cislo % 2 == 0:
        suda_cisla.append(cislo)
print(suda_cisla)
for cislo in (1, 2, 3, 4, 5):
    if cislo % 2 == 0:
        print("Sudé číslo")
    elif cislo % 2 != 0:
        print("Liché číslo")
for pismeno in ("a", "b", "c", "d"):
    if pismeno == "c":
        print("Nasel jsem 'c', preskakuji cyklus..")
        break
    print(pismeno)
for pismeno in ("a", "b", "c", "d"):
    if pismeno in {"a", "b"}:
        continue
    print("Hodnota", pismeno, "je dulezita")
for pismeno in ("a", "b", "c", "d"):
    if pismeno == "c":
        print("Nasel jsem 'c', preskakuji cyklus..")
        break
else:
    # kvůli 'break' se tento text nevypíše po ukončení smyčky
    print("Vsechna pismena vypsana")

print("Pokracuji po smycce")
print(
    tuple(range(11)), 
    tuple(range(1, 11)),
    tuple(range(1, 11, 3)),
sep="\n")
age = 36
txt = f"My name is John, I am {age}"
print(txt)
print(
    tuple(range(11)), 
    tuple(range(1, 11)),
    tuple(range(1, 11, 3)))
jmeena = ("Java", "C", "Rust", "Python")
print(enumerate(jmeena))
pismena = list()
for pismeno in "Matous":
    pismena.append(pismeno)
print(pismena)
# klasický zápis smyčky
pismena = list()
for pismeno in "Matous":
    pismena.append(pismeno)
else:
    print(f"Klasický zápis: {pismena}")
# list comprehension
nova_pismena = [pismeno for pismeno in "Matous"]
print(f"List comprehension: {nova_pismena}")
nova_pismena = [pismeno.upper() for pismeno in "Matous"]
print(nova_pismena)
veta = "Zvuk řeči je produkován poměrně otevřenou konfigurací vokálního traktu"
samohlasky = "aeiouáéíóú"
souhlasky = 'bcčdďfghjklmnňprřsštťvzžcdž'
vysledek = {"souhlasky": 0, "samohlasky": 0}
for pismeno in veta:
    if not pismeno.isalpha():
        continue
    elif pismeno.lower() in souhlasky:
        vysledek["souhlasky"] += 1
    elif pismeno.lower() in samohlasky:
        vysledek['samohlasky'] += 1
print('Počet souhlásek:', vysledek['souhlasky'], '| Počet samohlásek:', vysledek['samohlasky'])
cisla_xy = [1, 2, 3, 4, 5, 6, 7, 8]
suda = 0
licha = 0
for cislo in cisla_xy:
    if cislo %2 == 0:
        suda = suda + cislo
    else :
        licha = licha + cislo
vysledek_1 = abs(suda - licha)
print("rozdíl je: ", vysledek_1)
vysledek_xy = list()
start = 3
stop = 9
delitel = 3
vysledek = []
if isinstance(start, int) \
        and isinstance(stop, int) \
        and isinstance(delitel, int):
    print("Zadaný rozsah: <", start, ", ", stop, ">", sep="")

    # Iteruj skrze rozsah zadaných čísel
    for number in range(start, stop + 1):
        # .. pokud je vybrané číslo dělitelné hodnotou v prom. "delitel"
        if number % int(delitel) == 0:
            # .. přidej jej do seznamu "vysledek"
            vysledek.append(number)
    # doplň výpis hodnot v proměnné 'vysledek'
    print('Čísla dělitelná', delitel, ':', vysledek)

else:
    print("Zadané vstupy musí být čísla.")
seznam_slov = ["jablko", "pomeranč", "banán", "kiwi", "hruška"]
delka_slov = {slovo: len(slovo) for slovo in seznam_slov}
print(delka_slov)
oddelovac = "=" * 62

sluzby = ("dostupne filmy", "detaily filmu", 'reziseri', "doporuc film")

uzivatele = {
    "tomas": {"Shawshank Redemption", "The Godfather", "The Dark Knight"},
    "petr": {"The Godfather", "The Dark Knight"},
    "marek": {"The Dark Knight", "The Prestige"}
}

film_1 = {
    "JMENO": "Shawshank Redemption",
    "HODNOCENI": "93/100",
    "ROK": 1994,
    "REZISER": "Frank Darabont",
    "STOPAZ": 144,
    "HRAJI": ("Tim Robbins", "Morgan Freeman", "Bob Gunton", "William Sadler",
      "Clancy Brown", "Gil Bellows", "Mark Rolston", "James Whitmore",
      "Jeffrey DeMunn", "Larry Brandenburg"
     )
}

film_2 = {
    "JMENO": "The Godfather",
    "HODNOCENI": "92/100",
    "ROK": 1972,
    "REZISER": "Francis Ford Coppola",
    "STOPAZ": 175,
    "HRAJI": ("Marlon Brando", "Al Pacino", "James Caan",
      "Richard S. Castellano", "Robert Duvall", "Sterling Hayden",
      "John Marley", "Richard Conte"
    )
}

film_3 = {
    "JMENO": "The Dark Knight",
    "HODNOCENI": "90/100",
    "ROK": 2008,
    "REZISER": "Christopher Nolan",
    "STOPAZ": 152,
    "HRAJI": ("Christian Bale", "Heath Ledger", "Aaron Eckhart",
      "Michael Caine", "Maggie Gyllenhaal", "Gary Oldman", "Morgan Freeman",
      "Monique Gabriela", "Ron Dean", "Cillian Murphy"
    )
}

film_4 = {
    "JMENO": "The Prestige",
    "HODNOCENI": "85/100",
    "ROK": 2006,
    "REZISER": "Christopher Nolan",
    "STOPAZ": 130,
    "HRAJI": ("Hugh Jackman", "Christian Bale", "Michael Caine",
      "Piper Perabo", "Rebecca Hall", "Scarlett Johansson", "Samantha Mahurin",
      "David Bowie"
    )
}
filmovy_slovnik = {
    film_1["JMENO"]: film_1,
    film_2["JMENO"]: film_2,
    film_3["JMENO"]: film_3,
    film_4["JMENO"]: film_4
}
from pprint import pprint
pprint(filmovy_slovnik)
jmena = [
    ["Matouš", "Marek", "Lukas", "Jan"],
    ["Lucie", "Aneta", "Michaela"],
    ["Helmut", "Hetfield"]
]
for rada in jmena:
    print(f"{rada = }")
    for jmeno in rada:
        print(f"jmeno = {jmeno}")
limit = 13
for cislo in range(1, limit):
    print(f"Vytvor soubor Vyuctovani_za_{cislo}.mesic.txt")