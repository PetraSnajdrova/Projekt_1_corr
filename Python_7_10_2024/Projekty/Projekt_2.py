"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Petra Šnajdrová
email: petra.snajdrova@seznam.com
"""

from random import choice, sample

oddelovac = ('-' * 47)

def pozdrav_uzivatele():
    oddelovac = ('-' * 47)
    print('Hi there!')
    print(oddelovac)
    print("I've generated a random 4 digit number for you.", "Let's play a bulls and cows game.", sep="\n")
    print(oddelovac)

def generate_secret_number():
    pass

hadane_cislo = []
for cisla in range(1000,10000):
    hadane_cislo.append(cisla)
cisla = choice(hadane_cislo)
print(cisla) #po napsání celého kódu smazat!! - teď potřebuju vědět to číslo

hadani = input('Enter a number: ')
pokusy = int()

hra_bezi = True

def zkontroluj_tip(hadani):
    if not hadani.isdigit():
        return 'Enter the number not text!'
    if len(hadani) != 4:
        return 'Enter the number with 4 digits!'
    if hadani[0] == '0':
        return 'The number cannot starts with zero!'
    if len(set(hadani)) != 4:
        return 'The number contains duplicates!'

def vyhodnot_tip(tajne_cislo, hadani):
    bulls = sum(tajne_cislo[cislo] == digit for cislo, digit in enumerate(hadani))
    cows = sum(digit in tajne_cislo for digit in hadani) - bulls
    return bulls, cows


if hadani == str(cisla):
    pokusy += 1
    print(f"Correct, you've guessed the right number \nin {pokusy} guesses!")
    hra_bezi = False
    print(oddelovac)
    print('That is amazing!')
                # elif hadani in cislo:
                      #for poradi, cislo in enumerate(hadani):
                        #if cislo == hadani and cislo[poradi] == "_":
                            #cislo[poradi] = hadani
                    #hra_bezi = False if '_' not in cislo else True
else:
    for poradi, cislo in enumerate(str(cisla)):
        if cislo in hadani:
                    # if enumerate(hadani) == enumerate(str(cisla)):?????
            print('Boha jeho')
            pokusy += 1
            break
        else:
            pokusy += 1
            print(f'0 bulls, 0 cows')



#TODO hlavní smyčka hry
# while hra_bezi and zivoty > 0:











