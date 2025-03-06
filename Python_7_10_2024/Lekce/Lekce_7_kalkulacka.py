# napragramujeme si vlastní kalulačku
# TODO: vypsání nabídky
'''
---------------------------------
 + | - | * | / | sum | pow | quit
---------------------------------
'''
def zobraz_nabidku():
    nabidka = ['+', '-', '*', '/', 'pow', 'avg', 'quit']
    spojeni = ' | '.join(nabidka)
    oddelovac = '-' * len(spojeni)
    print(oddelovac, spojeni, oddelovac, sep='\n')

zobraz_nabidku()

# TODO: průměr
def vypocti_prumer():
    numbers = list()

    while (value := input('Number: ')) != '=':
        if value.isnumeric():
            numbers.append(int(value))

    result = sum(numbers) / len(numbers)
    print(f'Average is {result}')

# vypocti_prumer() - mám zakomentováno, aby se mi funkce nespustila, když ještě není kód celý hotový

# TODO: umocňování
def umocnovani():
    mocnenec = int(input('Zadej mocnence: '))
    mocnitel = int(input('Zadej mocnitele: '))

    vysledek = mocnenec ** mocnitel #existuje vestavěná funkce paw na umocňování

    print(vysledek)

# umocnovani()

# TODO: hlavní funkce kalkulačka (chci, aby to bylo celé řízeno jednou hladní funkcí)
def kalkulacka():
    while True:

        zobraz_nabidku()

        vyber = input('Vyber funkci: ')

        if vyber == 'quit':
            break
        elif vyber == 'avg':
            vypocti_prumer()
        elif vyber == 'paw':
            umocnovani()

kalkulacka()

# TODO: sčítání, odčítání, násobení, dělení (=základní matematické operace)

# TODO: sinus

# TODO: cosinus