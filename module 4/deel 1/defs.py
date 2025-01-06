def gegevens_opslaan():
    naam = input('Welke naam?: ').lower()
    leeftijd = int(input('Welke leeftijd?: '))
    stad = input('In welke stad woon je?: ').lower()
    return {'naam': naam, 'leeftijd': leeftijd, 'stad': stad}

def meer_namen():
    personen = []
    while True:
        gegevens_namen = gegevens_opslaan()
        if gegevens_namen in personen:
            print('Deze persoon staat al in de lijst.')
        else:
            personen.append(gegevens_namen)
        verder = input('\nWil je verder?: ').lower()
        if verder == 'nee':
            break
    return personen