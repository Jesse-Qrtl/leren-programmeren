def input_int(prompt: str) -> int:
  while True:
    try:
      answer = input(prompt + '\n')
      amount = int(answer)
      return amount
    except:
      print(f'Geen geldig getal: {answer}')

def input_float(prompt: str) -> float:
  while True:
    try:
      answer = input(prompt + '\n')
      amount = float(answer)
      return amount
    except:
      print(f'Geen geldig getal: {answer}')