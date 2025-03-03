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

    # Genereer 3 speciaale tekens
    special_characters = random.sample('@#$%&_?', 3)

    # Genereer 4-7 cijfers
    amount_digits = random.randint(4,7)
    digits = random.sample(string.digits, amount_digits)

    # Voeg alle elementen toe en shuffle ze
    password = uppercase_letters + special_characters + digits
    amount_lower = 24 - len(password)
    
    # Genereer kleineletters
    lowercase_letters = random.sample(string.ascii_lowercase, amount_lower)
    password += lowercase_letters
    
    middle_index = [11, 12]

    while True:
        random.shuffle(password)

        if password[0] in '@#$%&_?' or password[-1] in '@#$%&_?':
            return get_wachtwoord()
        if password[0].isdigit() or password[1].isdigit() or password[2].isdigit():
            return get_wachtwoord()
        if password[-1].islower():
            return get_wachtwoord()
        if password[middle_index[0]].isupper() or password[middle_index[1]].isupper():
            return get_wachtwoord()
        return ''.join(password)

# plaats hier de code om minimaal 500 wachtwoorden te testen.
for i in range(500):
    wachtwoord = get_wachtwoord()
    getest_wachtwoord = test_wachtwoord(wachtwoord)
    if getest_wachtwoord == False:
        print(getest_wachtwoord)
        print(wachtwoord)