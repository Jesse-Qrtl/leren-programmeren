def even_getal(getal:int) -> bool:
    return getal % 2 == 0

def zin_omdgedraaid(zin:str) -> str:
    woorden = zin.split()
    omgekeerd = woorden[::-1]
    omgedraaide_zin = ' '.join(omgekeerd)
    return omgedraaide_zin

def unieke_letters_tellen(zin:str) -> int:
    unieke_letters = set(zin)
    letter_teller = len(unieke_letters)
    return letter_teller

def gemmiddelde_letters_per_woord(zin:str) -> float:
    woorden = zin.split()
    
    totale_letters = 0
    for woord in woorden:
        totale_letters += len(woord)

    gemiddelde_aantal_letters = totale_letters / len(woorden)
    return gemiddelde_aantal_letters

def tafel_van(tafel:int, max_getal:int=10) -> None:
    for getal in range(1, max_getal+1):
        resultaat = getal * tafel
        print(f'{getal} x {tafel} = {resultaat}')