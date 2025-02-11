from value_defs import *

def fibonacci(amount: int) -> list:
    lijst = []
    if amount <= 2:
        for i in range(amount):
            lijst.append(i)
        return lijst
    for i in range(amount):
        pass