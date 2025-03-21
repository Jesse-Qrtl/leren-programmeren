import random

lootjes = []
deelnemers = {}

while True:
    naam = input('Wie doet er mee?: ').lower()
    if naam in deelnemers:
        print('Deze neemt had u al ingevoerd.')
    else:
        cadeautjes = []
        for i in range(3):
            cadeau = input(f'Wat voor cadeau wil je? {i + 1}: ')
            cadeautjes.append(cadeau)
        deelnemers[naam] = {
            "cadeau" : cadeautjes
        }
        lootjes.append(naam)
    if len(deelnemers) >= 3:
        extra_naam = input('Doen er nogmeer mensen mee?: ').lower()
        if extra_naam == 'nee':
            break

while True:
    gehusseld = True
    random.shuffle(lootjes)
    for i, naam in enumerate(deelnemers):
        for i in range(len(deelnemers)):
            if deelnemers[lootjes[i]] == lootjes[i]:
                gehusseld = False
    if gehusseld:
        break

while True:
    print(f'\n{deelnemers}')
    check_naam = input('Welke naam wil je checken?: ').lower()
    if check_naam in deelnemers:
        index_naam = deelnemers.index(check_naam)
        print(f'\n{deelnemers[check_naam]} heeft {lootjes[index_naam]} getrokken als lootje.')
        verder_checken = input('Wil je nog een naam checken?: ').lower()
        if verder_checken == 'nee':
            break
    else:
        print('Deze persoon doet niet mee.')