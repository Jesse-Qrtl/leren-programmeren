import random

lootjes = []
deelnemers = []

while True:
    naam = input('Wie doet er mee?: ').lower()
    if naam in deelnemers:
        print('Deze neemt had u al ingevoerd.')
    else:
        lootjes.append(naam)
        deelnemers.append(naam)
    if len(deelnemers) >= 3:
        extra_naam = input('Doen er nogmeer mensen mee?: ').lower()
        if extra_naam == 'nee':
            break

while True:
    gehusseld = True
    random.shuffle(lootjes)
    for i in range(len(deelnemers)):
        if deelnemers[i] == lootjes[i]:
            gehusseld = False
    if gehusseld:
        break

