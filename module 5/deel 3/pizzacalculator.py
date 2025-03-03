from value_defs import input_int

pizza_small = 0
pizza_medium = 0
pizza_large = 0

def pizza_multiplier(amount: int, price: float)-> float:
    return float(amount) * price

def pizza_teller(a1: int, a2: int, a3: int)-> int:
    return round(a1 + a2 + a3, 2)

pizza_small_amount = input_int("Hoeveel small pizzas wil je?: ")
pizza_medium_amount = input_int("Hoeveel medium pizzas wil je?: ")
pizza_large_amount = input_int("Hoeveel large pizzas wil je?: ")

pizza_prices = {
    "small_price" : 6.99,
    "medium_price" : 8.99,
    "large_price" : 11.99
}

prijs_small = pizza_multiplier(pizza_small_amount, pizza_prices["small_price"])
prijs_medium = pizza_multiplier(pizza_medium_amount, pizza_prices["medium_price"])
prijs_large = pizza_multiplier(pizza_large_amount, pizza_prices["large_price"])
totaal_prijs_pizzas = pizza_teller(prijs_large, prijs_medium, prijs_small)
totaal_pizzas = pizza_teller(pizza_large_amount, pizza_small_amount, pizza_medium_amount)

print('=============== bon pizzas ===============')
print(f'totaal aantal pizzas {totaal_pizzas}:')
print('-----------------------------------------------')
print(f'- {pizza_small_amount} x small pizza: {prijs_small} euro')
print(f'- {pizza_medium_amount} x medium pizza: {prijs_medium} euro')
print(f'- {pizza_large_amount} x large pizza: {prijs_large} euro')
print('-----------------------------------------------')
print(f'- {totaal_pizzas} x totale pizzas {totaal_prijs_pizzas} euro')
print('-----------------------------------------------')