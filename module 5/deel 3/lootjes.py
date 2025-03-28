import random

deelnemers = []
cadeautjes = {}

while True:
    naam = input('Wie doet er mee?: ').strip().lower()
    if naam in deelnemers:
        print('Deze naam had u al ingevoerd.')
    else:
        deelnemers.append(naam)

        wensen = []
        print(f'Wat zijn de drie cadeautjes die {naam} graag zou willen ontvangen?')
        for i in range(1, 4):
            cadeau = input(f'Cadeautje {i}: ').strip()
            wensen.append(cadeau)
        cadeautjes[naam] = wensen

    if len(deelnemers) >= 3:
        extra_naam = input('Doen er nogmeer mensen mee?: ').strip().lower()
        if extra_naam == 'nee':
            break

lootjes = deelnemers[:]
random.shuffle(lootjes)

while True:
    for i in range(len(deelnemers)):
        if deelnemers[i] == lootjes[i]:
            random.shuffle(lootjes)
            break
    else:
        break

while True:
    print(f'\n{deelnemers}')
    naam_checken = input('Welke naam wil je checken?: ').strip().lower()
    if naam_checken in deelnemers:
        index = deelnemers.index(naam_checken)
        lootje = lootjes[index]
        
        print(f"\n{naam_checken} heeft {lootje} getrokken als lootje.")
        print(f"Wensenlijst van {lootje}: {cadeautjes[lootje]}")
    else:
        print("Deze persoon doet niet mee.")
    DoorMet_checken = input('Wil je nog een naam checken?: ').strip().lower()
    if DoorMet_checken == 'nee':
        break