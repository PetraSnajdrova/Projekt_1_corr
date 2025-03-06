# TODO importy základních knihoven
# příště raději from random import choice
import os
from random import choice, seed

# TODO importy vlastních modulů
# kdybych dala jen import slova a import grafika, dále pak musím všude doplňovat proměnnou
# slova.hadana_slova, takhle je to jednodušší
# from slova import hadana_slova
# from grafika import obesenec

hadana_slova = ['dva', 'hudba', 'vecernicek']

# TODO proměnné
zivoty = 7
hra_bezi = True
# seed(2)
# slovo = choice(hadana_slova)
# print(slovo)
# tajenka = ['_'] * len(slovo)

#### definované funkce ########################
def tajne_slovo(list_tajnych_slov):
    return choice(list_tajnych_slov)

slovo = tajne_slovo(hadana_slova)
print(slovo)


def vytvor_tajenku(vstupni_slovo):
    return ['_'] * len(vstupni_slovo)

tajenka = vytvor_tajenku(slovo)
print(tajenka)

def zobraz_stav_hry(list_s_tajenkou, pocet_zivotu):
    # os.system('cls') #vyčistí terminál (můžu dát do řádku terminálu cls a vyčistí mi ho to)
    print(f"Tajenka: {''.join(list_s_tajenkou)}")
    print(f"Zbyvajici pocet zivotu: {zivoty}")

test = zobraz_stav_hry(tajenka, zivoty)
print(test)

def co_hada_uzivatel():
    return input('Hadej pismeno nebo slovo: ')

test = co_hada_uzivatel()
print(test)

#### beh programu ##############################

#TODO hlavní smyčka hry
# while hra_bezi and zivoty > 0:
    # os.system('cls')
    # print(f"Tajenka: {''.join(tajenka)}")
    # print(f"Zbyvajici pocet zivotu: {zivoty}")

    # zobraz tajenku
    # v průběhu smyčky, dokud nemám hotovo, si dávám break, aby se mi nerozjela nekonečná smyčka
    # a break si posouvám krok po kroku níž a níž, než dokončím smyčku
    # print('Tajenka: ', ' '.join(tajenka))
    
    # input (uložím si do proměnné)
    # hadani = input('Hadej pismeno nebo slovo: ')
    
    # pokud uzivatel uhadl cele slovo
    # if hadani == slovo:
        # hra_bezi = False
        # print('Vyhrál si!')
    
# TODO pokud uzivatel uhadne pismeno
    # elif len(hadani) == 1 and hadani in slovo:
        # for poradi, pismeno in enumerate(slovo):
            # if pismeno == hadani and tajenka[poradi] == "_":
                # tajenka[poradi] = hadani
        # hra_bezi = False if '_' not in tajenka else True
        # print(tajenka)
        # print(slovo)
   
    # TODO pokud uzivatel uhadl spatne pismeno
    # else:
        # print('Zadane pismeno neni v tajence.')
        # zivoty = zivoty - 1
        # zivoty -= 1
        # print(f'Zbyva ti {zivoty} zivotu.')

# TODO vypis else po tom, co je while cyklus prerusen
# else:
    # if not hra_bezi:
        # print('Vyhral jsi')
    # else:
        # print('Prohral jsi')