# Controleert of een getal een priemgetal is, een getal alleen deekbaar door 1 of zichzelf
def is_prime(number:int) -> bool:
    # als het getal kleiner of gelijk aan 1: False
    if number <= 1:
        return False
    
    # als het getal 2 is: True
    if number == 2:
        return True
    
    # als het gedeeld door elkaar kan zonder overig getal te hebben: False
    if number % 2 == 0:
        return False
    
    # als de wortel van het nummer kan delen door een priem getal: False
    max_divisor = int(number**0.5) + 1
    for d in range(3, max_divisor, 2):
        if number % d == 0:
            return False
    
    # als dat allemaal niet zo is: True
    return True

def priemgetallen_tot(number: int) -> list:
    lijst_priemgetallen = []
    for i in range(2, number + 1):
        if is_prime(i):
            lijst_priemgetallen.append(i)
    return lijst_priemgetallen

def aantal_priemgetallen(aantal: int) -> list:
    lijst_priemgetallen = []
    getal = 2
    while len(lijst_priemgetallen) < aantal:
        if is_prime(getal):
            lijst_priemgetallen.append(getal)
        getal += 1
    return lijst_priemgetallen

def priemgetallen_tussen(begin: int, eind: int) -> list:
    lijst_priemgetallen = []
    for i in range(begin, eind + 1):
        if is_prime(i):
            lijst_priemgetallen.append(i)
    return lijst_priemgetallen