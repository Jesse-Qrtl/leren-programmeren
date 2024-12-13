import random
import time

speelrondes = 0
geraden_rondes = 0
score = 0

geheim_getal = random.randint(1, 1000)

while speelrondes < 20:
    geraden_rondes += 1
    if geraden_rondes >= 10:
        geheim_getal = random.randint(1, 1000)
        speelrondes += 1
        geraden_rondes = 0
        print(f'U heeft het getal {score} x geraden\n')
        verder_spelen = input('Wilt u verder spelen?: ')
        if verder_spelen.lower() == 'nee':
            print('\nBedankt voor het spelen!')
            break
    
    geraden_getal = int(input('Een getal tussen de 1 en 1000: '))
    verschil = abs(geraden_getal - geheim_getal)
    
    if geraden_getal < geheim_getal:
        print('\nHet getal is hoger.\n')
    elif geraden_getal > geheim_getal:
        print('\nHet getal is lager.\n')
    else:
        score += 1
        geraden_rondes += 10
        print('U heeft het getal geraden!\n')
        time.sleep(1)

    if verschil < 20 and verschil > 0:
        print('U bent heel warm.\n')
    elif verschil < 50 and verschil >= 20:
        print('U bent warm\n')
