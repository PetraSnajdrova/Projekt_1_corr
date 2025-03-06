'''
author = Petra Snajdrova
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Petra Snajdrova
email: petrasnajdrova@seznam.cz
"""
oddelovac = "-" * 42
uzivatele = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}

uzivatel = input("Username: ")
heslo = input("Password: ")

if uzivatel in uzivatele:
    if heslo == uzivatele[uzivatel]:
        print(oddelovac)
        print(f"Welcome to the app, {uzivatel}", sep="\n")
        print("We have 3 texts to be analyzed", sep="\n")
        print(oddelovac)
    else:
        print("Incorrect password")
        quit()
else:
    print("Incorrect username!")
    quit()

cislo_textu = input("Enter a number btw. 1, 2 or 3 to select: ")
rozdelena_slova = TEXTS[int(cislo_textu) - 1].split()

if cislo_textu.isdigit():
    cislo_textu = int(cislo_textu)
    if 1 <= cislo_textu <= 3:
        words = rozdelena_slova
        titlecase_words = []
        uppercase_words = []
        lowercase_words = []
        numeric_strings = []
        soucet = []
        vycistena_slova = []
        for slovo in rozdelena_slova:
            ciste_slovo = slovo.strip('.,?!-')
            vycistena_slova.append(ciste_slovo.lower())
            if slovo.istitle():
                titlecase_words.append(slovo)
            elif slovo.isalpha() and slovo.isupper():
                uppercase_words.append(slovo)
            elif slovo.islower():
                lowercase_words.append(slovo)
            elif slovo.isnumeric():
                numeric_strings.append(slovo)
                soucet.append(int(slovo))
        print(oddelovac)
        print(f"There are {len(words)} words in the selected text.")
        print(f"There are {len(titlecase_words)} titlecase words.")
        print(f"There are {len(uppercase_words)} uppercase words.")
        print(f"There are {len(lowercase_words)} lowercase words.")
        print(f"There are {len(numeric_strings)} numeric strings.")
        print(f"The sum of all the numbers {sum(soucet)}")
        print(oddelovac)
    else:
        print("Cislo textu neexistuje!")
        quit()
else:
    print("Zadej cislo, ne text!")
    quit()

delky_slov = [len(slovo) for slovo in vycistena_slova]
print(f"{"LEN":<}|{"OCCURENCES":^{max(delky_slov)+5}}|{"NR.":<}")
print(oddelovac)

for delka in range(1,max(delky_slov)+1):
    print(f"{delka:>3}|{"*"*delky_slov.count(delka):<{max(delky_slov)+5}}|{delky_slov.count(delka):>}")

