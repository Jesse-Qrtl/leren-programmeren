from defs import *

lijst_namen = meer_namen()
for persoon in lijst_namen:
    print(f"{persoon['naam']} die in {persoon['stad']} woont, is {persoon['leeftijd']} jaar.")