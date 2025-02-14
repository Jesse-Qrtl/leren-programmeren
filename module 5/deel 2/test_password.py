# password 24 karakters lang!
# Random 2 tot 6 hoofdletters.
# Een hoofdletter mag niet op de twee middelste posities staan.
## Minimaal 8 kleine letters.
## Het wachtwoord mag niet met een kleine letter eindigen.
# 3 speciale tekens uit de volgende reeks: @ # $ % & _ ?.
## De speciale tekens mogen niet op de eerste of laatste positie staan.
# Random 4 tot 7 cijfers (0 t/m 9).
## Op de eerste 3 posities mag geen cijfer staan
import time, string, random
from math import floor

def test_wachtwoord(ww) -> bool:
    if len(ww) < 24:
        print('te kort')
        return False
    if not 1 < len(list(filter(lambda a: a in string.ascii_uppercase, list(ww)))) < 7:
        print('aantal hoofdletters klopt niet!')
        return False
    if ww[11] in string.ascii_uppercase or ww[12] in string.ascii_uppercase:
        print('In het midden geen hoofdletters')
        return False
    if len(list(filter(lambda a: a in string.ascii_lowercase, list(ww)))) < 8:
        print('te weinig kleine letters')
        return False
    if ww[-1] in string.ascii_lowercase:
        print('Laatste pos niet juist')
        return False
    if len(list(filter(lambda a: a in '@#$%&_?', list(ww)))) != 3:
        print('te weinig specials')
        return False
    if ww[0] in '@#$%&_?' or ww[-1] in '@#$%&_?':
        print('special op end')
        return False
    if not 3 < len(list(filter(lambda a: a.isdigit(), list(ww)))) < 8:
        print('te weinig getallen')
        return False
    if ww[0].isdigit() or ww[1].isdigit() or ww[2].isdigit():
        print('Eerste drie karakters staat een getal')
        return False
    return True

def get_wachtwoord() -> str:
    # plaats jouw code hier.
    # Genereer 2-6 hoofdletters
    amount_upper = random.randint(2,6)
    uppercase_letters = random.sample(string.ascii_uppercase, amount_upper)

    # Genereer 18-20 kleineletters
    amount_lower = random.randint(18,20)
    lowercase_letters = random.sample(string.ascii_lowercase, amount_lower)

    # Genereer 3 speciaale tekens
    characters = '@#$%&_?'
    special_characters = random.sample(characters, 3)

    # Genereer 4-7 cijfers
    amount_digits = random.randint(4,6)
    digits = random.sample(string.digits, amount_digits)

    # Voeg alle elementen toe en shuffle ze
    password = uppercase_letters + lowercase_letters + special_characters + digits
    middle_index = [len(password) // 2 - 1, len(password) // 2, len(password) // 2 + 1]

    # Zoek de index van alles dat geen getal is
    non_digit_index = []
    for i in range(3, len(password)):
        if not password[i].isdigit():
            non_digit_index.append(i)

    # Wissel de getallen om die in de eerste 3 elementen staan van het wachtwoord met iets dat geen getal is
    for i in range(3):
        if password[i].isdigit():
            swap_index = random.choice(non_digit_index)
            password[i], password[swap_index] = password[swap_index], password[i]
            non_digit_index.remove(swap_index)

    # Wissel het laatste getal om als het een kleine letter is
    for i in range(len(password) - 1):
        if password[-1].islower() and not password[i].islower():
            password[-1], password[i] = password[i], password[-1]
            break
    
    characters = '@ # $ % & _ ?'
    for i in range(len(password) - 1):
        if password[-1] in characters.split() and not password[i] in characters.split() :
            password[-1], password[i] = password[i], password[-1]
            print(characters.split())
    # Wissel de 2 middelste getallen om als het hoofdletters zijn
    middle_index = [len(password) // 2 - 1, len(password) // 2, len(password) // 2 + 1]
    for i in range(3):
        if password[middle_index[i]].isupper() and not password[i].isupper():
            password[middle_index[i]], password[i] = password[i], password[middle_index[i]]
    return ''.join(password)

# plaats hier de code om minimaal 500 wachtwoorden te testen.
for i in range(500):
    wachtwoord = get_wachtwoord()
    getest_wachtwoord = test_wachtwoord(wachtwoord)
    if getest_wachtwoord == False:
        print(getest_wachtwoord)
        print(wachtwoord)