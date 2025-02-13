def fibonacci(amount: int) -> list:
    lijst = []
    if amount < 1:
        return lijst
    elif amount <= 2:
        for i in range(amount):
            lijst.append(i)
        return lijst
    
    lijst = [0,1]
    for i in range(amount - 2):
        lijst.append(lijst[-1] + lijst[-2])
    return lijst

print(fibonacci(10))