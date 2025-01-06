from functions import *

geldige_keuze = True
n1 = None
resultaat = 0

choice = input("A) getallen optellen, \nB) getallen aftrekken, \nC) getallen vermenigvuldigen, \nD) getallen delen, \nE) getal ophogen, \nF) getal verlagen, \nG) getal verdubbelen of \nH) getal halveren \nwat wilt u doen?: ").lower()

while True:
    if n1 == None:
        n1 = get_getal('eerste getal: ')
    else:
        n1 = resultaat
    if choice == 'a' or 'b' or 'c' or 'd':
        n2 = get_getal('tweede getal: ')
    elif choice == 'e' or 'f':
        n2 = 1
    elif choice == 'g' or 'h':
        n2 = 2

    if choice == 'a':
        resultaat = addition(n1,n2)
        operator = '+'
    elif choice == 'b':
        resultaat = subtraction(n1,n2)
        operator = '-'
    elif choice == 'c':
        resultaat = multiplication(n1,n2)
        operator = 'x'
    elif choice == 'd':
        resultaat = division(n1,n2)
        operator = ':'
    elif choice == 'e':
        resultaat = addition(n1,n2)
        operator = '+'
    elif choice == 'f':
        resultaat = subtraction(n1,n2)
        operator = '-'
    elif choice == 'g':
        resultaat = multiplication(n1,n2)
        operator = 'x'
    elif choice == 'h':
        resultaat = division(n1,n2)
        operator = ':'
    else:
        geldige_keuze = False
        print('Deze keuze bestaat niet.')

    if geldige_keuze:
        print(f'{n1} {operator} {n2} = {resultaat}')

    choice = input(f"\nA) iets optellen, \nB) iets aftrekken, \nC) met iets vermenigvuldigen, \nD) ergens door delen, \nE) ophogen, \nF) verlagen, \nG) verdubbelen, \nH) halveren of \nI) niets \nWil je wat met de uitkomst ({resultaat}) doen?: ").lower()
    if choice == 'i':
        break