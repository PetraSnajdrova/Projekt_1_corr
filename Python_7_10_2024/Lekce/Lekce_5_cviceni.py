kosik = dict()
oddelovac = "=" * 40
sklad = {
    "mleko": [30, 5],  # index '0'-> cena, index '1' -> pocet
    "maso": [100, 1],
    "banan": [30, 10],
    "jogurt": [10, 5],
    "chleb": [20, 5],
    "jablko": [10, 10],
    "pomeranc": [15, 10]
}
nabidka = """
+-----------+----------+
| POTRAVINA |   CENA   |
+-----------+----------+
| mleko     |    30,-  |
| maso      |   100,-  |
| banan     |    30,-  |
| jogurt    |    10,-  |
| chleb     |    20,-  |
| jablko    |    10,-  |
| pomeranc  |    15,-  |
+-----------+----------+
"""
print(f"{"Vítejte u našeho nákupního košíku!".center(len(oddelovac))}\n{oddelovac}{nabidka}")

switch = True
while switch:
    zbozi = input("Vložit do košíku: ")
    if zbozi == "q":
        switch = False
    elif zbozi not in sklad:
        print(f"{zbozi.title()} bohužel není v nabídce")
    elif zbozi not in kosik and sklad[zbozi][1] > 0:
        kosik[zbozi] = [sklad[zbozi][0], 1]
        sklad[zbozi][1] -= 1
    elif sklad[zbozi][1] == 0:
        print(f"Zboží {zbozi} není skladem")
else:
    print(f"{oddelovac}\n{kosik.keys()}")