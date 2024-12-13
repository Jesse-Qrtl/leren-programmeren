PRIJS_COLA = 1.80
PRIJS_BIER = 2.40
PRIJS_CHAMPAGNE = 12.30

MIN_LEEFTIJD_DRANK = 21
MIN_LEEFTIJD_ENTREE = 18

DRANKJES = ('cola', 'bier', 'champagne')
VIP_LIST = ('jeroen', 'jouke', 'rudi')

blauw_bandje = False
rood_bandje = False
stempel = False
minderjarig = False
prijs = 0

leeftijd = int(input('Hoe oud bent u?: '))

if leeftijd >= 18:
    naam = input('Wat is uw naam?: ')
    if naam.lower() in VIP_LIST:
        if leeftijd >= 21:
            blauw_bandje = True
            kleur_band = 'blauw'
        else:
            rood_bandje = True
            kleur_band = 'rood'
        print(f'Je krijg van mij een {kleur_band} bandje.')
    else:
        if leeftijd >= 21:
            stempel = True
    gekozen_drank = input('Wat wilt u drinken?: ')
    if gekozen_drank.lower() in DRANKJES:
        if gekozen_drank.lower() == 'champagne':
            if rood_bandje or blauw_bandje:
                if blauw_bandje:
                    prijs = PRIJS_CHAMPAGNE
                    print(f'Alsjeblieft uw {gekozen_drank} dat is dan {prijs}$.')
                    exit()
                else:
                    print('Sorry u mag niet alcohol bestellen onder de leeftijd van 21.')
                    print(f'Probeer het over {MIN_LEEFTIJD_DRANK - leeftijd} jaar nog eens.')
                    exit()
            else:
                print('Sorry u mag alleen champagne halen als je VIP bent.')
                exit()
        
        elif gekozen_drank.lower() == 'bier':
            prijs = PRIJS_BIER
            if not blauw_bandje and not rood_bandje and not stempel:
                print('Sorry u mag niet alcohol bestellen onder de leeftijd van 21.')
                print(f'Probeer het over {MIN_LEEFTIJD_DRANK - leeftijd} jaar nog eens.')
                exit()
                
        elif gekozen_drank.lower() == 'cola':
            prijs = PRIJS_COLA
            if blauw_bandje or rood_bandje:
                print('Alstublieft complimenten van het huis.')
            else:
                print(f'Alsjeblieft uw {gekozen_drank} dat is dan {prijs}$.')
        else:
            print('Kennen we niet hier water.')
else:
    print('Sorry maar u mag niet naar binnen.')
    print(f'Probeer het over {MIN_LEEFTIJD_ENTREE - leeftijd} jaar nog eens.')