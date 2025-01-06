def aantal_function_town(getal:int) -> str:
    zin = ""
    for i in range(getal):
        zin += f'Hello from function town {i + 1}\n'
    return zin

aantal_x = int(input('Welk getal?: '))
zin_x = aantal_function_town(aantal_x)
print(zin_x)