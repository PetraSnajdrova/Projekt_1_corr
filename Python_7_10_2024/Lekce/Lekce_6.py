print("Python je cool!")
pozdrav = "ahoj pozemšťane"

listek = [100, 200, "Radim"]

dotazovani = True

while dotazovani:
   odpoved = input("Zadej celé číslo od 1 do 5 ")

   if odpoved.isnumeric() and int(odpoved) in range(1, 6):
       print("Výborně")
       dotazovani = False
   else:
       print("Špatná hodnota, zkus to znovu")
while True:
   odpoved = input("Zadej celé číslo od 1 do 5")

   if odpoved.isnumeric() and int(odpoved) in range(1, 6):
       print("Výborně")
       break
   else:
       print("Špatná hodnota, zkus to znovu")