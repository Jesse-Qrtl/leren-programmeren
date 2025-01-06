from functions import *

print("Welke functie wil je gebruiken?")
print("1: Alle priemgetallen tot en met een bepaald getal.")
print("2: Een specifiek aantal priemgetallen.")
print("3: Priemgetallen tussen twee getallen.")

keuze = input("Voer het nummer van je keuze in (1, 2 of 3): ")

if keuze == "1":
    getal = int(input("Tot en met welk getal wil je de priemgetallen zien?: "))
    result = priemgetallen_tot(getal)
    if result:
        print(f"De priemgetallen tot en met {getal} zijn: {result}")
    else:
        print(f"Er zijn geen priemgetallen tot en met {getal}.")

elif keuze == "2":
    aantal = int(input("Hoeveel priemgetallen wil je zien? "))
    result = aantal_priemgetallen(aantal)
    if result:
        print(f"De eerste {aantal} priemgetallen zijn: {result}")
    else:
        print(f"Er zijn geen priemgetallen om te tonen.")

elif keuze == "3":
    begin = int(input("Voer het begingetal in: "))
    eind = int(input("Voer het eindgetal in: "))
    result = priemgetallen_tussen(begin, eind)
    if result:
        print(f"De priemgetallen tussen {begin} en {eind} zijn: {result}")
    else:
        print(f"Er zijn geen priemgetallen tussen {begin} en {eind}.")

else:
    print("Die keuze bestaat niet.")