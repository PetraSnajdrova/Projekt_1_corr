def je_anagram(*args) -> bool:
    """
    Vrati boolean True, pokud jsou vsechny parametry anagramy.
    Jinak vrati False.

    Priklad:
    >>> print(je_anagram("ship", "hips", "hisp"))
    True
    >>> print(je_anagram_matous("ship", "hips", "duck"))
    False
    """
    vzor = sorted(args[0])

    for slovo in args:
        if sorted(slovo) != vzor:
            return False
    else:
        return True


print(
    je_anagram("ship", "hips", "hisp"),
    je_anagram("ship", "hips", "duck"),
    sep="\n"
)

adresy = [
   "matous@holinka.com",
   "danek11@seznam.cz",
   "rennud15@gmail.com",
   "pepa@centrum.cz"
]

def filtruj_adresy_s_cisly(emaily: list) -> list:
    """
    Ze zadaneho objektu emailu vyber pouze ty, ktere obsahuji ciselne znaky.

    Priklad:
    >>> print(filtruj_adresy_s_cisly(["matous@holinka.com", "danek11@seznam.cz"]))
    ["danek11@seznam.cz"]
    """
    ciselne_hodnoty = []

    for email in emaily:
        for znak in email:
            if not znak.isnumeric():
                continue
            ciselne_hodnoty.append(email)
            break

    return ciselne_hodnoty

# Uloz vystup funkce do promenne
vysledek = filtruj_adresy_s_cisly(adresy)

# Vytiskni obsah promenne vysledek
print(vysledek)


def je_prvocislo(cislo: int, prvocisla: tuple) -> bool:
    """
    Vrat boolean hodnotu True, pokud je zadane cislo     prvocislo.

    Jinak vrat False.

    Priklad:
    >>> print(je_prvocislo(23, (2, 3, 5, 7, 11, 13, 17, 19, 23)))
    True

    >>> print(je_prvocislo(10, (2, 3, 5, 7, 11, 13, 17, 19, 23)))
    False
    """
    return cislo in prvocisla


def generuj_interval_prvocisel(stop: int) -> tuple:
    """
    Vrat interval hodnot od start do stop.

    Priklad:
    >>> print(generuj_interval_prvocisel(10))
    (2, 3, 5, 7)

    >>> print(generuj_interval_prvocisel(20))
    (2, 3, 5, 7, 11, 13, 17, 19)
    """
    vsechna_cisla = tuple(range(stop + 1))
    vysledek = list()

    for cislo in vsechna_cisla:
        if cislo == 0 or cislo == 1:
           continue

        for filtr_cislo in range(2, cislo):
            if cislo % filtr_cislo == 0:
                break
        else:
            vysledek.append(cislo)

    return tuple(vysledek)


print(
    je_prvocislo(23, generuj_interval_prvocisel(30)),
    je_prvocislo(233, generuj_interval_prvocisel(300)),
    je_prvocislo(146, generuj_interval_prvocisel(300)),
    sep="\n"
)


# Vytvor promennou text a uloz do ni zadany text
text = '''\
Lorem ipsum dolor sit amet, consectetur adipiscing
elit. Mauris vulputate lacus id eros consequat tempus.
Nam viverra velit sit amet lorem lobortis, at tincidunt
nunc ultricies. Duis facilisis ultrices lacus, id
tiger123@email.cz auctor massa molestie at. Nunc 
tristique fringilla congue. Donec ante diam cnn@info.com, dapibus lacinia vulputate vitae, ullamcorper in justo. Maecenas massa purus, ultricies a dictum ut, dapibus vitae massa. Cras abc@gmail.com vel libero felis. In augue elit, porttitor nec molestie quis, auctor a quam. Quisque b2b@money.fr pretium dolor et tempor feugiat. Morbi libero lectus, porttitor eu mi sed, luctus lacinia risus. Maecenas posuere leo sit amet spam@info.cz. elit tincidunt maximus. Aliquam erat volutpat. Donec eleifend felis at leo ullamcorper cursus. Pellentesque id dui viverra, auctor enim ut, fringilla est. Maecenas gravida turpis nec ultrices aliquet.'''


def uloz_emailove_adresy(text: str) -> list:
    """
    Uloz vsechny ocistene emailove adresy ze zadaneho textu.

    Priklad:
    >>> print(uloz_emailove_adresy("Ahoj, tady matous@gmail.com."))
    {'matous@gmail.com'}

    >>> print(uloz_emailove_adresy("Ahoj, tady matous"))
    {}
    """
    return [
        slovo.strip(",.:;")
        for slovo in text.split()
        if "@" in slovo
    ]


# Uloz vystup funkce do promenne
vysledek = uloz_emailove_adresy(text)

# Vytiskni obsah promenne vysledek
print(vysledek)