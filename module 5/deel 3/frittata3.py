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

amount_salt = round_quarter(factor * AMOUNT_SALT)

amount_pepper = round_quarter(factor * AMOUNT_PEPPER)

amount_oil = round_quarter(factor * AMOUNT_OIL)

amount_onions = round_piece(factor * AMOUNT_ONIONS)

amount_garlics = round_piece(factor * AMOUNT_GARLICS)

amount_spinach = round_quarter(factor * AMOUNT_SPINACH)

amount_paprikas = round_piece(factor * AMOUNT_PAPRIKAS)

amount_cheese = round_quarter(factor * AMOUNT_CHEESE)

# -------- OUTPUT -------
print('=============== Frittata recept ===============')
print(f'Ingrediënten voor {nr_persons} personen:')
print('-----------------------------------------------')
print(f'- {amount_eggs} {str_single_plural(amount_eggs,TXT_EGGS)}')
print(f'- {str_amount_fraction(amount_milk)} {str_units(amount_milk,UNIT_MILK)} {TXT_MILK} {round(unit2ml(amount_milk,UNIT_MILK))} ml')
print(f'- {str_amount_fraction(amount_salt)} {str_units(amount_salt,UNIT_SALT)} {TXT_SALT} {ml2gram(unit2ml(amount_salt, UNIT_SALT), GRAM_PER_ML_SALT)} gram')
print(f'- {str_amount_fraction(amount_pepper)} {str_units(amount_pepper,UNIT_PEPPER)} {TXT_PEPPER} {ml2gram(unit2ml(amount_pepper, UNIT_PEPPER), GRAM_PER_ML_PEPPER)} gram')
print(f'- {str_amount_fraction(amount_oil)} {str_units(amount_oil,UNIT_OIL)} {TXT_OIL} {round(unit2ml(amount_oil,UNIT_OIL),1)} ml')
print(f'- {amount_onions} {str_single_plural(amount_onions,TXT_ONIONS)}')
print(f'- {amount_garlics} {str_single_plural(amount_garlics,TXT_GARLICS)}')
print(f'- {amount_paprikas} {str_single_plural(amount_paprikas,TXT_PAPRIKAS)}')
print(f'- {str_amount_fraction(amount_spinach)} {str_units(amount_spinach,UNIT_SPINACH)} {TXT_SPINACH} {round(ml2gram(unit2ml(amount_spinach, UNIT_SPINACH), GRAM_PER_ML_SPINACH))} gram')
print(f'- {str_amount_fraction(amount_cheese)} {str_units(amount_cheese,UNIT_CHEESE)} {TXT_CHEESE} {round(ml2gram(unit2ml(amount_cheese, UNIT_CHEESE), GRAM_PER_ML_CHEESE))} gram')
print('-----------------------------------------------')