import time, math
import random

# player stats
player_attack = 1
player_defense = 0
player_health = 3

# player items
rupees = 0

# booleans
schatkist_sleutel = False


# === [kamer 1] === #
print('Door de twee grote deuren loop je een gang binnen.')
print('Het ruikt hier muf en vochtig.')
print('Je ziet een deur voor je.')
print('')
time.sleep(1)

# === [kamer 7] === #
betoverd_k7 = random.randint(1,10)
if betoverd_k7 == 1:
    print('De kamer is leeg.')
else:
    rupees += 1
    print('Je loopt de kamer binnen en ziet een rupee.')
    print('Je neemt hem mee')

keuze_k2_k8 = input('wil je naar kamer 2 of 8?: ')

if keuze_k2_k8 == '2':
# === [kamer 2] === #
    k2_getal_1 = random.randint(10,25)
    k2_getal_2 = random.randint(-5,75)
    operator_somk2_keuze = random.randint(1,3)
    if operator_somk2_keuze == 1:
        antwoord_k2_som = k2_getal_1 + k2_getal_2
        k2_operator = '+'
    elif operator_somk2_keuze == 2:
        antwoord_k2_som = k2_getal_1 - k2_getal_2
        k2_operator = '-'
    elif operator_somk2_keuze == 3:
        antwoord_k2_som = k2_getal_1 * k2_getal_2
        k2_operator = '*'
    print('Je stapt door de deur heen en je ziet een standbeeld voor je.')
    print('Het standbeeld heeft een rupee vast.')
    print('Op zijn borst zit een numpad met de toesten 9 t/m 0.')
    print(f'Daarboven zie je een som staan {k2_getal_1} {k2_operator} {k2_getal_2} = ?')
    antwoord_k2 = int(input('Wat toest je in?: '))

    if antwoord_k2 == antwoord_k2_som:
        print('Het stadbeeld laat de rupee vallen en je pakt het op')
        rupees += 1
    else:
        print('Er gebeurt niets....')

    print('Je zie een deur achter het standbeeld.')
    print('Wil je naar kamer 8 of 6?: ')
    keuze_k8_k6 = input('')
    time.sleep(1)

    if keuze_k8_k6 == '6':
# === [kamer 6] === #
        zombie_attack = 1
        zombie_defense = 0
        zombie_health = 2
        print(f'Dapper loop je de kamer binnen.')
        print('Je loopt tegen een zombie aan.')

        zombie_hit_damage_k6 = (zombie_attack - player_defense)
        if zombie_hit_damage_k6 <= 0:
            print('Jij hebt een te goede verdediging voor de zombie, hij kan je geen schade doen.')
        else:
            zombie_attack_amount_k6 = math.ceil(player_health / zombie_hit_damage_k6)
            
            player_hit_damage_k6 = (player_attack - zombie_defense)
            player_attack_amount_k6 = math.ceil(zombie_health / player_hit_damage_k6)

            if player_attack_amount_k6 < zombie_attack_amount_k6:
                player_health -= player_attack_amount_k6 * zombie_attack
                print(f'In {player_attack_amount_k6} rondes versla je de zombie.')
                print(f'Je health is nu {player_health}.')
            else:
                print('Helaas is de zombie te sterk voor je.')
                print('Game over.')
                exit()
        
        keuze_k8_k6 = input('Wil je naar kamer 3 of 8?: ')
        print('')
        time.sleep(1)
        
    if keuze_k8_k6 == '8':
        # === [kamer 8] === #
            print('Je loopt de kamer binnen en ziet een gokmachine met 2 dobbelstenen.')
            print('Als je wilt gokken kan je de rupees die je hebt verdubbelen.')
            print('Als je hoger gooit dan 7 verdubbelt jouw aantal rupees.')
            print('Als je aantal 7 is verlies je 1 rupee en 4 health.')
            print('Als je aantal minder dan 7 is verlies je 1 health.')
            gok_keuze_k8 = input('Wil je de gok wagen?: ')
            if gok_keuze_k8.lower() == 'ja':
                dobbelstenen_k8 = random.randint(1,12)
                if dobbelstenen_k8 == 7:
                    rupees -= 1
                    player_health -= 4
                    print(f'Je hebt {dobbelstenen_k8} gedobbeld.')
                    print('je hebt nu -1 rupee en -4 health')
                elif dobbelstenen_k8 > 7:
                    rupees = rupees * 2
                    print(f'Je hebt {dobbelstenen_k8} gedobbeld.')
                    print('je hebt je aantal rupees verdubbeld.')
                else:
                    player_health -= 1
                    print(f'Je hebt {dobbelstenen_k8} gedobbeld.')
                    print('Je hebt -1 health.')
            if player_health <= 0:
                print('Je hebt 0 health en bent nu dood.')
                print('Je hebt verloren.')
                quit()

            keuze_k3_k9 = input('Wil je naar kamer 3 of 9?: ')
            if keuze_k3_k9 == '9':
        # === [kamer 9] === #
                print('Je loopt de kamer binnen.')
                random_power_k9 = random.randint(1,2)
                if random_power_k9 == 1:
                    player_health += 2
                    print('Je voelt je opeens gezonder je hebt +2 health.')
                else:
                    player_attack += 1
                    print('Je voelt je opeens sterker je hebt +1 attack')

                print('Je loopt door naar de volgende kamer.')
                
# === [kamer 3] === #
items_for_sale = ['schild','zwaard']
print('Je duwt hem open en stap een hele lange kamer binnen met daarbinnen een merchant.')
while rupees > 0:
    item_kopen_k3 = input('Hij heeft 2 items te koop een schild, zwaard en een sleutel wil je iets kopen?: ')
    if item_kopen_k3.lower() == 'ja':
        welke_item_k3 = input('\nZwaard\n(1 rupee) \n\nSchild\n(1 rupee)\n\nSleutel\n(1 rupee)\n: ')
        if rupees >= 1:
            if welke_item_k3.lower() == 'zwaard':
                rupees -= 1
                player_attack += 2
                item_k3 = 'zwaard'
            elif welke_item_k3.lower() == 'schild':
                rupees -= 1
                player_defense += 1
                item_k3 = 'schild'
            elif welke_item_k3.lower() == 'sleutel':
                rupees -= 1
                schatkist_sleutel = True
        else:
            print('Je hebt geen rupees dus kan niks kopen.')
    else:
        break

print('Op naar de volgende deur.')
print('')
time.sleep(1)

# === [kamer 4] === #
pekka_attack = 2
pekka_defense = 0
pekka_health = 3

print(f'Dapper loop je de kamer binnen.')
print('Je loopt tegen een pekka aan.')

pekka_hit_damage_k4 = (pekka_attack - player_defense)
if pekka_hit_damage_k4 <= 0:
    print('Jij hebt een te goede verdediging voor de pekka, hij kan je geen schade doen.')
else:
    pekka_attack_amount_k4 = math.ceil(player_health / pekka_hit_damage_k4)
    
    player_hit_damage_k4 = (player_attack - pekka_defense)
    player_attack_amount_k4 = math.ceil(pekka_health / player_hit_damage_k4)

    if player_attack_amount_k4 < pekka_attack_amount_k4:
        player_health -= player_attack_amount_k4 * pekka_attack
        print(f'In {player_attack_amount_k4} rondes versla je de pekka.')
        print(f'Je health is nu {player_health}.')
    else:
        print('Helaas is de pekka te sterk voor je.')
        print('Game over.')
        exit()
print('')
time.sleep(1)

# === [kamer 5] === #
print('Voorzichtig open je de deur, je wilt niet nog een zombie of pekka tegenkomen.')
print('Tot je verbazig zie je een schatkist in het midden van de kamer staan.')
print('Je loopt er naartoe.')

if schatkist_sleutel:
    print('Je hebt de sleutel uit kamer 2 gevonden en kan nu de schatkist openen.')
    print('Je hebt het spel gewonnen')
else:
    print('Je hebt geen sleutel om de schatkist te openen.')
    print('Je verliest het spel')