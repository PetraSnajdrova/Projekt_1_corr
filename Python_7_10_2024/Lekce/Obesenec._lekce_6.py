# TODO importy základních knihoven
# příště raději from random import choice
import random

# TODO importy vlastních modulů
# kdybych dala jen import slova a import grafika, dále pak musím všude doplňovat proměnnou
# slova.hadana_slova, takhle je to jednodušší
from slova import hadana_slova
from grafika import obesenec

# TODO proměnné
zivoty = 7
hra_bezi = True

# zafixuju si slovo metodou seed, to číslo v závorce si můžu vybrat
random.seed(2)
slovo = random.choice(hadana_slova)
print(slovo)
tajenka = ['_'] * len(slovo)

#TODO hlavní smyčka hry
while hra_bezi and zivoty > 0:

    # zobraz tajenku
    # v průběhu smyčky, dokud nemám hotovo, si dávám break, aby se mi nerozjela nekonečná smyčka
    # a break si posouvám krok po kroku níž a níž, než dokončím smyčku
    print('Tajenka: ', ' '.join(tajenka))
    
    # input (uložím si do proměnné)
    hadani = input('Hadej pismeno nebo slovo: ')
    
    # pokud uzivatel uhadl cele slovo
    if hadani == slovo:
        hra_bezi = False
        print('Vyhrál si!')
    
# TODO pokud uzivatel uhadne pismeno
    elif len(hadani) == 1 and hadani in slovo:
        for poradi, pismeno in enumerate(slovo):
            if pismeno == hadani and tajenka[poradi] == "_":
                tajenka[poradi] = hadani
        hra_bezi = False if '_' not in tajenka else True
        # print(tajenka)
        # print(slovo)
   
    # TODO pokud uzivatel uhadl spatne pismeno
    else:
        print('Zadane pismeno neni v tajence.')
        # zivoty = zivoty - 1
        zivoty -= 1
        print(f'Zbyva ti {zivoty} zivotu.')

# TODO vypis else po tom, co je while cyklus prerusen
else:
    if not hra_bezi:
        print('Vyhral jsi')
    else:
        print('Prohral jsi')



