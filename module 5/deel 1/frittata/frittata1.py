from recipe_lib import *
from frittata_ingredients import *

# -------- TITLE --------
print('=============== Frittata recept ===============')
# -------- INPUT --------
# use recipe_lib for input of nr_persons
nr_persons = input_nr_persons('Hoeveel personen eten mee?: ') # replace this with better input

# ----- CALCULATIONS ----
factor = nr_persons / RECIPE_PERSONS

amount_eggs = round_piece(factor * AMOUNT_EGGS)

amount_milk = round_quarter(factor * AMOUNT_MILK)

amount_salt = round_piece(factor * AMOUNT_SALT)

amount_pepper = round_piece(factor * AMOUNT_PEPPER)

amount_oil = round_piece(factor * AMOUNT_OIL)

amount_onions = round_piece(factor * AMOUNT_ONIONS)

amount_garlics = round_piece(factor * AMOUNT_GARLICS)

amount_spinach = round_piece(factor * AMOUNT_SPINACH)

amount_paprikas = round_piece(factor * AMOUNT_PAPRIKAS)

amount_cheese = round_piece(factor * AMOUNT_CHEESE)

# -------- OUTPUT -------
print('=============== Frittata recept ===============')
print(f'Ingrediënten voor {nr_persons} personen:')
print('-----------------------------------------------')
print(f'- {amount_eggs} {UNIT_EGGS} {TXT_EGGS}')
print(f'- {amount_milk} {UNIT_MILK} {TXT_MILK}')
print(f'- {amount_salt} {UNIT_SALT} {TXT_SALT}')
print(f'- {amount_pepper} {UNIT_PEPPER} {TXT_PEPPER}')
print(f'- {amount_oil} {UNIT_OIL} {TXT_OIL}')
print(f'- {amount_onions} {UNIT_ONIONS} {TXT_ONIONS}')
print(f'- {amount_garlics} {UNIT_GARLICS} {TXT_GARLICS}')
print(f'- {amount_paprikas} {UNIT_PAPRIKAS} {TXT_PAPRIKAS}')
print(f'- {amount_spinach} {UNIT_SPINACH} {TXT_SPINACH}')
print(f'- {amount_cheese} {UNIT_CHEESE} {TXT_CHEESE}')
print('-----------------------------------------------')