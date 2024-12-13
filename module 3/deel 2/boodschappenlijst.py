boodschappenlijst = {}

while True:
    product = input('Welk artikel wit u toevoegen?: ')
    hoeveelheid_producten = int(input('Hoeveel hiervan wilt u toevoegen?: '))
    if product.lower() in boodschappenlijst:
        boodschappenlijst[product] += hoeveelheid_producten
    else:
        boodschappenlijst[product] = hoeveelheid_producten
    meer_producten = input('Wilt u nogmeer producten toevoegen?: ')
    if meer_producten.lower() == 'nee':
        break

print('------[Boodschappenlijstje]-----\n')
for boodschap in boodschappenlijst:
    print(f'{boodschappenlijst[boodschap]} x {boodschap}')
print('\n-------------------------------')