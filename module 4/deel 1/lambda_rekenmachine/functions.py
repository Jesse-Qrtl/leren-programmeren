def addition(getal_1: int, getal_2: int) -> float:
    totaal = float(getal_1 + getal_2)
    return totaal

def subtraction(getal_1: int, getal_2: int) -> float:
    totaal = float(getal_1 - getal_2)
    return totaal

def multiplication(getal_1: int, getal_2: int) -> float:
    totaal = float(getal_1 * getal_2)
    return totaal

def division(getal_1:int, getal_2: int) -> float:
    totaal = float(getal_1 / getal_2)
    return totaal

def get_getal(zin: str) -> float:
        while True:
            try:
                return float(input(zin))
            except ValueError:
                print("Ongeldige invoer. Voer een getal in met de juiste waarde.")