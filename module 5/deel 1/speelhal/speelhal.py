# --> importeer alles uit help.py (zie tip 0)
from help import *

RECEIPT_TEXT = '***** SPEELHAL ENTREE VOOR {personen:2} PERSONEN *****'
RESTART_TEXT = '\nBestelprocedure gestopt door invoerfout!\nHerstart de bestelprocedure!'
MAX_TICKETS = 30
MAX_VR_VIP_SEAT_TIME = 45
VR_VIP_SEAT_PRICE_PERIOD = 5

TICKET_PRICE = 7.50
VR_VIP_SEAT_PERIOD_PRICE = 0.37
COLA_PRICE = 2.10
POPCORN_PRICE = 2.89
VAT_CODE_H = 'H'
VAT_CODE_L = 'L'

# ***************** INPUT *****************
print("SPEELHAL-ENTREE-KASSA")
# --> Vereenvoudig hier de code m.b.v. de help.py function: input_yes_no() (zie tip 1)
answer = input_yes_no("Wilt u bestellen?(J/N)") 

# --> Vereenvoudig hier de conditie met de 'in'-operator (zie tip 2)
if answer in NO_OPTIONS: 
  exit('Nu geen interesse? Tot ziens!')

print('Ik ga u nu vragen wat en hoeveel u wilt...')

# --> Vereenvoudig hier de code m.b.v. de help.py function: input_int() (zie tip 3)
min_tickets = 1
max_tickets = MAX_TICKETS

nr_tickets = input_int("Hoeveel personen?", min_tickets, max_tickets)

# --> Vereenvoudig hier de code m.b.v. de help.py function: input_yes_no() (zie tip 1)
answer = input_yes_no("Ook VR-VIP seats?(J/N)")

# --> Vereenvoudig hier de conditie met de 'in'-operator (zie tip 2)
# --> Vereenvoudig vervolgens de code door de uitkomst van de conditie toe te kennen aan: vr_vip_ordered (tip 4)
vr_vip_ordered = answer in YES_OPTIONS

# --> Vereenvoudig hier de conditie (zie tip 5)
if vr_vip_ordered:
  # --> Vereenvoudig hier de code m.b.v. de help.py function: input_int() (zie tip 3)
  min_seats = 0
  max_seats = nr_tickets

  nr_vr_vip_seats = input_int("Hoeveel VR-VIP seats?", min_seats, max_seats)
  # --> Vereenvoudig hier de code m.b.v. de help.py function: input_int() (zie tip 3)
  min_minuten = 5
  max_minuten = MAX_VR_VIP_SEAT_TIME
  
  vr_vip_seat_time = input_int("hoeveel minuten in de VR-VIP-seats?", min_minuten, max_minuten)

else:
  nr_vr_vip_seats = 0
  vr_vip_seat_time = 0

# --> Vereenvoudig hier de code m.b.v. de help.py function: input_int() (zie tip 3)
min_cola = 0
max_cola = nr_tickets

nr_cola = input_int("Hoeveel cola?", min_cola, max_cola)
# --> Vereenvoudig hier de code m.b.v. de help.py function: input_int() (zie tip 3)
min_popcorn = 0
max_popcorn = nr_tickets

nr_popcorn = input_int("Hoeveel popcorn?", min_popcorn, max_popcorn)
# --> Vereenvoudig hier de code m.b.v. de help.py function: input_yes_no() (zie tip 1)
answer = input_yes_no("Wilt u een factuur met BTW specificatie?(J/N)")

# --> Vereenvoudig hier de conditie met de 'in'-operator (zie tip 2)
# --> Vereenvoudig vervolgens de code door de uitkomst van de conditie toe te kennen aan: vr_vip_ordered (tip 4)
vat_invoice = answer in YES_OPTIONS

# --> Vereenvoudig hier de conditie (zie tip 5)
if vat_invoice:
   company_name = input('Op welke bedrijfsnaam komt de factuur?\n').strip()
   if len(company_name) == 0:
     company_name = '........... (zelf invullen)'

# ***************** CALCULATION *****************
total_tickets = round(nr_tickets * TICKET_PRICE,2)
vr_vip_seat_price = vr_vip_seat_time / VR_VIP_SEAT_PRICE_PERIOD * VR_VIP_SEAT_PERIOD_PRICE
total_vr_vip_seats = round(nr_vr_vip_seats * vr_vip_seat_price, 2)
total_cola = round(nr_cola * COLA_PRICE, 2)
total_popcorn = round(nr_popcorn * POPCORN_PRICE, 2)
total_all = total_tickets + total_vr_vip_seats + total_cola + total_popcorn

# --> Vereenvoudig hier de conditie (zie tip 5)
if vat_invoice:
# --> Vereenvoudig hier de code met de help.py function: get_vat_from_amount_incl() (zie tip 6)
  vat_perc_H = 21 # voor VAT_CODE_H
  total_tickets_vat = get_vat_from_amount_incl(total_tickets, VAT_CODE_H)
  total_vr_vip_seats_vat = get_vat_from_amount_incl(total_vr_vip_seats, VAT_CODE_H)

  vat_perc_L = 9  # voor VAT_CODE_L
  total_cola_ex_vat = get_vat_from_amount_incl(total_cola, VAT_CODE_L)
  total_popcorn_ex_vat = get_vat_from_amount_incl(total_popcorn, VAT_CODE_L)

  total_vat_H = total_tickets_vat + total_vr_vip_seats_vat
  total_vat_L = total_cola_ex_vat + total_popcorn_ex_vat
  total_vat = total_vat_H + total_vat_L

# ***************** OUTPUT *****************
receipt_text = RECEIPT_TEXT.format(personen = nr_tickets)
print(receipt_text+'\n')
if vat_invoice:
  print(f'Factuur voor: {company_name}')
else:
  print(f'Kassabon')\
  
print('-'*len(receipt_text))
print(f'Tickets                   {nr_tickets:2} x {TICKET_PRICE:2.2f} = {total_tickets:6.2f}')
print(f'VR-vip-seats  {vr_vip_seat_time:3} minuten {nr_vr_vip_seats:2} x {vr_vip_seat_price:2.2f} = {total_vr_vip_seats:6.2f}')
print(f'Cola                      {nr_cola:2} x {COLA_PRICE:2.2f} = {total_cola:6.2f}')
print(f'Popcorn                   {nr_popcorn:2} x {POPCORN_PRICE:2.2f} = {total_popcorn:6.2f}')
print('.'*len(receipt_text))
print(f'Totaal:                               {total_all:6.2f}')

print()
# --> Verbeter hier de code met de help.py function: get_vat_perc() en gebruikmakend van de vat codes: VAT_CODE_H en VAT_CODE_L (zie tip 7)
if vat_invoice:
  print(f'BTW Hoog                          {get_vat_perc(VAT_CODE_H):2}% {total_vat_H:6.2f}')
  print(f'BTW Laag                          {get_vat_perc(VAT_CODE_L):2}% {total_vat_L:6.2f}')
print('='*len(receipt_text))
print('Bedankt voor de bestelling, veel plezier!')
# --> Verwijder na succesvolle testen alle refactor instructies uit de code