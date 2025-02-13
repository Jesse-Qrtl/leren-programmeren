import random
import string 
from math import floor

# Genereer 2-6 hoofdletters
amount_upper = random.randint(2,6)
upper_positions = ''
uppercase_letters = random.sample(string.ascii_uppercase, amount_upper)

# Genereer 8-10 kleineletters
amount_lower = random.randint(8,10)
lowercase_letters = random.sample(string.ascii_lowercase, amount_lower)

# Genereer 3 speciaale tekens
characters = '@#$%&_?'
special_characters = random.sample(characters, 3)

# Genereer 4-7 cijfers
amount_digits = random.randint(4,6)
digits = random.sample(string.digits, amount_digits)

# Voeg alle elementen toe en shuffle ze
password = uppercase_letters + lowercase_letters + special_characters + digits
random.shuffle(password)

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

# Wissel de 2 middelste getallen om als het hoofdletters zijn
middle_index = [floor(len(password) / 2), floor(len(password) / 2) + 1]
for i in range(2):
    if password[middle_index[i]].isupper() and not password[i].isupper():
        password[middle_index[i]], password[i] = password[i], password[middle_index[i]]

print(f'\nPassword: {"".join(password)}\n')