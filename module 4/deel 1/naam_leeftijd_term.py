from defs import *
from termcolor import *

lijst_namen = meer_namen()
for persoon in lijst_namen:
    naam_groen = colored(persoon['naam'],"green")
    leeftijd_rood = colored(persoon['leeftijd'], "red")
    stad_geel = colored(persoon["stad"], "yellow")
    if persoon['leeftijd'] < 18:
        minderjarig = colored('nog niet', "red")
    else:
        jaar_oud = persoon['leeftijd']
        jaar_volwassen = jaar_oud - 18
        minderjarig = colored(f'al {jaar_volwassen} jaar', "red")
    print(f"In {stad_geel} woont {naam_groen}, die {minderjarig} volwassen is.")