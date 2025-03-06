import random

moznosti = ['kamen', 'nuzky', 'papir']
hrac = 'kamen'
pocitac = random.choice(moznosti)

print("Hráč:", hrac)
print("Počítač:", pocitac)

if hrac == 'kamen' and pocitac == 'nuzky':
    print('Vyral si')
elif hrac == 'kamen' and pocitac == 'papir':
    print('Prohral si')
else:
    print('nerozhodne')

# nahraj knihovnu 'os'
import os

# zadej absolutní nebo relativní cestu
jmena_slozek = ("obrazky", "texty", "gify")

# vytvoř všechny adresáře v sekvenci `jmeno_slozek`
for jmeno in jmena_slozek:

    # pokud soubor existuje a je to složka, přeskoč jej
    if os.path.exists(jmeno) and os.path.isdir(jmeno):
        print("Složka již existuje!")

    # .. jinak ji vytvoř
    else:
        print("Tvořím novou složku:", jmeno)
        os.mkdir(jmeno)

# jakmile budou všechny složky vytvořené, vypiš oznámení
print("Všechny složky existují")

# Nahraj knihovnu `random`
import random

# Do proměnných ulož nejvyšší a nejnižší hodnoty
# urči rozsah čísel pro hod kostkou
min_hodnota = 1
max_hodnota = 6

while True:
    print("Házím kostkou..")

    # ulož do proměnné výsledek
    kostka_hodnota = random.randint(min_hodnota, max_hodnota)

    # vypiš výsledek
    print("Na kostce je:", kostka_hodnota)


    # pokud uživatel hodí 6, vrať se na začátek smyčky
    if kostka_hodnota == 6:
        continue

    # v opačném případě ukonči smyčku
    else:
        break